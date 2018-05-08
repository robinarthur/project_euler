#
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
#______________________________________________________________________________

div = [x for x in range(1,21)]

start = 100000000
step = 10000
k, j = start, 0
stop = 1000000000000

for i in range(start, stop):
    l = []
    for e in div:
        l.append(i % e == 0 )
    j += 1
    if j % step == 0:
        k += step
        print('checked :', k)
    if all(item == True for item in l):
        print(l)
        print(i)