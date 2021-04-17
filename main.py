import pygame
from pygame.locals import *
import time
import random
import json

# -------- Game State -----------
# For dictionary
database = 'words_dictionary.json'
dictionary = json.loads(open(database).read())

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 128)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5 

# Holds the boggle letter distribution
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

# Pattern match  
r = 4
c = 4
  
# Function to check if a word exists 
# in the grid
def find_match(mat, pat, x, y, nrow, ncol, level) :
  
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
        res = (find_match(mat, pat, x - 1, y, nrow, ncol, level + 1) | 
               find_match(mat, pat, x + 1, y, nrow, ncol, level + 1) | 
               find_match(mat, pat, x, y - 1, nrow, ncol, level + 1) |
               find_match(mat, pat, x, y + 1, nrow, ncol, level + 1)) 
  
        # marking this cell as unvisited again 
        mat[x].replace(mat[x][y], temp)
        return res
      
    else :
        return False
  
# Function to check if the word exists in the grid or not 
def check_match(mat, pat, nrow, ncol) :
  
    l = len(pat)
  
    # if total characters in matrix is less then pattern length 
    if (l > nrow * ncol) :
        return False
  
    # Traverse in the grid 
    for i in range(nrow) :
        for j in range(ncol) :
  
            # If first letter matches, then recur and check 
            if (mat[i][j] == pat[0]) :
                if (find_match(mat, pat, i, j, 
                              nrow, ncol, 0)) :
                    return True
    return False


# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [640, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Input text Variables
text = 'Enter'
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, BLUE)

# Display the input text
rect = img.get_rect()
rect.topleft = (175, 20)

# store found words
found_words = []
found_font = pygame.font.SysFont(None, 48)

# turn the letter list into multidimensional array of pygame images
img_list = []
for row in range(4):
    img_list.append([])
    for column in range(4):
        cell_font = pygame.font.SysFont(None, 30)
        cell_img = cell_font.render(grid[row][column], True, BLUE)
        img_list[row].append(cell_img)

# Display the score
score_val = 0
score_str = str(score_val)
score_font = pygame.font.SysFont(None, 35)
score_img = score_font.render("Score: " + score_str, True, RED)

score_rect = img.get_rect()
score_rect.topleft = (175, 70)

# Set title of screen
pygame.display.set_caption("Fake Boggle")
 
# Loop until the user clicks the close button.
done = False

# Set variable indicating if input text is in the Trie to false
in_Grid = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # found words variables
    for word in found_words:
        found_img = font.render("Found:" + word, True, BLUE)
        found_rect = found_img.get_rect()
        found_rect.topleft = (175, 60)
        screen.blit(found_img, found_rect)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                # if (checkMatch(grid, text.lower(), r, c)) and text.lower() in dictionary and text.lower() not in found_words:
                if (check_match(str_grid, text.upper(), r, c)) and text.lower() not in found_words and text.lower() in dictionary:
                    found_words.append(text.lower())
                    print(found_words)
                    if 3 <= len(text) <= 4:
                        score_val += 1
                    elif len(text) == 5:
                        score_val += 2
                    elif len(text) == 6:
                        score_val += 3
                    elif len(text) == 7:
                        score_val += 5
                    elif len(text) >= 8:
                        score_val += 11
                    score_img = score_font.render("Score: " + str(score_val), True, RED)
                    score_rect.size = score_img.get_size()
            elif event.key == K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
            else:
                text += event.unicode
            img = font.render(text, True, BLUE)
            rect.size = img.get_size()
        
    # Set the screen background
    screen.fill(GRAY)
    
    # Display input text 
    screen.blit(img, rect)

    # Display score
    screen.blit(score_img, score_rect)



    # Draw the grid
    for row in range(4):
        for column in range(4): 
            for letter in img_list:
                color = WHITE
                rect2 = pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
                screen.blit(img_list[row][column], rect2)

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    in_Trie = False
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()