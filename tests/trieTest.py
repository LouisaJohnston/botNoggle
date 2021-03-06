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

# Grid Trie
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
    def insert (self, list):
        node = self.root
        # Check each character in the list
        # If none of the children of the current node contains the character, 
        # create a new child of the current node for storing the character.
        for char in list:
            if char in node.children:
                node = node.children[char]
            else:
                # As the character is not found, create a new trie node
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        for char in node.children:
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

# get all possible across lists
across_lists = []
reverse_across = []
# full across
for row in range(4):
    column_list = []
    reverse_col = []
    for column in range(4):
        column_list.append(grid[row][column])
        reverse_col = column_list[::-1]
    across_lists.append(column_list)
    reverse_across.append(reverse_col)
# across from idx 1
for row in range(4):
    column_list = []
    for column in range(1, 4):
        column_list.append(grid[row][column])
    across_lists.append(column_list)
# across from idx 2
for row in range(4):
    column_list = []
    for column in range(2, 4):
        column_list.append(grid[row][column])
    across_lists.append(column_list)
# reverse from idx 1
for row in range(4):
    column_list = []
    for column in reversed(range(3)):
        column_list.append(grid[row][column])
    reverse_across.append(column_list)
# reverse from idx 2
for row in range(4):
    column_list = []
    for column in reversed(range(2)):
        column_list.append(grid[row][column])
    reverse_across.append(column_list)

print(f'across \n {across_lists}')
print(f'reverse across \n {reverse_across}')
# get all possible down lists
down_lists = []
reverse_down = []
# full down 
for row in range(4):
    column_list = []
    reverse_col = []
    for column in range(4):
        column_list.append(grid[column][row])
        reverse_col = column_list[::-1]
    down_lists.append(column_list)
    reverse_down.append(reverse_col)
# down from idx 1
for row in range(4):
    column_list = []
    for column in range(1, 4):
        column_list.append(grid[column][row])
    down_lists.append(column_list)
# down from idx 2
for row in range(4):
    column_list = []
    for column in range(2, 4):
        column_list.append(grid[column][row])
    down_lists.append(column_list)
# reverse from idx 1
for row in range(4):
    column_list = []
    for column in reversed(range(3)):
        column_list.append(grid[column][row])
    reverse_down.append(column_list)
# reverse from idx 2
for row in range(4):
    column_list = []
    for column in reversed(range(2)):
        column_list.append(grid[column][row])
    reverse_down.append(column_list)

print(f'down \n {across_lists}')
print(f'reverse down \n {reverse_down}')

## # ## ## # get all possible forwards diagonal lists # ## # ## # ## # ##
f_diag_lists = []
# middle diagonal
f1 = []
r_f1 = []
for i in range(4):
    letter_list = []
    letter_list.append(grid[i][i])
    for j in letter_list:
        f1 += j
    r_f1 = f1[::-1]

# other diagonals
f2 = []
r_f2 = []
for i in range(3):
    letter_list = []
    letter_list.append(grid[i + 1][i])
    for j in letter_list:
        f2 += j
    r_f2 = f2[::-1]
f3 = []
r_f3 = []
for i in range(2):
    letter_list = []
    letter_list.append(grid[i + 2][i])
    for j in letter_list:
        f3 += j
    r_f3 = f3[::-1]
f4 = []
r_f4 = []
for i in range(3):
    letter_list = []
    letter_list.append(grid[i][i + 1])
    for j in letter_list:
        f4 += j
    r_f4 = f4[::-1]
f5 = []
r_f5 = []
for i in range(2):
    letter_list = []
    letter_list.append(grid[i][i + 2])
    for j in letter_list:
        f5 += j
    r_f5 = f5[::-1]
# for middle-grid diagonals
f6 = []
for i in range(1, 4):
    letter_list = []
    letter_list.append(grid[i][i])
    for j in letter_list:
        f6 += j
f7 = []
for i in range(2, 4):
    letter_list = []
    letter_list.append(grid[i][i])
    for j in letter_list:
        f7 += j
f8 = []
for i in reversed(range(3)):
    letter_list = []
    letter_list.append(grid[i][i])
    for j in letter_list:
        f8 += j
f9 = []
for i in reversed(range(2)):
    letter_list = []
    letter_list.append(grid[i][i])
    for j in letter_list:
        f9 += j
f10 = []
for i in range(1, 3):
    letter_list = []
    letter_list.append(grid[i + 1][i])
    for j in letter_list:
        f10 += j
