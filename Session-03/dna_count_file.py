with open ("dna", "r") as f:
    for line in f:
        for c in line:
            letterA = "A"
            letterc = "C"
            lettert = "T"
            letterG = "G"
print("A:", f.count(letterA))
print("C:", f.count(letterc))
print("T:", f.count(lettert))
print("G:", f.count(letterG))
