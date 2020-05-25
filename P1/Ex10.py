from Seq1 import Seq

bases = ["A", "C", "T", "G"]
list_of_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P" ]
txt = ".txt"
FOLDER = "../Session-04/"


for x in list_of_genes:
    s = Seq('')
    val = 0
    base = ''
    s = s.read_fasta(FOLDER+x+txt)
    dict1 = s.count()
    for a, b in dict1.items():
        while b > val:
            val = b
            base = a
    print("Gene ", x, " : Most frequent base: ", base)