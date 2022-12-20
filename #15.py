#!"C:\Users\BK048728\AppData\Local\Programs\Python\Python310\python.exe"
#####################################################################################
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
#How many such routes are there through a 20×20 grid?
#####################################################################################

# create a two-dimensional array to store the number of paths to each cell in the grid
paths = [[0 for j in range(21)] for i in range(21)]

# initialize the values in the first row and first column to be 1
for i in range(21):
    paths[i][0] = 1
for j in range(21):
    paths[0][j] = 1

# iterate through the rest of the cells in the grid and calculate the number of paths to each cell
for i in range(1, 21):
    for j in range(1, 21):
        # the number of paths to the current cell is the sum of the number of paths to the cell above and the number of paths to the cell to the left
        paths[i][j] = paths[i-1][j] + paths[i][j-1]

# the number of paths to the bottom right corner is stored in paths[20][20]
print(paths[20][20])
