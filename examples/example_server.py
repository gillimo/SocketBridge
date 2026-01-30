"""Minimal SocketBridge server example."""
import time
from socketbridge.server import SocketServer


def handler(msg):
    print("received:", msg)


def main():
    srv = SocketServer(host="127.0.0.1", port=7002, handler=handler, auth_token="secret", verbose=True)
    srv.start()
    print("SocketBridge server running on 127.0.0.1:7002 (token=secret). Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")
        srv.stop()


if __name__ == "__main__":
    main()
