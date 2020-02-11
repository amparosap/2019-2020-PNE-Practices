from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
file = Path(FILENAME).read_text()
f= file.split('\n')

# -- Print the contents on the console
print("First line of the RNU6_269P.txt file:", f[0])