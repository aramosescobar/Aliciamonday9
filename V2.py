fp = open("Text", "r")
fp2 = open ("Book2", "r")
list= []
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
    print(freq)

    #for word in texto:
        #if word == " ":
            #number_words = number_words + 1
    #print("there are", number_words + 1, "words")


