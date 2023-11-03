# how to write to files.

# parameter r is to read
# and pararameter w is to write

f = open('Exercise Files/inputFile.txt', 'r')
passFile = open('passFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
f.close()
passFile.close()

