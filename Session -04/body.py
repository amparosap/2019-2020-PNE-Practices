from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
f = Path(FILENAME).read_text()

# -- Print the contents on the console
print("First line of the U5.txt file:", (f))