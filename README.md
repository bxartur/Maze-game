# Maze game
Project of maze game in Python, where player navigates from starting position to exit, through ramdomly generated maze, filled with guards and enemies.

## Content
1. Function that generates random maze as matrix (list of lists)
2. Function that returns shortest way from start to exit
3. Object classes made to present each element of maze (wall, solution path, guards, treasures, etc...)
4. Turtle library to show game in separate window
5. Game functions (e.g. to control player character using keyboard and make interactions with objects in maze)
6. Many minor functions and lines of code to improve project

## Example
![maze-example](https://user-images.githubusercontent.com/123515299/215509446-85b5bdd6-9ede-4a51-a06f-03429e660ef3.png)

Game has 4 difficulty levels (easy, medium, hard, extreme), that change size of the maze, number of guards and number of treasures - maze shown above has difficulty level set on medium. Level easy has in addition solution path from start to exit, that is displayed on floor.

Worth mentioning is fact, that maze shown above is, thanks to randomness, one of many possibilities, that can be received and every test of program give different maze.

## Controls
W - Up, A - Left, S - Down, D - Right
