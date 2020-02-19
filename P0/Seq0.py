import pathlib
#imporatnte poner lo de arriba

#ex1
def seq_ping():
    print("okey")

#ex2
def seq_read_fasta(filename):
    # -- Open and read the file
    cuerpo = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(cuerpo)
    return body

#ex3
def seq_len(seq):
    return len(seq)

#ex4
def seq_count_base(seq, base):
    return seq.count(base)

#ex5
def  seq_count(seq):
    bases = ["A", "C", "T", "G"]
    n_bases = []
    for base in bases:
        n_bases.append(seq_count_base(seq, base))
    dictionary = dict(zip(bases, n_bases))
    return dictionary

#ex6
def seq_reverse(seq):
    return seq[::-1]