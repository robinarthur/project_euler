# Problem 8
# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 × 9 × 8 × 9 = 5832.
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit number that have the 
# greatest product. What is the value of this product?
#______________________________________________________________________________


file = open("#8.txt", "r")

digit = file.read()
"""
digit = map(int, ''.join(line.rstrip() for line in file))

print(len(digit))
print(digit)
"""


l = []
result = []

#for i in range(len(digit)-13+1):
#    l.append(digit[i:i+13])

for i in digit:
    for j in list(i):
        l.append(j)

prod = 0
print(l)

for k in range(len(l)-12):
    p = int(l[k])*int(l[k+1])*int(l[k+2])*int(l[k+3])*int(l[k+4])*int(l[k+5])*int(l[k+6])*int(l[k+7])*int(l[k+8])*int(l[k+9])*int(l[k+10])*int(l[k+11])*int(l[k+12])
    if p > prod:
        prod = p
print(prod)


"""
numbers = []

for n in l:
    digits = []
    for d in n:
        digits.append(d)
    numbers.append(digits)
    
print(numbers)
print(digits)


for number in l:
    product = []
    k = 1
    for digit in number:
        if digit.isdigit() and int(digit) > 0:
            k *= int(digit)
    
        product.append(k)
    result.append(product)

y = []

for x in result:
    y.append(x[-1])

print(y)

print(max(y))
print(sort(y))
print("hier: 31109847552")

m = max(result)
print(m[-1])

"""