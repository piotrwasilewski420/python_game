
# Imports
from pickle import TRUE
import pygame as py
from pygame.display import update

# Game Init
py.init()

# Screen Settings
width=1000
height=700
screen = py.display.set_mode((width, height))
surface = py.display.get_surface() #get the surface of the current active display
SurfaceWidth,SurfaceHeight = size = surface.get_width(), surface.get_height()#create an array of surface.width and surface.height
# Player
PlayerImg = py.image.load("player.png")
PlayerX=width
def player(x,y):
    screen.blit(PlayerImg, (((x-128)/2, (y-128))))
# UFO
UFOImg = py.image.load("ufo.png")
UFOX=width
UFOY=0
UFOChange=1
def UFO(x,y):
    screen.blit(UFOImg, (((x-128)/2, y)))
# Bullet
isBulletReady=False
bulletImg = py.image.load("bullet.png")
def bullet(x,y):
    screen.blit(bulletImg, (x,y))
def firBullet(x,y):
    bullet(x,y)
bulletChange=1
bulletY=height-128-32+bulletChange
bulletX=0

# Player Movement
PlayerChange=0
# Game Loop
running = True
print(SurfaceWidth)
while running:
    screen.fill((0,0,0))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                PlayerChange -= 1
            if event.key == py.K_SPACE: 
                print("bullet")
                if isBulletReady==False:
                    bulletX=PlayerX
                isBulletReady=True     
            if event.key == py.K_RIGHT:
                PlayerChange += 1
                print(PlayerChange)
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT:
                PlayerChange = 0
            if event.key == py.K_RIGHT:
                PlayerChange = 0
    #Player
    PlayerX += PlayerChange
    if PlayerX <= 64:
        PlayerX=64
    elif PlayerX >= (width*2)-64:
        PlayerX = (width*2)-64
    # print(PlayerX)

    #UFO
    UFOX += UFOChange
    if UFOX <= 64:
        # UFOX=64
        UFOChange *= -1
    elif UFOX >= (width*2)-64:
        # UFOX = (width*2)-64
        UFOChange *= -1
    # print(UFOX) 
    # print(UFOChange)
    UFO(UFOX,UFOY)
    player(PlayerX,height)
    # bullet
    print((PlayerX-27)/2)
    if isBulletReady == True:
        firBullet((bulletX-27)/2,bulletY-bulletChange)
        bulletChange += 0.5
        if bulletY-bulletChange <= 0:
            print("tak")
            isBulletReady=False
            bulletChange=1
    py.display.update()