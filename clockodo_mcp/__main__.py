import clockodo_mcp.clockodo_mcp
import clockodo_mcp.get # important to load get tools
import clockodo_mcp.delete # important to load delete tools
import clockodo_mcp.create_update # important to load create/update tools

def main():
    mcp = clockodo_mcp.clockodo_mcp.mcp
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--restricted', action='store_true', help='Enable only a restricted tool subset for better performance.')
    args = parser.parse_args()
    mcp.register_tools(restricted=args.restricted)
    mcp.mcp.run(transport="stdio")

if __name__ == "__main__":
    main()


#we have update_entry_group but not create ?
# the post and put method expect payload in the body not as params, maybe flatten_dict does not work here the same as in get. Otherwise it would be cool
# if we could use the same flattening method

# write better comments what functions actually do and represent
# make a release
#write a mcp server description

# search for all delete endpoints again

# get_entries_text filter {
#   "filter": {
#     "users_id": [
#       413898
#     ],
#     "time_since": "2025-12-08T00:00:00Z",
#     "time_until": "2025-12-14T23:59:59Z"
#   },
#   "items": 100,
#   "mode": "reports"
# }

#     {
#       "type": "InvalidDateFormat",
#       "message": "'2025-12-08T00:00:00Z' does not fit the date format 'Y-m-d'.",
#       "details": {
#         "format_example": "Y-m-d"
#       },
#       "path": "filter.time_since"
#     },
#     {
#       "type": "InvalidDateFormat",
#       "message": "'2025-12-14T23:59:59Z' does not fit the date format 'Y-m-d'.",
#       "details": {
#         "format_example": "Y-m-d"
#       },
#       "path": "filter.time_until"
#     }
#   ]
# }