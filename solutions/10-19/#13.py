# Problem 13
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
# see #13.txt for the number
#______________________________________________________________________________

file = open("#13.txt", "r")

digits = [ line.rstrip() for line in file]
result = 0

for num in digits:
    result += int(num)

print(result)
print(str(result)[:10])
