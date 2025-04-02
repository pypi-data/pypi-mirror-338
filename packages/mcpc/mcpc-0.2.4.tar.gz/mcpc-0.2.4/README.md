# MCPC - Model Context Protocol Callback

[![PyPI version](https://badge.fury.io/py/mcpc.svg)](https://badge.fury.io/py/mcpc)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/mcpc.svg)](https://pypi.org/project/mcpc/)

MCPC is an extension to MCP (Model-Context-Protocol) that solves a critical limitation in LLM tool interactions: **enabling continued conversations while running tools background tasks**. It facilitates **asynchronous two-way communication** between LLMs and tools through the already existing MCP transport - no additional transport layer needed, while maintaining full backward compatibility.

<p align="center">
  <img src="assets/mcpc-demo_540.avif" alt="Conceptual demo of MCPC's continuous conversation flow between LLM and tools (UI not included)">
</p>

## What is MCPC?

MCPC is an **extension** to the MCP protocol, not a replacement. It builds upon the existing MCP infrastructure to add real-time two-way communication capabilities while maintaining full compatibility with standard MCP implementations.

MCPC solves a critical limitation in LLM tool interactions: **enabling continuous two-way communication while running background tasks**:

- Bidirectional communication between LLMs and tools using the same MCP transport
- Continuous conversation with LLMs during tool execution
- Real-time updates from background processes
- Asynchronous notifications when operations complete
- Support for indefinitely running tasks with streaming updates

## Compatibility Matrix

| Feature                           | Status             | Notes                                               |
| --------------------------------- | ------------------ | --------------------------------------------------- |
| STDIO Transport                   | ✅ Implemented     | Full support for standard input/output transport    |
| SSE Transport                     | ⚠️ Limited Support | Standard MCP operations only, MCPC features pending |
| MCPC Client → Standard MCP Server | ✅ Implemented     | Full backward compatibility                         |
| Standard MCP Client → MCPC Server | ✅ Implemented     | Automatic fallback to synchronous results           |

## Quick Installation

```bash
# With UV (recommended)
uv add mcpc

# With pip
pip install mcpc
```

## Basic Client Usage

```python
# Initialize the MCPC handler
mcpc_handler = MCPCHandler("my-provider")

# Define your event listener function
async def my_mcpc_listener(mcpc_message: MCPCMessage) -> None:
    print(f"Received MCPC message: {mcpc_message}")
    # Handle the message based on status
    if mcpc_message.type == "task" and mcpc_message.event == "complete":
        print(f"Task {mcpc_message.task_id} completed with result: {mcpc_message.result}")

# Add your event listener for MCPC Message
mcpc_handler.add_event_listener(my_mcpc_listener)

# Wrap the transport with MCPC event listeners
wrapped_transport = await mcpc_handler.wrap_streams(*transport)

# Create a ClientSession with the wrapped transport
session = await ClientSession(*wrapped_transport)

# Initialize MCPC features by checking for MCPC support
mcpc_supported = await mcpc_handler.init_mcpc(session)
if mcpc_supported:
    print(f"MCPC protocol v{mcpc_handler.protocol_version} supported")
```

## Basic Server Usage

```python
# Initialize MCPC helper
server = Server("my-provider")
mcpc = MCPCHelper("my-provider", transport_type="stdio")

@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    metadata = arguments.pop("_metadata", {})
    session_id = metadata.get("mcpc_session_id", "default")
    task_id = metadata.get("mcpc_task_id", str(uuid.uuid4()))

    # Handle protocol information request
    if name == "_is_mcpc_enabled":
        client_info = arguments.get("mcpc_info")
        return mcpc.handle_protocol_info_request(client_info)

    if name == "process_data":
        async def process_data_task():
            await mcpc.send(mcpc.create_task_event(
                event="update",
                tool_name="process_data",
                session_id=session_id,
                task_id=task_id,
                result="Processing data..."
            ))
            await asyncio.sleep(3) # Simulate processing time
            await mcpc.send(mcpc.create_task_event(
                event="complete",
                tool_name="process_data",
                session_id=session_id,
                task_id=task_id,
                result={
                    YOUR_DATA_OBJECT
                }
            ))
        # Start a background task
        collected_messages = mcpc.start_task(task_id, process_data_task)

    # For standard MCP clients, return collected complete/failed messages
    if collected_messages:
        return mcpc.messages_to_text_content(collected_messages)

    # For MCPC clients, return immediate acknowledgment
    response = mcpc.create_task_event(
        event="created",
        tool_name="process_data",
        session_id=session_id,
        task_id=task_id,
        result=f"Started processing data_id={data_id}. Updates will stream in real-time."
    )
    return mcpc.messages_to_text_content([response])
```

## Documentation

For detailed documentation, please see:

- [Getting Started Guide](docs/getting-started.md) - Installation and basic usage
- [Server Implementation](docs/server-implementation.md) - How to implement MCPC in your server
- [API Reference](docs/api-reference.md) - Detailed API documentation
- [Protocol Details](docs/protocol-details.md) - Message structure and protocol information
- [Use Cases](docs/use-cases.md) - Example scenarios and use cases

## License

MIT
