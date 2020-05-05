from pathlib import Path

class Seq:
    """A class for representing sequence objects"""
    Error = "ERROR!"
    Null = "NULL!"
    def __init__(self, strbases = Null):

        if strbases == self.Null:
            self.strbases = self.Null
            print("Null Seq created")
            return

        if not self.valid_seq(strbases):
            self.strbases = self.Error
            print("Invalid Seq!")
            return

        self.strbases = strbases
        print("New Seq created!")

    def valid_seq(self, strbases):
        bases = ["A", "C", "G", "T"]
        for b in strbases:
            if b not in bases:
                return False
        return True

    def __str__(self):       # Everytime we want to print an object
        return self.strbases

    def len(self):
        if self.strbases == self.Error or self.strbases == self.Null:
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        res = {"A": self.count_base("A"), "C": self.count_base("C"),
               "G": self.count_base("G"), "T": self.count_base("T")}
        return res

    def reverse(self):
        if self.strbases == self.Error or self.strbases == self.Null:
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        dict_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
        res = ''
        if self.strbases == self.Error or self.strbases == self.Null:
            return self.strbases
        else:
            for b in self.strbases:
                res = res + dict_bases[b]
            return res

    def read_fasta(self, filename):
        file = Path(filename)
        file_contents = file.read_text()
        lines = file_contents.split('\n')
        self.strbases = "".join(lines[1:])
        return self