#
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#______________________________________________________________________________

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1,1000):
            if c*c == b*b + a*a and a < b < c and a + b + c == 1000:
                print("found")
                print("a: ", a)
                print("b: ", b)
                print("c: ", c)
                print("product: ", str(a*b*c))
                
