# Problem #63:
# 
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
# number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?
#______________________________________________________________________________

import math

#def is_power(number):
#    l = len(number)
#    if isinstance(ln(number) / ln(l), int):
#        return True

x = [x for x in range(10,999999) if (math.log(x) / math.log(len(str(x)))) % 1 == 0]
print(x)

    
#  print(math.exp(exponent*math.log(base))) 
# isinstance(4, int)





# 16807 = x^5  5=len

# ln(16807) = x * ln(len)

# ln(16807 / ln(len) = x

# if isistance(x, int) return 