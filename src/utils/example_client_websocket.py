import websocket
ws = websocket.WebSocket()
ws.connect("ws://localhost:8765")

try:
    while True:
        print(ws.recv())
finally:
    ws.close()
