import socket
from pathlib import Path
import termcolor

ip = "127.0.0.1"
port = 8080

def get_resource(path):
    cod = 200

    if path == "/":
        res = Path("Index.html").read_text()

    elif path == "/info/A":
        res = Path("A.html").read_text()

    elif path == "/info/C":
        res = Path("C.html").read_text()

    elif path == "/info/G":
        res = Path("G.html").read_text()

    elif path == "/info/T":
        res = Path("T.html").read_text()

    else:
        res = Path("Error.html").read_text()
        cod = 404

    return res, cod

def process_client(client):
    rec_bytes = client.recv(2840)
    rec = rec_bytes.decode()

    print("MESSAGE FROM CLIENT: ")

    lines = rec.split("\n")
    request_line = lines[0]

    request = request_line.split(" ")
    method = request[0]
    path = request[1]

    print("Client request: ", end = "")
    termcolor.cprint(request_line, "green")
    print()

    print(f"Method: {method}")

    body = ""
    code = 0

    if method == "GET":
        print(f"Path: {path}")
        print()
        body, code = get_resource(path)

    if code == 200:
        status_str = "OK"
    else:
        status_str = "Not found"

    header = "Content-Type: text/html\n"
    header += f"Content length: {len(body)}\n"

    status_line = f"HTTP/1.1 {code} {status_str}\n"

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
        print()

        cs.close()