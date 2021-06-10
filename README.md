# Bot Noggle

## User Stories
- As a user (AAU), I want to be able to search for words grid of random letters.
- AAU, I want to be able to enter these words into a text box, and if they exist in the dictionary, have the points corresponding to the length of the word added to my score and have my total score.

## Dependencies
Bot Noggle requires a code editor, Python, and Pyame. 

To install Pygame, run the following in your terminal:

```
python3 -m pip install -U pygame --user
```
To see if it works, run one of the included examples:
```
python3 -m pygame.examples.aliens
```

For more information on Pygame, visit https://www.pygame.org/wiki/GettingStarted



## Game Rules
Find as many words as possible within a 4x4 grid of random letters.

Words must be three letters or longer in length and in the adjacent tiles (across, down, forwards, backwards, and diagonally) of a 4x4 grid.

Word Length (in letters) | Points
-|-
3-4 | 1 pt.
5  | 2 pts.
6  | 3 pts.
7 | 5 pts.
8+ | 11 pts.


## Wireframe
![Game Layout](/images/wireframes/p4_wireframes.png)

## Technologies
Python, Pygame and words_dictionary.json from https://github.com/dwyl/english-words/

