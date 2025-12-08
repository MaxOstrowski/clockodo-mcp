# Clockodo MCP Server

This is an MCP server for the clockodo API, no webhooks.

## Usage

To run the server:

```bash
python -m clockodo_mcp
```

To inspect the endpoints use:

```bash
npx -y @modelcontextprotocol/inspector
```


The datamodel for the payload was generated using

```bash
datamodel-codegen --input openapi.yaml --output clockodo_mcp/payload_models.py --output-model-type pydantic_v2.BaseModel
```
with the openapi.yaml that was provided by clockodo. (use datmodel-codegen >= 0.4.0)


## Known problems:
datamodel-codegen is used and some enums lose their names (CustomerColor), bugreport is open


I do not yet know how to use the changeRequests to delete or change an entry
