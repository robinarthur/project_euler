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

# define the alphabet
alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# define reverse lookup dict
rdict = dict([ (x[1], x[0]) for x in enumerate(alfa) ])

# sum the word score
def char_score(word):
    score = 0
    for i in word:
        score += rdict[str(i)] + 1
    return score


file = open("#22.txt", "r")

f = file.read()

text = str(f).replace('"', '').replace(', ',' ')

text = text.split(',')
text = sorted(text)

result = []

for i in text:
    n_one = text.index(str(i)) + 1
    n_two = char_score(i)
    r = n_one * n_two
    result.append(r)

print(sum(result))