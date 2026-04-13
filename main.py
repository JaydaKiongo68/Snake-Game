from tkinter import *
import random

#gamesettings
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKROUND_COLOR = '#000000'
SPACE_SIZE = 50

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

class Food:
    def __init__(self):
        x =  random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y =  random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag='food')

#Game Window Set-Up
score = 0
direction = "down"

window = Tk()
window.title("Snake Game")
window.resizeable(False, False)

label = Label(window, text='score: {}'.format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(
    window,
    bg=BACKROUND_COLOR,
    height=GAME_HEIGHT,
    width=GAME_WIDTH
)
canvas.pack()