f11 = []
for i in reversed(range(2)):
    letter_list = []
    letter_list.append(grid[i + 1][i])
    for j in letter_list:
        f11 += j
f12 = []
for i in range(1, 3):
    letter_list = []
    letter_list.append(grid[i][i + 1])
    for j in letter_list:
        f12 += j
f13 = []
for i in reversed(range(2)):
    letter_list = []
    letter_list.append(grid[i][i + 1])
    for j in letter_list:
        f13 += j

f_diag_lists.extend((f1, r_f1, f2, r_f2, f3, r_f3, f4, r_f4, f5, r_f5, 
f6, f7, f8, f9, f10, f11, f12, f13))

## # ## ## # get all possible backwards diagonal lists # ## # ## # ## # ##

b_diag_lists = []
# middle diagonal
b1 = []
r_b1 = []
for i in range(4):
    letter_list = []
    letter_list.append(grid[i][-i - 1])
    for j in letter_list:
        b1 += j
    r_b1 = b1[::-1]
# other diagonals
b2 = []
r_b2 = []
for i in range(3):
    letter_list = []
    letter_list.append(grid[i][-i - 2])
    for j in letter_list:
        b2 += j
    r_b2 = b2[::-1]
b3 = []
r_b3 = []
for i in range(2):
    letter_list = []
    letter_list.append(grid[i][-i - 3])
    for j in letter_list:
        b3 += j
    r_b3 = b3[::-1]
b4 = []
r_b4 = []
for i in range(3):
    letter_list = []
    letter_list.append(grid[i + 1][-i - 1])
    for j in letter_list:
        b4 += j
    r_b4 = b4[::-1]

b5 = []
r_b5 = []
for i in range(2):
    letter_list = []
    letter_list.append(grid[i + 2][-i - 1])
    for j in letter_list:
        b5 += j
    r_b5 = b5[::-1]
# for middle-grid diagonals
b6 = []
for i in range(1, 4):
    letter_list = []
    letter_list.append(grid[i][-i - 1])
    for j in letter_list:
        b6 += j
b7 = []
for i in range(2, 4):
    letter_list = []
    letter_list.append(grid[i][-i - 1])
    for j in letter_list:
        b7 += j
b8 = []
for i in reversed(range(3)):
    letter_list = []
    letter_list.append(grid[i][-i - 1])
    for j in letter_list:
        b8 += j
b9 = []
for i in reversed(range(2)):
    letter_list = []
    letter_list.append(grid[i][-i - 1])
    for j in letter_list:
        b9 += j
b10 = []
for i in range(1, 3):
    letter_list = []
    letter_list.append(grid[i][-i - 2])
    for j in letter_list:
        b10 += j
b11 = []
for i in reversed(range(2)):
    letter_list = []
    letter_list.append(grid[i][-i - 2])
    for j in letter_list:
        b11 += j
b12 = []
for i in range(1, 3):
    letter_list = []
    letter_list.append(grid[i + 1][-i - 1])
    for j in letter_list:
        b12 += j
b13 = []
for i in reversed(range(2)):
    letter_list = []
    letter_list.append(grid[i + 1][-i - 1])
    for j in letter_list:
        b13 += j

b_diag_lists.extend((b1, r_b1, b2, r_b2, b3, r_b3, b4, r_b4, b5, r_b5,
b6, b7, b8, b9, b10, b11, b12, b13))

print(f'diagonal \n {f_diag_lists}')
print(f'reverse diagonal \n {b_diag_lists}')

def make_trie():
    ## # Forwards # ##
    # for across
    for list in across_lists:
        t.insert(list)
    # for down
    for list in down_lists:
        t.insert(list)
    # for diagonal
    for list in f_diag_lists:
        t.insert(list)
    ## # Backwards # ##    
    # for across
    for list in reverse_across:
        t.insert(list)
    # for down
    for list in reverse_down:
        t.insert(list)
    # for diagonal
    for list in b_diag_lists:
        t.insert(list)
 
make_trie()
# print(t.root.children)

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [640, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Input text Variables
text = 'Enter'
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, BLUE)

# Display the input text
rect = img.get_rect()
rect.topleft = (175, 20)

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
in_Trie = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                if t.search(text.upper()):
                    in_Trie = True
                if in_Trie == True:
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
    in_Trie = False
    pygame.display.update()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()