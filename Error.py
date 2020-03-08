fp = open("Text", "r")
number_words = ""
punt = [".", "!", "?", ","]

for liner in fp:
    for p in punt:
        liner = liner.replace(p, "")
    print(liner)
    total_words=len(liner)
    #print(total_words)
    Mylist= liner.split()
    freq = []
    for w in Mylist:
        freq.append(Mylist.count(w))
    print(freq)

for x in liner:
    if x not in freq:
        freq.append(x)
        fp.write(str(x))


# for word in texto:
# if word == " ":
# number_words = number_words + 1
# print("there are", number_words + 1, "words")