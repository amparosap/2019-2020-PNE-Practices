class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        if strbases== "":
            print("NULL Seq created!")
            self.strbases = "NULL"
        else:
            for e in strbases:
                if e not in ["A", "C", "T", "G"]:
                    print("INVALID seq")
                    self.strbases = "ERROR"
                    return
            print("New sequence created!")
            self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        for e in self.strbases:
            if e not in ["A", "C", "T", "G"]:
                return 0
        return len(self.strbases)
    """pass #there is nothing inside this class"""

    def count_bases(self, base):
        counter = 0
        if self.strbases == '':
            return 0
        else:
            for e in self.strbases:
                if e not in ["A", "C", "T", "G"]:
                    return 0
                else:
                    if e in base:
                        counter += 1
            return counter

    def count(self):
        bases = ["A", "C", "T", "G"]
        count_b = []
        for base in bases:
            count_b.append(self.count_bases(base))
        dictionary = dict(zip(bases, count_b))
        return dictionary

    def reverse(self):
        rev_seq = ''
        if self.strbases == 'NULL':
            return self.strbases
        else:
            for e in self.strbases[::-1]:
                if e not in ["A", "C", "T", "G"]:
                    rev_seq = 'ERROR'
                    return rev_seq

                else:
                    rev_seq += e
        return (rev_seq)

    def complement(self):
        comp_seq = ""
        if self.strbases == 'NULL':
            return self.strbases
        else:
            for x in self.strbases:
                if x not in ["A", "C", "T", "G"]:
                    comp_seq = 'ERROR'
                    return comp_seq
                else:
                    if x in "A":
                        comp_seq += "T"
                    if x in "T":
                        comp_seq += "A"
                    if x in "C":
                        comp_seq += "G"
                    if x in "G":
                        comp_seq += "C"
            return (comp_seq)

    def read_fasta(self, filename):
        file_lines = pathlib.Path(filename).read_text().split("\n")
        body = (file_lines[1:])
        self.strbases = ''.join(body)
        return (self)

class Gene(Seq):
    pass
#main program
s1= Seq("AACGTC")
g= Gene("CCGTCGA")

#print(f"sequence 1: {s1}")
#print(f"sequence 2: {g}")

l1= s1.len()
#print(f"the lenght of the sequence 1 is {l1}")
#print(f"the length of the sequence 2 is {g.len()}")