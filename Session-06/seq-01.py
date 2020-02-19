class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases =strbases
        print("New sequence created ")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)
    """pass #there is nothing inside this class"""

class Gene(Seq):
    pass
#main program
s1= Seq("AACGTC")
g= Gene("CCGTCGA")

print(f"sequence 1: {s1}")
print(f"sequence 2: {g}")

l1= s1.len()
print(f"the lenght of the sequence 1 is {l1}")
print(f"the length of the sequence 2 is {g.len()}")