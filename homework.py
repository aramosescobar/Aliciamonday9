fp = open("Book1", "r")
fp2 = open ("Book2", "r")
list = []
fp_contents = fp.read()
punct =".", ",", ";", ":", "!", "?", "'"
line = ""
for p in fp_contents:
    if p not in punct:
        line=line + p
line = line.split()

for x in line:
    if x not in list:
        list.append(x)
        fp2.write(str(x)+"\n")

print(len(list))
