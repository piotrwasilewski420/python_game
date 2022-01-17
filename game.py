
# Imports
from pickle import TRUE
import pygame as py
from pygame.display import update
import math

# Game Init
py.init()
score=0
font = py.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True,66, 66)
textRect = text.get_rect()
# Screen Settings
width=1000
height=700
textRect.center = (width // 2, height // 2)
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
UFOY=20
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

# Rectangles
bulletRect = bulletImg.get_rect(topleft= ((bulletX-27)/2,bulletY-bulletChange))
UFORect = UFOImg.get_rect(topleft=(UFOX,UFOY))
# Player Movement
PlayerChange=0

# Colision Detection
def isColided(bx,by,ux,uy):
    if abs(by-uy) < 110 and abs(bx-ux) < 600:
        global isBulletReady 
        global bulletChange
        global score
        bulletChange=1
        isBulletReady = False 
        score+=1
        print(bx)
        print()
        print(ux)
        print()
        print(abs(bx-ux))
       
# Game Loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(text, textRect)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                PlayerChange -= 1
            if event.key == py.K_SPACE: 
                if isBulletReady==False:
                    bulletX=PlayerX
                isBulletReady=True     
            if event.key == py.K_RIGHT:
                PlayerChange += 1
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
    # Colision
    isColided((bulletX-27)/2,bulletY-bulletChange,UFOX,UFOY)
    # bullet
    if isBulletReady == True:
        firBullet((bulletX-27)/2,bulletY-bulletChange)
        bulletChange += 0.5
        if bulletY-bulletChange <= 0:
            isBulletReady=False
            bulletChange=1
    # print("BulletX",(bulletX-27)/2)
    # print("BulletY",bulletY-bulletChange)
    # print("UFOY",UFOY)
    # print("UFOX",UFOX)
    # print(isBulletReady)
    # print("-----")
    print(score)
    py.display.update()