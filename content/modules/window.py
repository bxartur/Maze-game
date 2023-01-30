"""
Module that initialises game window with following instructions
"""

from turtle import Screen

def game_window(level_size):

    window = Screen()
    window.bgcolor("black")              # set background color
    window.title("Maze game")            # set window title

    width = (level_size[1] * 24) + 50    # set window width (x coordinate)
    height = (level_size[0] * 24) + 50   # set window height (y coordinate)
    window.setup(width, height)          # set window resolution
    
    window.tracer(0)                     # skipping map drawing process, comment line if want to see it
   
    return window