# Problem 7:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?
#______________________________________________________________________________

def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    
    for i in range(3, int(n**0.5)+1,2): # only odd numbers
        if n % i == 0: return False
    return True

l = []
i = 0

while len(l) < 10001:
    i += 1
    if is_prime(i): l.append(i)

print(l[-1])