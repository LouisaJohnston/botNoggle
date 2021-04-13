import pygame
from pygame.locals import *
import time
import random
import string

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# This sets the WIDTH and HEIGHT of each grid location
# w = 20
# x,y = 0,0
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5 


# For letters in cells
# cell_font = pygame.font.SysFont(None, 20)
# cell_img = cell_font.render(random_letter, True, RED)
# cell_rect =cell_img.get_rect()

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.

grid = []
for row in range(4):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(4):
        random_letter = random.choice(string.ascii_letters).upper()
        grid[row].append(random_letter)  # Append a cell

# for i in grid:
#     print(i[0], i[1], i[2], i[3])
letter_list = []
for letter in grid:
    letter_list+= letter
print(letter_list)
print(letter_list[-1])

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [640, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Text Variables
text = 'this text is editable'
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, RED)

# turn the letter list into pygame images
img_list = []
for letter in letter_list:
    cell_font = pygame.font.SysFont(None, 30)
    cell_img = cell_font.render(letter, True, RED)
    img_list.append(cell_img)

rect = img.get_rect()
rect.topleft = (175, 20)

# Set title of screen
pygame.display.set_caption("Fake Boggle")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]
            else:
                text += event.unicode
            img = font.render(text, True, RED)
            rect.size=img.get_size()

    # Set the screen background
    screen.fill(GRAY)
    screen.blit(img, rect)

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
                screen.blit(letter, rect2)
                if img_list.index(letter) != -1:
                    letter = img_list[+ 1]
             

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()