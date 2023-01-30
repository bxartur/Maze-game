"""
Module providing loading images from dedicated directory
"""
import os
from turtle import register_shape

def load_graphics():
    # set path
    basic_path = os.getcwd()
    os.chdir(os.getcwd() + "\content\graphics")
    
    # add graphics
    register_shape("wall.gif")
    register_shape("path.gif")
    register_shape("hero_right.gif")
    register_shape("hero_left.gif")
    register_shape("hero_up.gif")
    register_shape("hero_down.gif")
    register_shape("guard_right.gif")
    register_shape("guard_left.gif")
    register_shape("guard_up.gif")
    register_shape("treasure_chest.gif")
    register_shape("exit.gif")

    os.chdir(basic_path)
