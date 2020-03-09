punctuation2 = ",.;:!?\"'()[]{}-*<>"

def common_words(Book1):
    fd = open(Book1, "r") #opening the file for reading
    d = {} #define a new dictionary
    for line in fd: #edit line by line from now on do this for every line in the text

        for c in punctuation2: #for each caratcter in this puctuenion each line is what each line was before but without the punctuation
            line = line.replace(c, " ")
        words = line.split() #once I have de line I am splitting to recognize each word beacuse space divide words
        #words is a list of individual words. word[["I", "can", "see"....]
        for word in words:
            #words = ["I", then "can", then "see"...
            if word in d:
                d[word] += 1 #each individual word appears. the value is what is was begore plus 1, the walue will be 2. That is how we count the number of words.
            else:
                d[word] = 1 #por cada palabra que encuentre en el texto corregido que no esté en el diccionario definiido cuentame +1.
    values = list(d.values()) #
    values.sort(reverse=True)
    common = []
    for numbers in values[:10]: #el número de palabras que se repite más de 10 veces. El programa ya sabe que son las Keys y values. las Keys son las palabras
        #y el número se lo he asignado cuando he contado el número de veces que aparece.
        for keys in d:
            if d[keys] == numbers:
                common.append((keys, numbers))
    print("the most common words are:")
    for i in common:
        print(i[0], i[1], "times")

common_words("../Book1")