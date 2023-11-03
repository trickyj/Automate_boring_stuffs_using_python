# usinf forloop we can print every line with the counter.
# 'r' is for read

f = open('Exercise Files/inputFile.txt', 'r')
count = 0
for line in f:
    print(str(count) + line)
    count = count + 1
f.close()
