from tkinter import *
import random

#gamesettings
GAME_WIDTH = 700
GAME_HIGHT = 700
SPEED = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FODD_COLOR = '#FF0000'
BACKROUND_COLOR = '#000000'

#classes
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill = SNAKE_COLOR,tag = 'snake')
            self.squares.append(square)