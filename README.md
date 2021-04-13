# Fake Boggle

## User Stories
- As a user (AAU), I want to be able to search for words grid of random letters.
- AAU, I want to be able to enter these words into a text box, and if they exist in the dictionary, have the points corresponding to the length of the word added to my score and have my total score.

### Game Rules
Find as many words as possible within a 4x4 grid of random letters in three minutes.

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


## Stretch
- Display previously found words
- Calculate total possible points
- Multiple grid sizes 
- Option to display word definitions
- Some sort of a daily grid with a leader board
- Mobile-friendly
- Randomize letter directions


## Technologies
Python, Pygame and words_dictionary.json from https://github.com/dwyl/english-words/

