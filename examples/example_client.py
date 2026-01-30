"""Minimal SocketBridge client example."""
import argparse
from socketbridge.client import send


def main():
    parser = argparse.ArgumentParser(description="Send a JSON message via SocketBridge")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=7002)
    parser.add_argument("--text", default="ping")
    parser.add_argument("--token", default="")
    args = parser.parse_args()

    payload = {"type": "message", "text": args.text}
    resp = send(args.host, args.port, payload, token=args.token or None)
    print("response:", resp)


if __name__ == "__main__":
    main()
