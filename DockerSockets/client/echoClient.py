import socket
import os

try:
    HOST = os.environ.get("SERVER_IP")  # The server's hostname or IP address
    PORT =  int(os.environ.get("SERVER_PORT"))  # The port used by the server
except:
    print("No .env found, using default variables.")
    HOST = "localhost"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print(HOST, PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")