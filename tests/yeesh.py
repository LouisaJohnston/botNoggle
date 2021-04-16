import random

BOGGLE_STRING = "AAEEGNELRTTYAOOTTWABBJOOEHRTVWCIMOTUDISTTYEIOSSTDELRVYACHOPSHIMNEEINSUEEGHNWAFFKPSHLNNRZDEILRX"

# Create a 2 dimensional array
grid = []
for row in range(4):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(4):
        random_char = random.choice(BOGGLE_STRING)
        grid[row].append(random_char)  # Append a cell
print(grid)

str_grid = []
for row in grid:
    str_row = ''
    str_row += ''.join(row)
    str_grid.append(str_row)
print(str_grid)

# Pattern match  
r = 4
c = 4
  
# Function to check if a word exists 
# in a grid starting from the first 
# match in the grid level: index till  
# which pattern is matched x, y: current 
# position in 2D array 
def findmatch(mat, pat, x, y, 
              nrow, ncol, level) :
  
    l = len(pat) 
  
    # Pattern matched 
    if (level == l) :
        return True
  
    # Out of Boundary 
    if (x < 0 or y < 0 or 
        x >= nrow or y >= ncol) :
        return False
  
    # If grid matches with a letter 
    # while recursion 
    if (mat[x][y] == pat[level]) :
  
        # Marking this cell as visited 
        temp = mat[x][y]
        mat[x].replace(mat[x][y], "#")
  
        # finding subpattern in 4 directions 
        res = (findmatch(mat, pat, x - 1, y, nrow, ncol, level + 1) | 
               findmatch(mat, pat, x + 1, y, nrow, ncol, level + 1) | 
               findmatch(mat, pat, x, y - 1, nrow, ncol, level + 1) |
               findmatch(mat, pat, x, y + 1, nrow, ncol, level + 1)) 
  
        # marking this cell as unvisited again 
        mat[x].replace(mat[x][y], temp)
        return res
      
    else : # Not matching then false 
        return False
  
# Function to check if the word
# exists in the grid or not 
def checkMatch(mat, pat, nrow, ncol) :
  
    l = len(pat)
  
    # if total characters in matrix is 
    # less then pattern length 
    if (l > nrow * ncol) :
        return False
  
    # Traverse in the grid 
    for i in range(nrow) :
        for j in range(ncol) :
  
            # If first letter matches, then 
            # recur and check 
            if (mat[i][j] == pat[0]) :
                if (findmatch(mat, pat, i, j, 
                              nrow, ncol, 0)) :
                    return True
    return False

value = input('Please enter a string \n')

# grid = ["axmy", "bgdf", 
#         "xeet", "raks"]

# Function to check if word 
# exists or not 
if (checkMatch(str_grid, value, r, c)) :
    print("Yes")
else :
    print("No") 