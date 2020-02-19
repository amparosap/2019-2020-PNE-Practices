from Seq0 import *

print("-----| Exercise 6 |------")

FOLDER = "../Session-04/"
filename = "U5.txt"
length_bases = 20
sequence = seq_read_fasta(FOLDER + filename)

print("Gene " , filename)
print("Fragment:" , (sequence)[:length_bases])
print("Reverse:" , seq_reverse(sequence[:length_bases]))