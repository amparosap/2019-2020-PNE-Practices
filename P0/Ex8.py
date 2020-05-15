from seq0 import *

print("------Exercise 8--------")
folder ="../session-04/.."
bases=["A","C","T","G"]
files_list=["U5","ADA","FRAT1","FXN","RNU6_269P"]
txt = ".txt"

for line in files_list:
    val = 0
    base = ''
    for i, t in seq_count(seq_read_fasta(FOLDER + e + txt)).items():
        while t > val:
            val = t
            base = i
    print("Gene ", e, " : Most frequent base: ", base)

