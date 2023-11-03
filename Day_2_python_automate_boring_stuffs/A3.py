# usinf forloop we can print every line with the counter.
# 'r' is for read

f = open('Exercise Files/inputFile.txt', 'r', encoding='utf=8')
for line in f:
    line_split = line.split()
    if len(line_split) > 2:
        if line_split[2] == 'P':
            print(line)
    else:
        print(f"Line  '{line}' does not contain at least 3 words.")
f.close()
