# Fake Boggle

## User Stories
- As a user (AAU), I want to be able to search for words grid of random letters.
- AAU, I want to be able to enter these words into a text box, and if they exist in the dictionary, have the points corresponding to the length of the word added to my score and have my total score and previously entered words displayed.

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
- Calculate total possible points
- Multiple grid sizes 
- Option to display word definitions
- Some sort of a daily grid with a leader board
- Mobile-friendly
- Randomize letter directions
- Multi-player (Socket.io)


## Technologies
JavaScript, React, Express, and the WordsAPI. In addition, I would like to include Socket.io as a stretch goal.

