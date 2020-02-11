from pathlib import Path

FILENAME = "RNU6_269P.txt"

# -- Open and read the file
with open(FILENAME, "r") as f:
    header = next(f).replace('"', "").strip("\n").split(',')

print ("First line of the RNU6_269P.txt file:", header)

