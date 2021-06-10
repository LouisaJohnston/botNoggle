import pygame
from pygame.locals import *
import time
import random
import json

# -------- Game State -----------
# For dictionary
database = 'words_dictionary.json'
dictionary = json.loads(open(database).read())

# dictionary Trie
class TrieNode:
    def __init__(self, char):
        # Character stored in this node
        self.char = char
        # A flag that marks if the word ends on this particular node.
        self.end_of_word = False
        # A dictionary of child nodes where the keys are the characters (letters) 
        # and values are the nodes
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")
    def insert (self, string):
        node = self.root
        # Check each character in the string
        # If none of the children of the current node contains the character, 
        # create a new child of the current node for storing the character.
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                # As the character is not found, create a new trie node
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # Mark the end of a word
        node.end_of_word = True

    def search (self, string):
        node = self.root
        # Check each character in the string
        # If none of the children of the node contains the character,
        # Return none
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                node = None
                break
        return node


t = Trie()

def make_trie():
    for string in dictionary.keys():
        t.insert(string)
 
make_trie()
# print(t.root.children)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 128)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each grid cell
MARGIN = 5 

# Holds the dice letter distribution
NOGGLE_STRING = [
	[
        'AAEEGN',
	    'ABBJOO',
	    'ACHOPS',
	    'AFFKPS'
    ], [
        'AOOTTW',
        'CIMOTU',
        'DEILRX',
        'DELRVY'
    ], [
        'DISTTY',
        'EEGHNW',
        'EEINSU',
        'EHRTVW'
    ], [
        'EIOSST',
        'ELRTTY',
        'HIMNU',
        'HLNNRZ',
    ]
]

# For building the grid
grid = []
for row in range(4):
    grid.append([])
    for column in range(4):
        random_char = random.choice(NOGGLE_STRING[row][column])
        grid[row].append(random_char)  # Append a cell
print(grid)

# For checking input text
str_grid = []
for row in grid:
    str_row = ''
    str_row += ''.join(row)
    str_grid.append(str_row)

# Set the row/column length  
r = 4
c = 4
  
# Function to find adjacent letters in the grid
def find_match(noggle_grid, input_text, x, y, nrow, ncol, level):
    l = len(input_text) 
    if level == l:
        return True
    # Check if out of grid boundary 
    if x < 0 or y < 0 or x >= nrow or y >= ncol:
        return False
    # Use recursion to find grid letter matches
    if noggle_grid[x][y] == input_text[level]:
        # Marking this cell as visited 
        temp = noggle_grid[x][y]
        noggle_grid[x].replace(noggle_grid[x][y], "#")
        # check neighboring letters in all eight directions
        res = (find_match(noggle_grid, input_text, x - 1, y, nrow, ncol, level + 1) | 
               find_match(noggle_grid, input_text, x + 1, y, nrow, ncol, level + 1) | 
               find_match(noggle_grid, input_text, x, y - 1, nrow, ncol, level + 1) |
               find_match(noggle_grid, input_text, x, y + 1, nrow, ncol, level + 1) |
               find_match(noggle_grid, input_text, x + 1, y + 1, nrow, ncol, level + 1) |
               find_match(noggle_grid, input_text, x - 1, y + 1, nrow, ncol, level + 1) |
               find_match(noggle_grid, input_text, x + 1, y - 1, nrow, ncol, level + 1) |
               find_match(noggle_grid, input_text, x - 1, y - 1, nrow, ncol, level + 1)) 
        # marking this cell as unvisited again 
        noggle_grid[x].replace(noggle_grid[x][y], temp)
        return res
    else:
        return False
  
# Function to check if word exists in the grid or not 
def check_match(noggle_grid, input_text, nrow, ncol):
    l = len(input_text)
    # if total characters in matrix is less than input text length 
    if l > nrow * ncol:
        return False
    # Traverse in the grid 
    for i in range(nrow):
        for j in range(ncol):
            # If first letter matches, then recur and check 
            if noggle_grid[i][j] == input_text[0]:
                if find_match(noggle_grid,input_text, i, j, nrow, ncol, 0):
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
found_font = pygame.font.SysFont(None, 30)

# Function to space out found words
def blit_text(surface, text, pos, font, color = pygame.Color('BLUE')):
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for word in found_words:
        found_img = found_font.render(word, True, BLUE)
        word_width, word_height = found_img.get_size()
        if x + word_width >= max_width:
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
        if x + word_height >= max_height:
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
        surface.blit(found_img, (x, y))
        x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

found_title_img = found_font.render("Found:", True, BLUE)
found_title_rect = found_title_img.get_rect()
found_title_rect.topleft = (175, 120)

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
pygame.display.set_caption("Bot Noggle")
 
# Loop until the user clicks the close button.
done = False

# Set variable indicating if input text is in the Trie to false
in_Trie = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Game Loop -----------
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                if t.search(text.lower()):
                    in_Trie = True
                if (check_match(str_grid, text.upper(), r, c)) and text.lower() not in found_words and in_Trie == True:
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
    
    # Display found words
    screen.blit(found_title_img, found_title_rect)
    blit_text(screen, found_words, (175, 150), found_font)

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

    # Limit to 60 frames/second
    clock.tick(60)
 
    # Update the screen with what we've drawn.
    pygame.display.update()
    in_Trie = False
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()