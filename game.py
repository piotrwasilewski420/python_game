
# Imports
import pygame as py
from pygame.display import update

# Game Init
py.init()

# Screen Settings
width=1920
height=1080
screen = py.display.set_mode((width, height))

# Player
PlayerImg = py.image.load("player.png")

def player(x,y):
    screen.blit(PlayerImg, (((x-128)/2, (y-128))))

# Player Movement

# Game Loop
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    player(width,height)
    py.display.update()