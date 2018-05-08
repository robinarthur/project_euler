# Problem 10:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#______________________________________________________________________________

def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    
    for i in range(3, int(n**0.5)+1,2): # only odd numbers
        if n % i == 0: return False
    return True

l = []

for i in range(2000001):
    if is_prime(i): l.append(i)

print(sum(l))
    