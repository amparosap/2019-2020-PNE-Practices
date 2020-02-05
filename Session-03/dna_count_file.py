with open ("dna", "r") as f:
    for line in f:
        for c in line:
            letterA = "A"
            letterc = "C"
            lettert = "T"
            letterG = "G"
print("Total length:", len(user_input))
print("A:", user_input.count(letterA))
print("C:", user_input.count(letterc))
print("T:", user_input.count(lettert))
print("G:", user_input(letterG))
