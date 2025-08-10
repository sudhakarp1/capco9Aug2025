string='''count the words
present in the string
adding extra count inside the string'''

counter = {}
for word in string.split():
    if word not in counter:
        counter.setdefault(word, 1)
    else:
        counter[word] += 1

print(counter)
