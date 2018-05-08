#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#______________________________________________________________________________

def is_pal(n):
    return str(n) == str(n)[::-1]

print('{}'.format(max([i*j for i in range(999, 0, -1) for j in range(999, 0, -1) if is_pal(i*j)
                                              ])  # generator, max
                                              )  # format
                                              )  # print