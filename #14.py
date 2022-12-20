#!"C:\Users\BK048728\AppData\Local\Programs\Python\Python310\python.exe"
#####################################################################################
#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?##
#
#NOTE: Once the chain starts the terms are allowed to go above one million.
#
##############################################################################################

def collatz_sequence_length(n):
    # initialize the length to 1, since the starting number is included in the sequence
    length = 1
    # keep generating numbers in the sequence until you reach 1
    while n != 1:
        # if the number is even, divide it by 2
        if n % 2 == 0:
            n = n // 2
        # if the number is odd, multiply it by 3 and add 1
        else:
            n = 3 * n + 1
        # increment the length by 1 for each number in the sequence
        length += 1
    # return the length of the sequence
    return length

# initialize the maximum length and starting number to be the minimum possible values
max_length = 0
max_starting_number = 0

# iterate through all the starting numbers from 1 to one million
for starting_number in range(1, 1000000):
    # calculate the length of the Collatz sequence for the current starting number
    length = collatz_sequence_length(starting_number)
    # update the maximum length and starting number if the current length is greater
    if length > max_length:
        max_length = length
        max_starting_number = starting_number

# the starting number that produces the longest Collatz sequence is stored in the max_starting_number variable
print(max_starting_number)
