# Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#______________________________________________________________________________

def is_prime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True # filter out number 2 and 3
    if n % 2 == 0 or n < 2: return False
    
    for i in range(3, int(n**0.5)+1,2): # only odd numbers
        if n % i == 0: return False
    return True

i = number = 600851475143
l = []
k = 0

while l[-1] >= 0:
    i -= 1
    if is_prime(i):
        l.append(i)
        
        # check if the prime is a factor of number
        
        
    if i % 100000 == 0:
        k += 100000
        print('checked: ', k)
    
print("yuhuu")
print(l[-1])