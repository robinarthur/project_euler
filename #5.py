#
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
#______________________________________________________________________________

div = [x for x in range(1,21)]

l = []

for i in range(20, 10000):
    for e in div:
        l.append(i % e == 0 )
    if all(item == True for item in l):
        print(l)
        print(i)