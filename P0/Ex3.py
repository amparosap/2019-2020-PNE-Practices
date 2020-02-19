from Seq0 import *

list_files = ["U5" , "ADA" , "FRAT1" , "FXN" , "RNU6_269P"]
FOLDER = "../Session-04/"

for file in list_files:
    sequence = seq_read_fasta(FOLDER + file + ".txt")
    print("Gene " , file , " ---> Length: ", seq_len(sequence))

