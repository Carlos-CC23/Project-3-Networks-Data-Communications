import socket
from special_encoder import encode_integer

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER] Connected by {addr}")
        data = conn.recv(1024).decode()
        if data:
            number = int(data)
            code = encode_integer(number)
            conn.send(str(code).encode())
