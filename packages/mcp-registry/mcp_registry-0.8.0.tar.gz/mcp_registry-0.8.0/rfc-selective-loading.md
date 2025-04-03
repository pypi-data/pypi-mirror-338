# RFC: Selective Server and Tool Loading in MCPRegistry

## Summary

This RFC proposes a two-level filtering mechanism for MCP Registry:

1. Server-level filtering via a new `filter_servers` method in ServerRegistry
2. Tool-level filtering via a new `tool_filter` parameter in MCPAggregator

These enhancements will provide a clean, explicit way to work with specific subsets of servers and tools, improving efficiency and flexibility.

## Background and Motivation

Currently, the MCP Registry has limited capabilities for selective loading:

1. In MCPAggregator, we can filter servers but still load all configurations
2. There's no way to selectively load specific tools from a server

This leads to inefficiency, especially in large deployments with many servers and tools where users may only need access to a small subset.

## Proposal

1. Add a `filter_servers` method to ServerRegistry that creates a new registry with only specified servers
2. Add a `tool_filter` parameter to MCPAggregator to control which tools are exposed from each server

## Implementation Phases

### Phase 1: Server-level Filtering

1. Add the `filter_servers` method to ServerRegistry class
2. Update the serve.py command to use this method
3. Add tests for the new method
4. Update documentation

### Phase 2: Tool-level Filtering

1. Add tool filtering capability to MCPAggregator
2. Add tests for tool filtering
3. Update documentation with tool filtering examples

## API Changes

### Phase 1: Server-level Filtering

```python
def filter_servers(self, server_names: list[str]) -> "ServerRegistry":
    """
    Create a new ServerRegistry containing only the specified servers.
    
    Args:
        server_names: List of server names to include in the filtered registry
        
    Returns:
        ServerRegistry: A new registry containing only the specified servers
        
    Raises:
        ValueError: If any of the specified servers are not in the registry
    """
    missing = [name for name in server_names if name not in self.registry]
    if missing:
        raise ValueError(f"Servers not found: {', '.join(missing)}")
        
    filtered = {
        name: settings for name, settings in self.registry.items()
        if name in server_names
    }
    return ServerRegistry(filtered)
```

### Phase 2: Tool-level Filtering

```python
def __init__(
    self, 
    registry: ServerRegistry, 
    server_names: list[str] | None = None, 
    tool_filter: dict[str, list[str] | None] | None = None,
    separator: str = "__"
):
    """
    Initialize the aggregator.
    
    Args:
        registry: ServerRegistry containing server configurations
        server_names: Optional list of specific server names to include (deprecated,
                     prefer using registry.filter_servers() instead)
        tool_filter: Optional dict mapping server names to lists of tool names to include.
                    If a server is mapped to None, all tools from that server are included.
                    If a server is not in the dict, all tools from that server are included.
        separator: Separator string between server name and tool name
    """
    self.registry = registry
    self.server_names = server_names or registry.list_servers()
    self.tool_filter = tool_filter or {}
    self._namespaced_tool_map: dict[str, NamespacedTool] = {}
    self._connection_manager = None
    self._in_context_manager = False
    self.separator = separator
```

## Implementation Considerations

### Two-level Filtering Architecture

This proposal establishes a clear two-level filtering architecture:

1. **Server-level filtering** (which servers to connect to)
   - Implemented at the ServerRegistry level
   - Most efficient because it prevents loading unnecessary server configurations
   - Primary method for reducing resource usage

2. **Tool-level filtering** (which tools to expose from each server)
   - Implemented at the MCPAggregator level
   - Still connects to the server and loads all tools, but only exposes selected ones
   - Useful for reducing API complexity and improving security

### Performance Implications

- Server filtering provides the largest performance gain by eliminating connections
- Tool filtering doesn't reduce connection overhead but simplifies the exposed API
- The combined approach allows for precise control over which functionality is accessible

### Backward Compatibility

The proposed changes maintain backward compatibility:

- Adding a new method to ServerRegistry is non-breaking
- Adding a new optional parameter to MCPAggregator is non-breaking
- The existing server_names parameter is maintained but marked as deprecated

## Example Usage

### Phase 1: Server-level Filtering

#### CLI Implementation

```python
# In serve.py
def serve(servers, project):
    # ... existing code to load available_servers ...
    
    # Create registry with all available servers
    registry = ServerRegistry(available_servers)
    
    # If specific servers requested, filter the registry
    if servers:
        try:
            registry = registry.filter_servers(list(servers))
            click.echo(f"Serving {len(registry.registry)} servers: {', '.join(registry.registry.keys())}", err=True)
        except ValueError as e:
            click.echo(f"Error: {str(e)}", err=True)
            return
    else:
        click.echo(f"Serving all {len(registry.registry)} available servers", err=True)
    
    # Run the compound server with pre-filtered registry
    asyncio.run(run_registry_server(registry))
```

#### Programmatic Usage

```python
# Create a registry with all servers
full_registry = ServerRegistry.from_config(config_path)

# Filter at the server level - only connect to memory and github
filtered_registry = full_registry.filter_servers(["memory", "github"])

# Create an aggregator with the filtered registry
aggregator = MCPAggregator(filtered_registry)

# Use the aggregator with only the selected servers
tools = await aggregator.list_tools()
result = await aggregator.call_tool("memory__get", {"key": "test"})
```

### Phase 2: Tool-level Filtering

```python
# Create a registry with all servers
full_registry = ServerRegistry.from_config(config_path)

# Filter at the server level - only connect to memory and github
filtered_registry = full_registry.filter_servers(["memory", "github"])

# Filter at the tool level - only expose certain tools from each server
tool_filter = {
    "memory": ["get", "set"],  # Only include get/set from memory
    "github": ["list_repos", "create_issue"],  # Only specific github tools
}

# Create an aggregator with both filtering levels
aggregator = MCPAggregator(filtered_registry, tool_filter=tool_filter)

# Use the aggregator with only the selected servers and tools
tools = await aggregator.list_tools()
result = await aggregator.call_tool("memory__get", {"key": "test"})
```

## Testing Plan

### Phase 1 Tests

1. Test `filter_servers` with valid server names
2. Test `filter_servers` with missing server names (should raise ValueError)
3. Test `filter_servers` with empty list (should return empty registry)
4. Integration test with `serve` command
5. Test programmatic usage with filtered registry

### Phase 2 Tests

1. Test tool filtering with specific tools from specific servers
2. Test tool filtering with None for a server (include all tools)
3. Test tool filtering with empty list for a server (include no tools)
4. Test tool filtering with mix of specified servers and unspecified servers
5. Integration test with both filtering mechanisms

## Conclusion

The proposed two-level filtering mechanism provides a clean, explicit, and flexible way to work with specific subsets of servers and tools. The phased implementation approach allows for careful testing and validation at each step.