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

number = 600851475143
l = []
k, i = 0, 0

while number > 1:
    i += 1
    if is_prime(i):
        if number % i == 0:
            l.append(i)
            number = number / i
            print("number", number)
                
    if i % 10 == 0:
        k += 10
        print('checked: ', k)
        
print(l[-1])