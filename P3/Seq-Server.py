import socket
import termcolor
from Seq1 import Seq

list_seq = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]

def info_seq(arg):
    seq = Seq(arg)

    length = seq.len()

    count_a = seq.count_base("A")
    a_percent = (count_a * 100) / length

    count_c = seq.count_base("C")
    c_percent = (count_c * 100) / length

    count_g = seq.count_base("G")
    g_percent = (count_g * 100) / length

    count_t = seq.count_base("T")
    t_percent = (count_t * 100) / length

    res = f"""Sequence: {seq} \n
Total length: {length} \n
A: {round(count_a, 2)} ({a_percent}) \n
C: {round(count_c, 2)} ({c_percent}) \n
G: {round(count_g, 2)} ({g_percent}) \n
T: {round(count_t, 2)} ({t_percent})"""

    return res

ip = "192.168.1.39"
port = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((ip, port))

ls.listen()

print("Seq server configurated!")

while True:
    print()
    print("Waiting for clients...")

    try:
        (cs, cs_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server interrupted by user")

        ls.close()
        exit()

    else:

        msg = cs.recv(2840).decode()

        lines = msg.split("\n")
        line0 = lines[0].strip()

        lines_command = line0.split(" ") # So it divides the line0 into command and argument

        command = lines_command[0]

        try:
            argument = lines_command[1]

        except IndexError:
            argument = ""

        else:

            if command == "PING":
                termcolor.cprint("PING command!", "green")
                response = "OK!" + "\n"

            elif command == "GET":
                termcolor.cprint("GET command!", "green")

                response = list_seq[int(argument)] + "\n"
                print(response)

            elif command == "INFO":
                termcolor.cprint("INFO command!", "green")

                response = info_seq(argument) + "\n"
                print(response)

            elif command == "COMP":
                termcolor.cprint("COMP command!", "green")

                seq = Seq(argument)

                response = seq.complement() + "\n"
                print(response)

            elif command == "REV":
                termcolor.cprint("REV command!", "green")

                seq = Seq(argument)

                response = seq.reverse() + "\n"
                print(response)

            elif command == "GENE":
                termcolor.cprint("GENE command!", "green")

                filename = "../Session 04/" + argument + ".txt"

                seq = Seq().read_fasta(filename)
                response = str(seq)
                print(response)

        response_bytes = response.encode()

        cs.send(response_bytes)

        cs.close()