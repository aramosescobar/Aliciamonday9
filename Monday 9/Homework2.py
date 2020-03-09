import dictionary

print(dictionary.d)

text ="my cat loves swim in the swimmingpool in summer every day"
translate = ""
words= text.split()
for w in words:
    translate = translate + " " + dictionary.d[w]

print(translate)