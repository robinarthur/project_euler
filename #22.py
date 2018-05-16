# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
#______________________________________________________________________________


#import nltk
#nltk.download()

from tokenize import tokenize

file = open("#22.txt", "r")

f = file.read()

text = str(f).replace('"', '').replace(', ',' ')

text = text.split(',')

print(text)

for i in text:
    print(i


"""
names.append(''.join(i.rstrip(',') for i in f))

text = str(names).replace('"', ' ').replace("'",'')

print(type(names))
print(names)
print(text)

w_l = tokenize(text)

print(w_l)

"""