from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
f = Path(FILENAME).read_text()

# -- Print the contents on the console
print("First line of the RNU6_269P.txt file:", next(f))