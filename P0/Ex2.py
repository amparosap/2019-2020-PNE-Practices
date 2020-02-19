
from Seq0 import *
folder= "../Session-04/"
filename= "U5.txt"
n_bases = 20
print("DNA file: ", filename)
print("The first ", n_bases, "bases are:")
print( seq_read_fasta(folder + filename)[:n_bases])
