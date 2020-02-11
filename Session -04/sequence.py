from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file = Path(FILENAME).read_text()
f= file.split('\n')
cadena= ''.join(f[1::])
letterA= "A"
letterc= "C"
lettert= "T"
letterG= "G"
print("A:", cadena.count(letterA))
print("C:", cadena.count(letterc))
print("T:", cadena.count(lettert))
print("G:", cadena.count(letterG))
print(len(cadena))