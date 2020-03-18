from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq('')

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence", 1, ": (Length:",  s1.len(), ")",  s1)
print(f"Bases: {s1.countdic()}")
print("Sequence", 2, ": (Length:",  s2.len(), ")",  s2)
print(f"Bases: {s2.countdic()}")
print("Sequence", 3, ": (Length:",  s3.len(), ")",  s3)
print(f"Bases: {s3.countdic()}")
