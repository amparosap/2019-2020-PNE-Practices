from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file = Path(FILENAME).read_text()
f= file.split('\n')
cadena= ''.join(f[1::])

# -- Print the contents on the console
print("The body of the U5.txt file:", cadena)