# Problem 51:
# By replacing the 1st digit of the 2-digit number *3, it turns out that six
# of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 
# 5-digit number is the first example having seven primes among the ten 
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family,
#  is the smallest prime with this property.
# 
# Find the smallest prime which, by replacing part of the number (not 
# necessarily adjacent digits) with the same digit, is part of an eight 
# prime value family.
#______________________________________________________________________________

import time
import string
 
start = time.time()

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        # filter out number 2 and 3
        return True 
    if n % 2 == 0 or n < 2:
        return False
    
    # only odd numbers
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True


def check_number(prime, n):
    result = []
    
    for digit in '0123456789':
        x = int(string.replace(prime, n, digit))
        
        
        
        
        
    for i in str(prime):
        for x in range(10):
            
            return result

run = 0

for i in range(1000000):
    run += 1
    if is_prime(i):
        if bool(check_number(i)):
            c = check_number(i)
            if len(c) == 8:
                print(i)
                break
    if i % 10 == 0:
        print('Durchlauf: ', run)



elapsed = (time.time() - start)
 
print "time: %s seconds" % elapsed


"""

l = []
k = 0

for i in range(10000000, 99999999, 1):
    if is_prime(i):
        l.append(i)
        print(i)
    if i / 1000 == 0:
        k += 1000
        print(k)

print(len[l])

"""
