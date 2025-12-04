
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

	def extract_schema(self, schema: Dict[str, Any], name: str = "Model") -> str:
		# Always return the model/enum name, only store code in self.models/self.enums
		if "$ref" in schema:
			ref = schema["$ref"].split("/")[-1]
			ref_schema = self.spec.get("components", {}).get("schemas", {}).get(ref)
			if ref_schema and "enum" in ref_schema:
				# Always reference the enum class name
				return ref + "Enum"
			return ref
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
					enum_name = prop.capitalize() + "Enum"
					enum_type = "IntEnum" if prop_schema.get("type") == "integer" else "Enum"
					enum_values = prop_schema["enum"]
					enum_names = prop_schema.get("x-enumNames", [sanitize_name(str(v)) for v in enum_values])
					enum_items = "\n".join([f"    {name} = {repr(value)}" for name, value in zip(enum_names, enum_values)])
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
				enum_name = name + "Enum"
				enum_type = "IntEnum" if t == "integer" else "Enum"
				enum_values = schema["enum"]
				enum_names = schema.get("x-enumNames", [sanitize_name(str(v)) for v in enum_values])
				enum_items = "\n".join([f"    {name} = {repr(value)}" for name, value in zip(enum_names, enum_values)])
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
	print("# All extracted Enums\n")
	for name, code in extractor.enums.items():
		print(code)
		print()
	print("# All referenced schemas as Pydantic models\n")
	for name, code in extractor.models.items():
		print(code)
		print()
if __name__ == "__main__":
	main()