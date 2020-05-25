from Seq1 import Seq

FOLDER = "../Session-04/"
file_name = FOLDER + "U5.txt"
s = Seq('')
s = s.read_fasta(file_name)

print(f"Sequence : (Length: {s.len()}) {s}")
print(f"Bases: {s.count()}")
print(f"Rev: {s.reverse()}")
print(f"Comp: {s.complement()}")