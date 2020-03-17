class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        for el in strbases:
            if el not in ["A", "C", "T", "G"]:
                print ("ERROR: Invalid seq detected")
                self.strbases= "ERROR"
                return

        print("New sequence created ")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)
    pass

class Gene(Seq):
    pass
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
#mainmenu
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")