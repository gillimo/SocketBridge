# SocketBridge

Mission Learning Statement
- Mission: Build a lightweight TCP IPC bridge for local agents and tools.
- Learning focus: protocol design, safe defaults, and zero-dependency networking.
- Project start date: 2026-01-30 (inferred from earliest git commit)

Lightweight, stdlib-only TCP IPC bridge for local agents and tools.

## Features

- Length-prefixed JSON frames (no partial or merged reads)
- Loopback-by-default bind
- Auth token + host allowlist
- Max-bytes cap and protocol version check
- Zero dependencies (pure Python stdlib)

## Installation

```bash
pip install socketbridge
```

## Quick Start

```python
from socketbridge.server import SocketServer

def handler(message):
    print("got", message)

srv = SocketServer("127.0.0.1", 7002, handler=handler)
srv.start()
# ... send messages with an auth_token ...
srv.stop()
```

## Usage

Client helper:

```python
from socketbridge.client import send
resp = send("127.0.0.1", 7002, {"type": "ping"}, token="secret")
print(resp)
```

Examples:

```bash
python examples/example_server.py &
python examples/example_client.py --text "hello" --token secret
```

## Architecture

```
Client
  |
  | 4-byte length + JSON (auth_token, protocol_version, payload)
  v
SocketBridge Server (loopback, token/allowlist/max-bytes)
  |--> handler(message)
  ^ 4-byte length + JSON response (status, message, protocol_version)
```

## Project Structure

```
socketbridge/       # Core library
examples/           # Example server/client
```

## Building

No build step required. Run directly with Python.

## Contributing

Issues and PRs welcome.

## License

MIT License - see [LICENSE](LICENSE) for details.
