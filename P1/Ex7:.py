from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq('')

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")


print("Sequence", 1, ": (Length:",  s1.len(), ")",  s1)
print(f"Bases: {s1.count()}")
print(f"Rev: {s1.reverse()}")
print("Sequence", 2, ": (Length:",  s2.len(), ")",  s2)
print(f"Bases: {s2.count()}")
print(f"Rev: {s2.reverse()}")
print("Sequence", 3, ": (Length:",  s3.len(), ")",  s3)
print(f"Bases: {s3.count()}")
print(f"Rev: {s3.reverse()}")