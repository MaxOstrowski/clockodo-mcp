import yaml
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from enum import Enum, IntEnum

import re

def sanitize_name(val):
    # Replace non-alphanumeric with underscores
    s = re.sub(r'\W+', '_', val)
    # Remove leading digits
    if s and s[0].isdigit():
        s = '_' + s
    return s

def load_openapi_yaml(path: str) -> Dict[str, Any]:
	with open(path, "r") as f:
		return yaml.safe_load(f)

class SchemaExtractor:
	def __init__(self, spec: Dict[str, Any]):
		self.spec = spec
		self.enums = {}
		self.models = {}

	### this is bad to do this on the string level, but for now it works
	def get_dependencies(self, code: str) -> List[str]:
		# Find referenced model/enum/type alias names in the code
		# Match both capitalized and lowercase identifiers that are known models/enums
		import re
		# Collect all known names (models and enums)
		known_names = set(self.models.keys()) | set(self.enums.keys())
		# Regex matches all word-like identifiers
		identifiers = re.findall(r'\b([A-Za-z_][A-Za-z0-9_]*)\b', code)
		# Return only those that are in known_names (excluding self-dependencies in topo_sort)
		return [name for name in identifiers if name in known_names]

	def topo_sort(self, items: Dict[str, str]) -> List[str]:
		# Topological sort of items by dependencies
		graph = {name: set(self.get_dependencies(code)) for name, code in items.items()}
		# Remove self-dependencies and filter to only known items
		for name in graph:
			graph[name] = {dep for dep in graph[name] if dep in items and dep != name}
		visited = set()
		result = []
		def visit(n):
			if n in visited:
				return
			visited.add(n)
			for dep in graph[n]:
				visit(dep)
			result.append(n)
		for n in items:
			visit(n)
		return result

	def extract_schema(self, schema: Dict[str, Any], name: str = "Model") -> str:
		# Always return the model/enum name, only store code in self.models/self.enums
		if "$ref" in schema:
			ref = schema["$ref"].split("/")[-1]
			ref_schema = self.spec.get("components", {}).get("schemas", {}).get(ref)
			if ref_schema and "enum" in ref_schema:
				# Always reference the enum class name (use schema name directly)
				return ref
			return ref
		if "oneOf" in schema:
			# Handle oneOf schemas as Union types
			union_types = []
			for subschema in schema["oneOf"]:
				if "$ref" in subschema:
					ref = subschema["$ref"].split("/")[-1]
					union_types.append(self.extract_schema({"$ref": subschema["$ref"]}, ref))
				else:
					union_types.append(self.extract_schema(subschema, name + "Sub"))
			union_type_str = f"Union[{', '.join(union_types)}]"
			# Generate a type alias for the union
			self.models[name] = f"{name} = {union_type_str}"
			return name
		# Handle top-level primitive type schemas (type: boolean, integer, string, number, array)
		t = schema.get("type")
		if t in ["boolean", "integer", "string", "number"]:
			py_type = {
				"boolean": "bool",
				"integer": "int",
				"string": "str",
				"number": "float"
			}
			self.models[name] = f"{name} = {py_type[t]}"
			return name
		if t == "array":
			item_type = self.extract_schema(schema["items"], name + "Item")
			self.models[name] = f"{name} = List[{item_type}]"
			return name
		if schema.get("type") == "object":
			model_name = name
			if model_name in self.models:
				return model_name
			props = schema.get("properties", {})
			required = schema.get("required", [])
			fields = []
			for prop, prop_schema in props.items():
				# Enum handling
				if "enum" in prop_schema:
					enum_name = prop.capitalize()
					enum_type = "IntEnum" if prop_schema.get("type") == "integer" else "Enum"
					enum_values = prop_schema["enum"]
					enum_names = prop_schema.get("x-enumNames", [])
					# Fallback for missing names or empty string values
					fallback_names = []
					for i, v in enumerate(enum_values):
						if enum_names and i < len(enum_names):
							name = enum_names[i]
						else:
							if v == "":
								name = "EMPTY"
							else:
								name = sanitize_name(str(v))
						# Ensure valid Python identifier
						name = sanitize_name(name)
						fallback_names.append(name)
					enum_items = "\n".join([f"    {name} = {repr(value)}" for name, value in zip(fallback_names, enum_values)])
					enum_code = f"class {enum_name}({enum_type}):\n{enum_items}\n"
					if enum_name not in self.enums:
						self.enums[enum_name] = enum_code
					field_type = enum_name
				elif prop_schema.get("type") == "object":
					# Recursively generate nested model
					nested_name = f"{model_name}_{prop.capitalize()}Model"
					field_type = self.extract_schema(prop_schema, nested_name)
				else:
					field_type = self.extract_schema(prop_schema, prop.capitalize())
				# Determine nullability
				t = prop_schema.get("type")
				is_nullable = False
				if isinstance(t, list):
					is_nullable = "null" in t
				elif t == "null":
					is_nullable = True
				# Required and nullable: Optional[...] (no default)
				# Required and not nullable: type (no default)
				# Not required: Optional[...] = None
				field_args = []
				if "description" in prop_schema:
					desc = prop_schema["description"].replace('"', '\"').replace("\n", "\\n")
					field_args.append(f'description="{desc}"')
				if "example" in prop_schema:
					field_args.append(f'example={repr(prop_schema["example"])}')
				field_args_str = f"Field(None, {', '.join(field_args)})" if field_args else "None"
				if prop in required:
					if is_nullable:
						field_str = f"    {prop}: Optional[{field_type}]"
					else:
						field_str = f"    {prop}: {field_type}"
				else:
					field_str = f"    {prop}: Optional[{field_type}] = None"
				if field_args:
					# Add Field(...) if there are extra args
					if prop in required:
						field_str += f" = {field_args_str}"
					else:
						# Already has = None
						field_str = field_str.replace("= None", f"= {field_args_str}")
				fields.append(field_str)
			class_code = f"class {model_name}(BaseModel):\n" + ("\n".join(fields) if fields else "    pass")
			self.models[model_name] = class_code
			return model_name
		elif schema.get("type") == "array":
			item_type = self.extract_schema(schema["items"], name + "Item")
			return f"List[{item_type}]"
		else:
			t = schema.get("type")
			if "enum" in schema:
				enum_name = name
				enum_type = "IntEnum" if t == "integer" else "Enum"
				enum_values = schema["enum"]
				enum_names = schema.get("x-enumNames", [])
				fallback_names = []
				for i, v in enumerate(enum_values):
					if enum_names and i < len(enum_names):
						name = enum_names[i]
					else:
						if v == "":
							name = "EMPTY"
						else:
							name = sanitize_name(str(v))
					fallback_names.append(name)
				enum_items = "\n".join([f"    {name} = {repr(value)}" for name, value in zip(fallback_names, enum_values)])
				enum_code = f"class {enum_name}({enum_type}):\n{enum_items}\n"
				if enum_name not in self.enums:
					self.enums[enum_name] = enum_code
				return enum_name
			if isinstance(t, list):
				py_type = {
						"integer": "int",
						"string": "str",
						"boolean": "bool",
						"number": "float",
						"null": "None"
					}
				if len(t) == 1:
					return py_type.get(t[0], "Any")
				else:
					return f"Union[{', '.join(py_type.get(tt, 'Any') for tt in t)}]"
			else:
				if t == "integer":
					return "int"
				elif t == "string":
					return "str"
				elif t == "boolean":
					return "bool"
				elif t == "number":
					return "float"
				else:
					return "Any"
				
	def extract_path_inputs_and_json_schemas(self, path_def: Dict[str, Any], endpoint_name: str = "endpoint") -> None:
		"""
		Extract input models and their JSON schemas for a single path endpoint definition.
		Returns a dict: {method: {model: str, json_schema: dict}}
		"""
		for method, details in path_def.items():
			input_models = {}
			# Parameters
			params = details.get("parameters", [])
			for param in params:
				pname = param["name"]
				schema = param.get("schema", param.get("content", {}).get("application/json", {}).get("schema"))
				if schema:
					model_name = f"{sanitize_name(endpoint_name)}_{method}_{pname}_InputModel"
					model_code = self.extract_schema(schema, model_name)
					input_models[pname] = {"model": model_code, "json_schema": None}
			# Request body
			if "requestBody" in details:
				body_schema = details["requestBody"]["content"]["application/json"]["schema"]
				model_name = f"{sanitize_name(endpoint_name)}_{method}_RequestBodyModel"
				model_code = self.extract_schema(body_schema, model_name)
				input_models["requestBody"] = {"model": model_code, "json_schema": None}
			model_name = f"{sanitize_name(endpoint_name)}_{method}_InputModel"
			model_code = f"class {model_name}(BaseModel):\n"
			for pname, model_info in input_models.items():
				model_code += f"    {pname}: {model_info['model']}\n"
			if len(input_models) == 0:
				model_code += "    pass\n"
			self.models[model_name] = model_code


	def extract_all(self) -> None:
		schemas = self.spec.get("components", {}).get("schemas", {})
		for schema_name, schema_def in schemas.items():
			self.extract_schema(schema_def, schema_name)

		paths = self.spec.get("paths", {})
		for path, path_def in paths.items():
			endpoint_name = path.strip("/").replace("/", "_") or "root"
			self.extract_path_inputs_and_json_schemas(path_def, endpoint_name)

def main():
	spec = load_openapi_yaml("openapi.yaml")

	print("from pydantic import BaseModel, Field")
	print("from typing import List, Optional, Union, Any")
	print("from enum import Enum, IntEnum\n")

	extractor = SchemaExtractor(spec)
	extractor.extract_all()
	# Topologically sort enums and models
	enum_order = extractor.topo_sort(extractor.enums)
	model_order = extractor.topo_sort(extractor.models)
	print("# All extracted Enums\n")
	for name in enum_order:
		print(extractor.enums[name])
		print()
	print("# All referenced schemas as Pydantic models\n")
	for name in model_order:
		print(extractor.models[name])
		print()
if __name__ == "__main__":
	main()