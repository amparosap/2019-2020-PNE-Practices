class Seq:

class Gene(Seq):
    pass


def generate_seqs(pattern, number):
    seq_lists = []
    bases = ''
    for e in range(1, number + 1):
        bases = e * pattern
        bases = Seq(bases)
        seq_lists.append(bases)
        bases = ''
    return (seq_lists)

print(generate_seqs("AC", 5))

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)