"""
Module with implementation of elements in maze as class objects
"""


from turtle import Turtle, ontimer
from math import sqrt
from random import randint, choice
from content.modules.graphic_functions import load_graphics
load_graphics()

class Wall(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("wall.gif")
        self.penup()
        self.speed(0)
        self.unpassable_position = []


class SolutionPath(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("path.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("hero_right.gif")
        self.penup()
        self.speed(0)
        self.score = 0
        self.unpassable_position = []

    def moveUp(self):
        new_position = (self.xcor(), self.ycor() + 24)
        if (new_position not in self.unpassable_position):
            self.shape("hero_up.gif")
            self.goto(new_position)

    def moveDown(self):
        new_position = (self.xcor(), self.ycor() - 24)
        if (new_position not in self.unpassable_position):
            self.shape("hero_down.gif")
            self.goto(new_position)

    def moveLeft(self):
        new_position = (self.xcor() - 24, self.ycor())
        if (new_position not in self.unpassable_position):
            self.shape("hero_left.gif")
            self.goto(new_position)

    def moveRight(self):
        new_position = (self.xcor() + 24, self.ycor())
        if (new_position not in self.unpassable_position):
            self.shape("hero_right.gif")
            self.goto(new_position)

    def collides(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()

        if (sqrt((a**2) + (b**2)) < 24):
            return True
        else: 
            return False


class TreasureChest(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("treasure_chest.gif")
        self.penup()
        self.speed(0)
        self.award = 100
        self.goto(x, y)


class LevelExit(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("exit.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class RandomWalkingGuard(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("guard_right.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.unpassable_position = []
        self.direction = choice(['up', 'down', 'left', 'right'])
        self.player_pos = 0

    def move(self):
        if self.player_detection(self.player_pos):
            if self.player_pos.ycor() > self.ycor():
                self.direction = 'up'
            elif self.player_pos.ycor() < self.ycor():
                self.direction = 'down'
            elif self.player_pos.xcor() < self.xcor():
                self.direction = 'left'
            elif self.player_pos.xcor() > self.xcor():
                self.direction = 'right'

        if self.direction == 'up':
            self.shape("guard_up.gif")
            new_position = (self.xcor(), self.ycor() + 24)
        elif self.direction == 'down':
            self.shape("guard_right.gif")
            new_position = (self.xcor(), self.ycor() - 24)
        elif self.direction == 'left':
            self.shape("guard_left.gif")
            new_position = (self.xcor() - 24, self.ycor())
        elif self.direction == 'right':
            self.shape("guard_right.gif")
            new_position = (self.xcor() + 24, self.ycor())
        else:
            new_position = (self.xcor(), self.ycor())
        
        if (new_position not in self.unpassable_position):
            self.goto(new_position)
        else:
            self.direction = choice(['up', 'down', 'left', 'right'])
        
        ontimer(self.move, t=randint(200,500))

    # t/f flag if guard detects player
    def player_detection(self, player):
        a = self.xcor() - player.xcor()
        b = self.ycor() - player.ycor()

        if (sqrt((a**2) + (b**2)) <= 72):
            return True
        else: 
            return False
    



