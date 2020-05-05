import socket
from pathlib import Path
import termcolor

ip = "127.0.0.1"
port = 8080

def get_resource(path):
    res = ""

    if path == "/info/A":
        res = Path("A.html").read_text()

    return res

def process_client(client):
    rec_bytes = client.recv(2840) #numero de bites q puede tener el mensaje
    rec = rec_bytes.decode()

    print("MESSAGE FROM CLIENT: ")

    lines = rec.split("\n")
    request_line = lines[0]

    request = request_line.split(" ")
    method = request[0]
    path = request[1]

    print("Client request: ", end = "")
    termcolor.cprint(request_line, "green")

    print(f"Method: {method}")
    print(f"Path: {path}")

    body = ""

    if method == "GET":
        body = get_resource(path)

    header = "Content-Type: text/html\n"
    header += f"Content length: {len(body)}\n"

    status_line = "HTTP/1.1 200 OK\n"

    msg = status_line + header + "\n" + body

    cs.send(msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((ip, port))

ls.listen()

print("Server configurated!")

while True:
    print("Waiting for clients...")

    try:
        (cs, cs_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server interrupted by user!")

        ls.close()
        exit()

    else:
        process_client(cs)

        cs.close()