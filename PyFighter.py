#-------------------------------------------------------------------------------
# Name:        PyFighter
# Purpose:     Fse computer science
#
# Author:      Abdul Khan and Tyler Wiggins
#
# Created:     06/15/2012
# Copyright:   Roaring Cattle co. (c)
#-------------------------------------------------------------------------------
#!/usr/bin/env python

"""
This is the fighting game made by Tyler and Abdul.
With all vectors, [right] is set as the positive Y-axis
and [down] is set as the positive X-axis.

This game contains is a full menu, including a  main
menu, and character selection menu, and a map selection
menu. When the game starts, two 'karate' guys fight
each other, with their respective health bars
shown in the corners.

We had several problems with the rendering of the
animations when flipping the orientation of the images.
When an attack was done the image shifted back. This
was fixed by changing the point from which the image
was drawn. Instead of having the image drawn relative
to the end where the attack is, it had to be drawn
relative to the back side of the player (quite complex).
Also, there were many issues with collision and
registering attacks, but those were fixed as well.

This program demonstrates our knowledge of all the main
aspects of Python learned in class, and many others not
discussed in class, such as classes (no pun intended),
and global variables used in functions.

The controls for player 1 are wasd to move, v to punch,
and c to kick. The controls for player 2 are up, down,
left, right to move, shift to punch, and / to kick.


"""

from pygame import *
from random import randint
from sys import *
import sys
import pygame
import random
##from health import *

init()

WHITE =255,255,255 # background
BLUE = 0,0,255
RED = 255,0,0
GREEN = 0,255,0
YELLOW = 255,255,0
PURPLE = 255,0,255
BLACK = 0,0,0
NUM_COLOURS = 7
GROUND = 525
exitPause = False
FPS = 50
frameLength = 0.02 # 1 frame = 0.02s

WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
screen= display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
display.set_caption('PyFighter')
loading = image.load('loading.png')
screen.blit(loading, (0,0))
display.flip()


# ============================================================================ #

main = True
game = True
end = False

moveLeft = {'p1':False, 'p2':False}
moveRight = {'p1':False, 'p2':False}
jump = {'p1':False, 'p2':False}
punch = {'p1':False, 'p2':False}
kick = {'p1':False, 'p2':False}
block = {'p1':False, 'p2':False}

menu = 0

# menu images
title = image.load('title.png')
mapselection = image.load('map selection.png')
characterSelect = image.load('charecterselect.png')
characterRyu = image.load('ryu.png')
characterBalrog = image.load('balrog.png')
characterDhalsim = image.load('dhalsim.png')
pause = image.load('pause.png')
instructionsImg = image.load('instructions.png')

# map images
mortalKombat = image.load('maps/MK map.png')
dungeon = image.load('maps/dungeon.png')
finalDestination = image.load('maps/final destination.png')
marioLand = image.load('maps/mario land.png')
minecraft = image.load('maps/minecraft.png')
city = image.load('maps/city street.png')
citynight = image.load('maps/city street night.png')

# winning/losing screens
p1wins = image.load('p1wins.png')
p2wins = image.load('p2wins.png')
tieGame = image.load('tie.png')

# health bar images
health1 = image.load('player1health.png')
health2 = image.load('player2health.png')

# music and sounds
punchSound = pygame.mixer.Sound('punch.wav')
kickSound = pygame.mixer.Sound('kick.wav')
pygame.mixer.music.load('music1.mp3')

# character booleans
Ryu = False
Balrog = False
Dhalsim = False

Ryu1 = False
Balrog1 = False
Dhalsim1 = False

Ryu2 = False
Balrog2 = False
Dhalsim2 = False

# menu booleans
start = False
instructions = False
exitGame = False
player1 = False
player2 = False
click = False
clickBack = False
clickBack1 = False
Back = False
select1 = True
select2 = False
mapSelected= False
game = False
characterMenu = 0
mapMenuX = 0
mapMenuY = 0
map1= False
map2= False
map3= False
map4= False
map5= False
map6= False
Back1= False
counter1 = 0
gameMap = mortalKombat
healthcolor1 = GREEN
healthcolor2 = GREEN

player1health = 100
player2health = 100

resume = False
gameExit = False


# ============================== Character Data ============================== #

# for frame dictionaries: i = idle, p = punch, k = kick, w = walking
balrog = {'i1':image.load('characters/balrog/idle1.png'),
          'i2':image.load('characters/balrog/idle2.png'),
          'i3':image.load('characters/balrog/idle3.png'),
          'i4':image.load('characters/balrog/idle4.png'),
          'p1':image.load('characters/balrog/punch1.png'),
          'p2':image.load('characters/balrog/punch2.png'),
          'p3':image.load('characters/balrog/punch3.png'),
          'k1':image.load('characters/balrog/kick1.png'),
          'k2':image.load('characters/balrog/kick2.png'),
          'k3':image.load('characters/balrog/kick3.png'),
          'k4':image.load('characters/balrog/kick4.png'),
          'k5':image.load('characters/balrog/kick5.png'),
          'w1':image.load('characters/balrog/walking1.png'),
          'w2':image.load('characters/balrog/walking2.png'),
          'w3':image.load('characters/balrog/walking3.png'),
          'w4':image.load('characters/balrog/walking4.png')}

ryu = {'i1':image.load('characters/ryu/idle1.png'),
       'i2':image.load('characters/ryu/idle2.png'),
       'i3':image.load('characters/ryu/idle3.png'),
       'i4':image.load('characters/ryu/idle4.png'),
       'i5':image.load('characters/ryu/idle5.png'),
       'p1':image.load('characters/ryu/punch1.png'),
       'p2':image.load('characters/ryu/punch2.png'),
       'p3':image.load('characters/ryu/punch3.png'),
       'k1':image.load('characters/ryu/kick1.png'),
       'k2':image.load('characters/ryu/kick2.png'),
       'k3':image.load('characters/ryu/kick3.png'),
       'k4':image.load('characters/ryu/kick4.png'),
       'k5':image.load('characters/ryu/kick5.png'),
       'w1':image.load('characters/ryu/walking1.png'),
       'w2':image.load('characters/ryu/walking2.png'),
       'w3':image.load('characters/ryu/walking3.png'),
       'w4':image.load('characters/ryu/walking4.png'),
       'w5':image.load('characters/ryu/walking5.png'),
       'w6':image.load('characters/ryu/walking6.png')}

dhalsim = {'i1':image.load('characters/dhalsim/idle1.png'),
           'i2':image.load('characters/dhalsim/idle2.png'),
           'i3':image.load('characters/dhalsim/idle3.png'),
           'i4':image.load('characters/dhalsim/idle4.png'),
           'i5':image.load('characters/dhalsim/idle5.png'),
           'i6':image.load('characters/dhalsim/idle6.png'),
           'i7':image.load('characters/dhalsim/idle7.png'),
           'i8':image.load('characters/dhalsim/idle8.png'),
           'i9':image.load('characters/dhalsim/idle9.png'),
           'p1':image.load('characters/dhalsim/punch1.png'),
           'p2':image.load('characters/dhalsim/punch2.png'),
           'w1':image.load('characters/dhalsim/walking1.png'),
           'w2':image.load('characters/dhalsim/walking2.png'),
           'w3':image.load('characters/dhalsim/walking3.png'),
           'w4':image.load('characters/dhalsim/walking4.png'),
           'w5':image.load('characters/dhalsim/walking5.png'),
##           'p3':image.load('characters/dhalsim/punch3.png'),
##           'p4':image.load('characters/dhalsim/punch4.png'),
           'k1':image.load('characters/dhalsim/kick1.png'),
           'k2':image.load('characters/dhalsim/kick2.png'),
           'k3':image.load('characters/dhalsim/kick3.png'),
           'k4':image.load('characters/dhalsim/kick4.png'),
           'k5':image.load('characters/dhalsim/kick5.png'),
           'k6':image.load('characters/dhalsim/kick6.png')}

class Player:
    def __init__(self, spawnx, spawny, direction, GROUND, frameLength, idleList, punchList, kickList, walkingList):
        self.x = spawnx # refers to centerx of the player
        self.y = spawny # refers to the bottom of the player
        self.xVel = 0
        self.yVel = 0
        self.jumpInitSpeed = 700 # (px/s)
        self.WALKSPEED = 200
        self.direction = direction
        self.WIDTH = 100
        self.HEIGHT = 150
        self.hp = 100
        self.accely = 0
        self.mainRect = 0

        # idle frames
        self.idleImagesRight = []
        self.idleRectsRight = []

        # walking frames
        self.walkingImagesRight = []
        self.walkingRectsRight = []

        self.walkingImagesLeft = []
        self.walkingRectsLeft = []

        self.idleImagesLeft = []
        self.idleRectsLeft = []

        # punch frames
        self.punchImagesRight = []
        self.punchRectsRight = []

        self.punchImagesLeft = []
        self.punchRectsLeft = []

        # kick frames
        self.kickImagesRight = []
        self.kickRectsRight = []

        self.kickImagesLeft = []
        self.kickRectsLeft = []

        # fill up image lists - images are added more than once to make animation slower independent of framerate
        # idle
        for i in idleList:
            for j in range (15 // len(idleList)):
                self.idleImagesRight.append(i)
        for i in self.idleImagesRight:
            self.idleRectsRight.append(i.get_rect())


        for i in idleList:
            for j in range (15 // len(idleList)):
                self.idleImagesLeft.append(transform.flip(i, True, False))
        for i in self.idleImagesLeft:
            self.idleRectsLeft.append(i.get_rect())

        # walking
        for i in walkingList:
            for j in range (15 // len(idleList)):
                self.walkingImagesRight.append(i)
        for i in self.walkingImagesRight:
            self.walkingRectsRight.append(i.get_rect())


        for i in walkingList:
            for j in range (15 // len(idleList)):
                self.walkingImagesLeft.append(transform.flip(i, True, False))
        for i in self.walkingImagesLeft:
            self.walkingRectsLeft.append(i.get_rect())

        # punch
        for i in punchList:
            for j in range (15 // len(punchList)):
                self.punchImagesRight.append(i)
        for i in self.punchImagesRight:
            self.punchRectsRight.append(i.get_rect())

        for i in punchList:
            for j in range (15 // len(punchList)):
                self.punchImagesLeft.append(transform.flip(i, True, False))
        for i in self.punchImagesLeft:
            self.punchRectsLeft.append(i.get_rect())

        # kick
        for i in kickList:
            for j in range (15 // len(kickList)):
                self.kickImagesRight.append(i)
        for i in self.kickImagesRight:
            self.kickRectsRight.append(i.get_rect())

        for i in kickList:
            for j in range (15 // len(kickList)):
                self.kickImagesLeft.append(transform.flip(i, True, False))
        for i in self.kickImagesLeft:
            self.kickRectsLeft.append(i.get_rect())

        # index counters for each 'type' of frame - this decides which frame is drawn
        self.punchFrameCtr = 0
        self.kickFrameCtr = 0
        self.idleFrameCtr = 0
        self.walkingFrameCtr = 0
        self.rect = self.idleRectsRight[0]
        if direction == 'right':
            self.rect = self.idleRectsRight[0]
            self.rect.bottom = GROUND
            self.rect.centerx = self.x
            self.tempRect = self.rect
        if direction == 'left':
            self.rect = self.idleRectsLeft[0]
            self.rect.bottom = GROUND
            self.rect.centerx = self.x
            self.tempRect = self.rect

        self.baseRect = self.idleRectsLeft[0]

    def update(self, moveLeft, moveRight, jump, punch, kick, frameLength, WINDOWWIDTH, GROUND, getPunched, getKicked): # signs denote direction of vectors
        # velocity of X-direction (no acceleration)
        ##if self.direction == 'right':

        if not moveRight:
            self.xVel = 0
        if not moveLeft:
            self.xVel = 0
        if moveLeft:
            self.xVel = -self.WALKSPEED
            self.direction = 'left'
        if moveRight:
            self.xVel = self.WALKSPEED
            self.direction = 'right'

        # acceleration of Y-direction (acceleration only exists if player is above ground)
        if jump == True and self.rect.bottom == GROUND:
            self.yVel = -self.jumpInitSpeed

        if self.rect.bottom < GROUND:
            self.accely = 1200
        if self.rect.bottom == GROUND:
            self.accely = 0

        # velocity of Y-direction --> v2 = v1 + at
        self.yVel += self.accely * frameLength

        # X and Y positions --> change in position = time (length of frame) x velocity
        # also wall collision
        if not punch and not kick:
            self.rect.centerx += self.xVel * frameLength
        self.rect.bottom += self.yVel * frameLength

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOWWIDTH:
            self.rect.right = WINDOWWIDTH
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.yVel = 0

        self.x = self.rect.centerx
        self.y = self.rect.bottom
##        print("yVel:", self.yVel, "accely:", self.accely, "yPos", self.rect.bottom)
    def updateRect(self, punch, kick, walking):
        # updating rectangles for each 'type' of frame, punch, kicking, walking, and idle for left and right
        if punch or self.punchFrameCtr > 0:
            if self.direction == 'right':
                self.tempRect = self.punchRectsRight[self.punchFrameCtr]
                self.tempRect.centerx = self.x
                self.tempRect.bottom = self.y
                self.x = self.rect.left
                self.y = self.rect.top
                self.mainRect = Rect(self.x, self.y, self.punchRectsRight[self.punchFrameCtr].width, self.punchRectsRight[self.punchFrameCtr].height)
                self.baseRect = Rect(self.x, self.y, self.idleRectsRight[0].width, self.idleRectsRight[0].height)
            if self.direction == 'left':
                self.tempRect = self.punchRectsLeft[self.punchFrameCtr]
                self.tempRect.centerx = self.x
                self.tempRect.bottom = self.y
                self.x = self.rect.right - self.tempRect.width
                self.y = self.rect.top
                self.mainRect = Rect(self.x, self.y, self.punchRectsLeft[self.punchFrameCtr].width, self.punchRectsLeft[self.punchFrameCtr].height)
                self.baseRect = Rect(self.x, self.y, self.idleRectsRight[0].width, self.idleRectsRight[0].height)
        elif kick or self.kickFrameCtr > 0:
            if self.direction == 'right':
                self.tempRect = self.kickRectsRight[self.kickFrameCtr]
                self.tempRect.centerx = self.x
                self.tempRect.bottom = self.y
                self.x = self.rect.left
                self.y = self.rect.top
                self.mainRect = Rect(self.x, self.y, self.kickRectsRight[self.kickFrameCtr].width, self.kickRectsRight[self.kickFrameCtr].height)
                self.baseRect = Rect(self.x, self.y, self.idleRectsRight[0].width, self.idleRectsRight[0].height)
            if self.direction == 'left':
                self.tempRect = self.kickRectsLeft[self.kickFrameCtr]
                self.tempRect.centerx = self.x
                self.tempRect.bottom = self.y
                self.x = self.rect.right - self.tempRect.width
                self.y = self.rect.top
                self.mainRect = Rect(self.x, self.y, self.kickRectsLeft[self.kickFrameCtr].width, self.kickRectsLeft[self.kickFrameCtr].height)
                self.baseRect = Rect(self.x, self.y, self.idleRectsRight[0].width, self.idleRectsRight[0].height)
        elif walking or self.walkingFrameCtr > 0:
            if self.direction == 'right':
                self.tempRect = self.walkingRectsRight[self.walkingFrameCtr]
                self.tempRect.centerx = self.x
                self.tempRect.bottom = self.y
                self.x = self.rect.left
                self.y = self.rect.top
                self.mainRect = Rect(self.x, self.y, self.walkingRectsRight[self.walkingFrameCtr].width, self.walkingRectsRight[self.walkingFrameCtr].height)
                self.baseRect = Rect(self.x, self.y, self.idleRectsRight[0].width, self.idleRectsRight[0].height)
            if self.direction == 'left':
                self.tempRect = self.walkingRectsLeft[self.walkingFrameCtr]
                self.tempRect.centerx = self.x
                self.tempRect.bottom = self.y
                self.x = self.rect.right - self.tempRect.width
                self.y = self.rect.top
                self.mainRect = Rect(self.x, self.y, self.walkingRectsLeft[self.walkingFrameCtr].width, self.walkingRectsLeft[self.walkingFrameCtr].height)
                self.baseRect = Rect(self.x, self.y, self.idleRectsRight[0].width, self.idleRectsRight[0].height)

        else:
            if self.direction == 'right':
                self.tempRect = self.idleRectsRight[self.idleFrameCtr]
                self.tempRect.centerx = self.x
                self.tempRect.bottom = self.y
                self.x = self.tempRect.left
                self.y = self.tempRect.top
                self.mainRect = Rect(self.x, self.y, self.idleRectsRight[self.idleFrameCtr].width, self.idleRectsRight[self.idleFrameCtr].height)
            if self.direction == 'left':
                self.tempRect = self.idleRectsLeft[self.idleFrameCtr]
                self.tempRect.centerx = self.x
                self.tempRect.bottom = self.y
                self.x = self.tempRect.right - self.tempRect.width
                self.y = self.tempRect.top
                self.mainRect = Rect(self.x, self.y, self.idleRectsLeft[self.idleFrameCtr].width, self.idleRectsLeft[self.idleFrameCtr].height)


    def draw(self, punch, kick, walking): # drawing the frames for all types of frames
        if punch or self.punchFrameCtr > 0:
            if self.punchFrameCtr < len(self.punchImagesRight):
                if self.direction == 'right':
                    screen.blit(self.punchImagesRight[self.punchFrameCtr], (self.x, self.y))
                if self.direction == 'left':
                    screen.blit(self.punchImagesLeft[self.punchFrameCtr], (self.x, self.y))
            self.punchFrameCtr += 1
            if self.punchFrameCtr == len(self.punchImagesRight):
                self.punchFrameCtr = 0

        elif kick or self.kickFrameCtr > 0:
            if self.kickFrameCtr < len(self.kickImagesRight):
                if self.direction == 'right':
                    screen.blit(self.kickImagesRight [self.kickFrameCtr], (self.x, self.y))
                if self.direction == 'left':
                    screen.blit(self.kickImagesLeft [self.kickFrameCtr], (self.x, self.y))
            self.kickFrameCtr += 1
            if self.kickFrameCtr == len(self.kickImagesRight):
                self.kickFrameCtr = 0

        elif walking or self.walkingFrameCtr > 0:
            if self.walkingFrameCtr < len(self.walkingImagesRight):
                if self.direction == 'right':
                    screen.blit(self.walkingImagesRight[self.walkingFrameCtr], (self.x, self.y))
                if self.direction == 'left':
                    screen.blit(self.walkingImagesLeft[self.walkingFrameCtr], (self.x, self.y))
            self.walkingFrameCtr += 1
            if self.walkingFrameCtr == len(self.walkingImagesRight):
                self.walkingFrameCtr = 0

        else:
            if self.idleFrameCtr < len(self.idleImagesRight):
                if self.direction == 'right':
                    screen.blit(self.idleImagesRight [self.idleFrameCtr], (self.x, self.y))
                if self.direction == 'left':
                    screen.blit(self.idleImagesLeft [self.idleFrameCtr], (self.x, self.y))
            self.idleFrameCtr += 1
            if self.idleFrameCtr == len(self.idleImagesRight):
                self.idleFrameCtr = 0
# ============================================================================ #
p1 = Player(WINDOWWIDTH // 3,
                 GROUND, 'right',
                 GROUND,
                 0.02,
                 (ryu['i1'], ryu['i2'], ryu['i3'], ryu['i4'], ryu['i5']),
                 (ryu['p1'], ryu['p2'], ryu['p3']),
                 (ryu['k1'], ryu['k2'], ryu['k3'], ryu['k4'], ryu['k5']),
                 (ryu['w1'], ryu['w2'], ryu['w3'], ryu['w4'], ryu['w5'], ryu['w6']))

p2 = Player(2 * WINDOWWIDTH // 3,
                 GROUND, 'right',
                 GROUND,
                 0.02,
                 (balrog['i1'], balrog['i2'], balrog['i3'], balrog['i4']),
                 (balrog['p1'], balrog['p2'], balrog['p3']),
                 (balrog['k1'], balrog['k2'], balrog['k3'], balrog['k4']),
                 (balrog['w1'], balrog['w2'], balrog['w3'], balrog['w4']))
balrogplayer1 = Player( WINDOWWIDTH // 3,
                 GROUND, 'right',
                 GROUND,
                 0.02,
                 (balrog['i1'], balrog['i2'], balrog['i3'], balrog['i4']),
                 (balrog['p1'], balrog['p2']),
                 (balrog['k1'], balrog['k2'], balrog['k3']),
                 (balrog['w1'], balrog['w2'], balrog['w3'], balrog['w4']))

ryuplayer1 = Player(WINDOWWIDTH // 3,
                 GROUND, 'right',
                 GROUND,
                 0.02,
                 (ryu['i1'], ryu['i2'], ryu['i3'], ryu['i4'], ryu['i5']),
                 (ryu['p1'], ryu['p2'], ryu['p3']),
                 (ryu['k1'], ryu['k2'], ryu['k3']),
                 (ryu['w1'], ryu['w2'], ryu['w3'], ryu['w4'], ryu['w5'], ryu['w6']))


balrogplayer2 = Player(2 * WINDOWWIDTH // 3,
                 GROUND, 'left',
                 GROUND,
                 0.02,
                 (balrog['i1'], balrog['i2'], balrog['i3'], balrog['i4']),
                 (balrog['p1'], balrog['p2']),
                 (balrog['k1'], balrog['k2'], balrog['k3']),
                 (balrog['w1'], balrog['w2'], balrog['w3'], balrog['w4']))

ryuplayer2 = Player(2 *WINDOWWIDTH // 3,
                 GROUND, 'left',
                 GROUND,
                 0.02,
                 (ryu['i1'], ryu['i2'], ryu['i3'], ryu['i4'], ryu['i5']),
                 (ryu['p1'], ryu['p2'], ryu['p3']),
                 (ryu['k1'], ryu['k2'], ryu['k3']),
                 (ryu['w1'], ryu['w2'], ryu['w3'], ryu['w4'], ryu['w5'], ryu['w6']))
dhalsimplayer1 = Player(WINDOWWIDTH // 3,
                 GROUND, 'right',
                 GROUND,
                 0.02,
                 (dhalsim['i1'], dhalsim['i3'], dhalsim['i5'], dhalsim['i7'], dhalsim['i9']),
                 (dhalsim['p1'], dhalsim['p2']),
                 (dhalsim['k1'], dhalsim['k2'], dhalsim['k3'], dhalsim['k4']),
                 (dhalsim['w1'], dhalsim['w2'], dhalsim['w3'], dhalsim['w4'], dhalsim['w5']))

dhalsimplayer2 = Player(2 * WINDOWWIDTH // 3,
                 GROUND, 'left',
                 GROUND,
                 0.02,
                 (dhalsim['i1'], dhalsim['i3'], dhalsim['i5'], dhalsim['i7'], dhalsim['i9']),
                 (dhalsim['p1'], dhalsim['p2']),
                 (dhalsim['k1'], dhalsim['k2'], dhalsim['k3'], dhalsim['k4']),
                 (dhalsim['w1'], dhalsim['w2'], dhalsim['w3'], dhalsim['w4'], dhalsim['w5']))

def checkForInput():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        return

def healthBar1():
    global p1, healthcolor1
    screen.blit(health1 , (0,0))
    draw.rect(screen, healthcolor1, (0, 30, p1.hp * 2,42))
    if p1.hp < 33:
        healthcolor1 = RED
    elif p1.hp >32 and p1.hp < 66:
        healthcolor1 = YELLOW
    else:
        healthcolor1 = GREEN

def healthBar2():
    global p2, healthcolor2
    screen.blit(health2 , (800,0))
    draw.rect(screen, healthcolor2, (800, 30, p2.hp*2,42))
    if p2.hp < 33:
        healthcolor2 = RED
    elif p2.hp >32 and p2.hp < 66:
        healthcolor2 = YELLOW
    else:
        healthcolor2 = GREEN


def terminate():
    quit()
    exit()

def makingValuesFalse( ):
    global start,instructions,exitGame, Ryu,Balrog,Dhalsim, Ryu1,Balrog1,Dhalsim1, Ryu2,Balrog2,Dhalsim2, player1,player2, click,clickBack,Back,select1,select2
    global map1,map2,map3,map4,map5,map6,Back1,clickBack1,mapSelected,gameMap,GROUND, gameMap,game
    start = False
    instructions = False
    exitGame = False

    Ryu = False
    Balrog = False
    Dhalsim = False

    Ryu1 = False
    Balrog1 = False
    Dhalsim1 = False

    Ryu2 = False
    Balrog2 = False
    Dhalsim2 = False

    player1 = False
    player2 = False

    click = False
    clickBack = False
    clickBack1 = False
    Back = False


    player1 = False
    player2 = False

    select1 = True
    select2 = False
    mapSelected= False
    map1= False
    map2= False
    map3= False
    map4= False
    map5= False
    map6= False
    Back1= False
    game = False
    GROUND = 525
    gameMap =mortalKombat
def buttons( ):

#==================== Selects what button you are on due to what your value is=================================#
    global menu

    pygame.event.get()
    screen.blit(title , (0,0))
    k = key.get_pressed()

    if k [K_DOWN]:
        menu += 1
    if k [K_UP]:
        menu -= 1
    if menu >9:
        menu =9
    if menu <0:
        menu = 0
    return
def rectanglesAroundText( ):
    global menu
    global instructions
    global start
    global exitGame
#============================Draws rectangels around the buttons and sets the button to true if you are selected on it====================================#
    if menu >= 0 and menu <= 2:
        start = True
        draw.rect(screen, YELLOW, (700, 150, 130 ,40),5)
    else :
        start = False

            ## instructionss
    if menu > 2 and menu <7  :
        instructions = True
        draw.rect(screen, YELLOW, (700, 210, 285 ,40),5)
    else:
        instructions = False


            ## exit game
    if menu >= 7 and menu <=9 :
        exitGame = True
        draw.rect(screen, YELLOW, (700, 250, 230 ,40),5)
    else:
        exitGame = False

def clickingStartMenu( ):
    global menu
    global instructions
    global start
    global exitGame
#========================= Makes buttons actualy do something================================#
    if exitGame == True and k [K_RETURN]:
        terminate ()


    display.flip()
## charecter selection screen
    if start == True and k [K_RETURN]:
        menu = 0
        click = True
        time.delay(200)

def characterMenuFn( ):
#==================== Selects what character you are on due to what your value is=================================#
    global characterMenu
    global k

    pygame.event.get()
    k = key.get_pressed()
    screen.blit(characterSelect, (0,0))

    if k [K_DOWN]:
        characterMenu += 1

    if k [K_UP]:
        characterMenu -= 1

    if characterMenu >9:
        characterMenu =9
    if characterMenu <0:
        characterMenu = 0

def rectAroundMenu( ):
    global charecterMenu
    global Ryu,Ryu1,Ryu2
    global Dhalsim,Dhalsim1,Dhalsim2
    global Balrog,Balrog1,Balrog2
    global player1
    global k
    global Back
# Draws rectangle around the words and depending on whitch character you are on it will draw an image #
    if characterMenu >= 0 and characterMenu <= 2 and player1 == False :
        Balrog = True
        draw.rect(screen, YELLOW, (430, 120, 150 ,60),5)
        screen.blit(characterBalrog , (100,150))
    elif characterMenu >= 0 and characterMenu <= 2 and player1 == True :
        Balrog = True
        draw.rect(screen, YELLOW, (430, 120, 150 ,60),5)
        screen.blit(characterBalrog , (700,150))
    else :
        Balrog = False


    if characterMenu > 2 and characterMenu <7 and player1 == False :
        Ryu = True
        draw.rect(screen, YELLOW, (450, 215, 100 ,60),5)
        screen.blit(characterRyu , (100,150))
    elif characterMenu > 2 and characterMenu <7 and player1 == True  :
        Ryu = True
        draw.rect(screen, YELLOW, (450, 215, 100 ,60),5)
        screen.blit(characterRyu , (700,150))
    else:
        Ryu = False


    if characterMenu >= 7 and characterMenu <=9 and player1 == False :
        Dhalsim = True
        draw.rect(screen, YELLOW, (410, 305, 190 ,60),5)
        screen.blit(characterDhalsim , (100,150))
    elif characterMenu >= 7 and characterMenu <=9 and player1 == True  :
        Dhalsim = True
        draw.rect(screen, YELLOW, (410, 305, 190 ,60),5)
        screen.blit(characterDhalsim , (700,150))
    else:
        Dhalsim = False



def checkingCharacter( ):
    global charecterMenu
    global player1,player2
    global Ryu,Ryu1,Ryu2
    global Dhalsim,Dhalsim1,Dhalsim2
    global Balrog,Balrog1,Balrog2
    global Back
    global select1,select2,game
# checks which character you have selected and  sets you character in the game to match the character you have selected #
    if Balrog == True and k [K_RETURN] and select1 == True :
        player1 = True
        Balrog1 = True
        select2 = True
        Ryu1 = False
        Dhalsim1 = False

    if  Ryu  == True and k [K_RETURN] and select1 == True :
        player1 = True
        Ryu1 = True
        select2 = True
        Balrog1 = False
        Dhalsim1 = False

    if Dhalsim  == True and k [K_RETURN] and select1 == True :
        player1 = True
        Dhalsim1  = True
        select2 = True
        Balrog1 = False
        Ryu1 = False
    if player1 == True and Balrog1 == True :
        screen.blit(characterBalrog , (100,150))

    if player1 == True and Ryu1 == True :
        screen.blit(characterRyu , (100,150))

    if player1 == True and Dhalsim1 == True :
        screen.blit(characterDhalsim , (100,150))

    if player1 == True  and player2 == True:
        game = True


    display.flip()
def checkingCharacter2():
    global charecterMenu
    global player1,player2
    global Ryu,Ryu1,Ryu2
    global Dhalsim,Dhalsim1,Dhalsim2
    global Balrog,Balrog1,Balrog2
    global Back
    global select1,select2,game
# checks for player two's selection of character
    if Balrog == True and k [K_RETURN] and select2  == True :
        Balrog2 = True
        player2 = True
        Ryu2 = False
        Dhalsim2 = False

    if  Ryu  == True and k [K_RETURN] and select2  == True :
        Ryu2 = True
        player2 = True
        Balrog2 = False
        Dhalsim2 = False

    if Dhalsim  == True and k [K_RETURN] and select2 == True:
        Dhalsim2  = True
        player2 = True
        Balrog2 = False
        Ryu2 = False
###################### charecters stay on left side
# Draws the character on either side depending oon who you have selected
    if player1 == True and Balrog1 == True :
        screen.blit(characterBalrog , (100,150))

    if player1 == True and Ryu1 == True :
        screen.blit(characterRyu , (100,150))

    if player1 == True and Dhalsim1 == True :
        screen.blit(characterDhalsim , (100,150))

    if player1 == True  and player2 == True:
        game = True
    if player2 == True and Balrog2 == True :
        screen.blit(characterBalrog , (700,150))
    if player2 == True and Ryu2 == True :
        screen.blit(characterRyu , (700,150))
    if player2 == True and Dhalsim2 == True :
        screen.blit(characterDhalsim , (700,150))

##    return player1
##    return player2

################## exit if hit back
    if player1 == True  and player2 == True:
        game = True


    display.flip()

############################################################################################################################
def mapSelection():
# scrolls through the maps depeding what arrow key you have selected
    global mapMenuY, mapMenuX
    pygame.event.get()
    k = key.get_pressed()
    screen.blit(mapselection, (0,0))

    if k [K_DOWN]:
        mapMenuY += 1

    if k [K_UP]:
        mapMenuY -= 1

    if mapMenuY >5:
        mapMenuY = 5
    if mapMenuY <0:
        mapMenuY = 0

    if k [K_RIGHT]:
        mapMenuX += 1

    if k [K_LEFT]:
        mapMenuX -= 1

    if mapMenuX >9:
        mapMenuX = 9
    if mapMenuX <0:
        mapMenuX = 0
def rectMap():
# Draws the rectangle around the map, also chooses map depending on whitch map you select
    global mapMenuX, mapMenuY,mapSelected, gameMap
    global map1,map2,map3,map4,map5,map6,Back1,Back,GROUND
#**********************Draws all rectangles around and selects map*****************************#

    if mapMenuY >= 0 and mapMenuY <= 2 and mapMenuX >= 0 and mapMenuX <= 2 :
        map1 = True
        gameMap = dungeon
        mapSelected = True
        GROUND = 525
        draw.rect(screen, YELLOW, (53, 110, 295 ,180),5)
    else :
        map1 = False

            ## instructionss
    if  mapMenuY >= 0 and mapMenuY <= 2 and mapMenuX >= 3 and mapMenuX <= 6 :
        map2 = True
        GROUND = 495
        gameMap = finalDestination
        mapSelected = True
        draw.rect(screen, YELLOW, (360, 110, 300 ,180),5)
    else:
        map2 = False


            ## exit game
    if mapMenuY >= 0 and mapMenuY <= 2 and mapMenuX >= 7 and mapMenuX <= 9:
        map3 = True
        GROUND = 525
        gameMap = mortalKombat
        mapSelected = True
        draw.rect(screen, YELLOW, (670, 110, 295 ,180),5)
    else:
        map3 = False

    if mapMenuY >= 3 and mapMenuY <= 5 and mapMenuX >= 0 and mapMenuX <= 2 :
        map4 = True
        GROUND = 525
        gameMap = minecraft
        mapSelected = True
        draw.rect(screen, YELLOW, (47, 325, 295 ,175),5)
    else :
        map4 = False

            ## instructionss
    if  mapMenuY >= 3 and mapMenuY <= 5 and mapMenuX >= 3 and mapMenuX <= 6 :
        map5 = True
        GROUND = 525
        gameMap = city
        mapSelected = True
        draw.rect(screen, YELLOW, (360, 328, 290 ,175),5)
    else:
        map5 = False


            ## exit game
    if mapMenuY >= 3 and mapMenuY <= 5 and mapMenuX >= 7 and mapMenuX <= 9:
        map6 = True
        GROUND = 525
        gameMap = citynight
        mapSelected = True
        draw.rect(screen, YELLOW, (670, 327, 295 ,178),5)
    else:
        map6 = False

    display.flip()
## charecter selection screen


pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1, 0.0)
while True:
    pygame.event.get()
    k = key.get_pressed()
    makingValuesFalse( )
    buttons( )
    rectanglesAroundText( )
    clickingStartMenu(  )
    checkForInput()
    if instructions == True and k [K_RETURN]:
        while True:
            pygame.event.get()
            k = key.get_pressed()
            screen.blit(instructionsImg, (0,0))
            display.flip()
            if k [K_ESCAPE]:
                break
            checkForInput()



    end = False
    p1.hp = 100
    p2.hp = 100
    counter1 = 0

    if start == True and k [K_RETURN]:
        menu = 0
        time.delay(200)
        while True:
            exitPause = False
            pygame.event.get()
            k = key.get_pressed()
            characterMenuFn( )
            rectAroundMenu( )
            checkingCharacter( )
            checkForInput()
            print(characterMenu)

            if player1 == True:
                counter1 += 1
            if player1 == True and counter1 >= 20:
                time.delay(200)
                while True:
                    pygame.event.get()
                    k = key.get_pressed()
                    checkingCharacter2()
                    characterMenuFn( )
                    rectAroundMenu( )
                    print(characterMenu)
##                    checkingCharacter( )
                    checkForInput()
                    if game == True:
                        time.delay(200)
                        while True:

                            pygame.event.get()
                            k = key.get_pressed()
                            mapSelection()
                            rectMap ()
                            checkForInput()



# ==============================redecaring character data ============================================== #

                            balrogplayer1 = Player( WINDOWWIDTH // 3,
                                             GROUND, 'right',
                                             GROUND,
                                             0.02,
                                             (balrog['i1'], balrog['i2'], balrog['i3'], balrog['i4']),
                                             (balrog['p1'], balrog['p2']),
                                             (balrog['k1'], balrog['k2'], balrog['k3']),
                                             (balrog['w1'], balrog['w2'], balrog['w3'], balrog['w4']))

                            ryuplayer1 = Player(WINDOWWIDTH // 3,
                                             GROUND, 'right',
                                             GROUND,
                                             0.02,
                                             (ryu['i1'], ryu['i2'], ryu['i3'], ryu['i4'], ryu['i5']),
                                             (ryu['p1'], ryu['p2'], ryu['p3']),
                                             (ryu['k1'], ryu['k2'], ryu['k3']),
                                             (ryu['w1'], ryu['w2'], ryu['w3'], ryu['w4'], ryu['w5'], ryu['w6']))


                            balrogplayer2 = Player(2 * WINDOWWIDTH // 3,
                                             GROUND, 'left',
                                             GROUND,
                                             0.02,
                                             (balrog['i1'], balrog['i2'], balrog['i3'], balrog['i4']),
                                             (balrog['p1'], balrog['p2']),
                                             (balrog['k1'], balrog['k2'], balrog['k3']),
                                             (balrog['w1'], balrog['w2'], balrog['w3'], balrog['w4']))

                            ryuplayer2 = Player(2 *WINDOWWIDTH // 3,
                                             GROUND, 'left',
                                             GROUND,
                                             0.02,
                                             (ryu['i1'], ryu['i2'], ryu['i3'], ryu['i4'], ryu['i5']),
                                             (ryu['p1'], ryu['p2'], ryu['p3']),
                                             (ryu['k1'], ryu['k2'], ryu['k3']),
                                             (ryu['w1'], ryu['w2'], ryu['w3'], ryu['w4'], ryu['w5'], ryu['w6']))
                            dhalsimplayer1 = Player(WINDOWWIDTH // 3,
                                             GROUND, 'right',
                                             GROUND,
                                             0.02,
                                             (dhalsim['i1'], dhalsim['i3'], dhalsim['i5'], dhalsim['i7'], dhalsim['i9']),
                                             (dhalsim['p1'], dhalsim['p2']),
                                             (dhalsim['k1'], dhalsim['k2'], dhalsim['k3'], dhalsim['k4']),
                                             (dhalsim['w1'], dhalsim['w2'], dhalsim['w3'], dhalsim['w4'], dhalsim['w5']))

                            dhalsimplayer2 = Player(2 * WINDOWWIDTH // 3,
                                             GROUND, 'left',
                                             GROUND,
                                             0.02,
                                             (dhalsim['i1'], dhalsim['i3'], dhalsim['i5'], dhalsim['i7'], dhalsim['i9']),
                                             (dhalsim['p1'], dhalsim['p2']),
                                             (dhalsim['k1'], dhalsim['k2'], dhalsim['k3'], dhalsim['k4']),
                                             (dhalsim['w1'], dhalsim['w2'], dhalsim['w3'], dhalsim['w4'], dhalsim['w5']))
                            # selects who your the character is
                            if Balrog1 == True:
                                p1 = balrogplayer1
                            if Ryu1 == True :
                                p1 = ryuplayer1
                            if Balrog2 == True:
                                p2 = balrogplayer2
                            if Ryu2 == True :
                                p2 = ryuplayer2
                            if Dhalsim1:
                                p1 = dhalsimplayer1
                            if Dhalsim2:
                                p2 = dhalsimplayer2
                            if characterMenu >=10 and k [K_RETURN]:
                                break
                                Back = True

                            if mapSelected == True and k [K_RETURN]:
#======================================= main game ==========================================#
                                while main:
                                    moveLeft = {'p1':False, 'p2':False}
                                    moveRight = {'p1':False, 'p2':False}
                                    jump = {'p1':False, 'p2':False}
                                    punch = {'p1':False, 'p2':False}
                                    kick = {'p1':False, 'p2':False}
                                    idle = {'p1':True, 'p2':True}
                                    walking = {'p1':False, 'p2':False}
                                    punchRect1 = Rect(0,0,10,10)
                                    punchRect2 = Rect(0,0,10,10)
                                    while game:
                                        punch = {'p1':False, 'p2':False}
                                        kick = {'p1':False, 'p2':False}

                                        for event in pygame.event.get():
                                            if event.type == QUIT:
                                                pygame.quit()
                                                sys.exit()
                                            if event.type == KEYDOWN:
                                                # player 1 controls
                                                if event.key == ord('a'):
                                                    moveRight['p1'] = False
                                                    moveLeft['p1'] = True
                                                    walking['p1'] = True
                                                if event.key == ord('d'):
                                                    moveLeft['p1'] = False
                                                    moveRight['p1'] = True
                                                    walking['p1'] = True
                                                if event.key == ord('w'):
                                                    jump['p1'] = True

                                                if event.key == ord('b'):
                                                    block['p1'] = True
                                                if event.key == ord('v'):
                                                    punch['p1'] = True
                                                if event.key == ord('c'):
                                                    kick['p1'] = True
                                                # player 2 controls
                                                if event.key == K_LEFT:
                                                    moveRight['p2'] = False
                                                    moveLeft['p2'] = True
                                                    walking['p2'] = True
                                                if event.key == K_RIGHT:
                                                    moveLeft['p2'] = False
                                                    moveRight['p2'] = True
                                                    walking['p2'] = True
                                                if event.key == K_UP:
                                                    jump['p2'] = True
                                                if event.key == K_RCTRL:
                                                    block['p2'] = True
                                                if event.key == ord('/'):
                                                    punch['p2'] = True
                                                if event.key == ord('.'):
                                                    kick['p2'] = True


                                            if event.type == KEYUP:
                                                # player 1 controls
                                                if event.key == ord('a'):
                                                    moveLeft['p1'] = False
                                                    walking['p1'] = False
                                                if event.key == ord('d'):
                                                    moveRight['p1'] = False
                                                    walking['p1'] = False
                                                if event.key == ord('w'):
                                                    jump['p1'] = False
                                                if event.key == ord('b'):
                                                    block['p1'] = False
                                                if event.key == ord('v'):
                                                    punch['p1'] = False
                                                if event.key == ord('c'):
                                                    kick['p1'] = False

                                                # player 2 controls
                                                if event.key == K_LEFT:
                                                    moveLeft['p2'] = False
                                                    walking['p2'] = False
                                                if event.key == K_RIGHT:
                                                    moveRight['p2'] = False
                                                    walking['p2'] = False
                                                if event.key == K_UP:
                                                    jump['p2'] = False
                                                if event.key == K_RCTRL:
                                                    block['p2'] = False
                                                if event.key == ord('/'):
                                                    punch['p2'] = False
                                                if event.key == ord('.'):
                                                    kick['p2'] = False
                                                if event.key == ord('p') or event.key == K_ESCAPE:
                                                    pausemenu = 0
                                                    resume = False
                                                    gameExit = False
                                                    while True:
                                                        screen.blit (pause,(0,0))

                                                        pygame.event.get()
                                                        k = key.get_pressed()
                                                        screen.blit(pause, (0,0))

                                                        if k [K_DOWN]:
                                                            pausemenu += 1

                                                        if k [K_UP]:
                                                            pausemenu -= 1

                                                        if pausemenu > 1:
                                                            pausemenu = 1
                                                        if pausemenu < 0:
                                                            pausemenu = 0

                                                        if pausemenu == 0:
                                                            resume = True
                                                            draw.rect(screen, YELLOW, (350, 140, 350 ,75),5)


                                                        else :
                                                            resume = False
                                                            draw.rect(screen, YELLOW, (420, 250, 170 ,75),5)
                                                        if pausemenu == 1 and k [K_RETURN]:
                                                            end = True

                                                        display.flip()
                                                        if resume == True and k [K_RETURN]:
                                                            break
                                                        if end == True and k [K_RETURN]:
                                                            exitPause = True
                                                            break


                                        screen.blit(gameMap, (0,0)) # updating positions
                                        p1.update(moveLeft['p1'], moveRight['p1'], jump['p1'], punch['p1'], kick['p1'], frameLength, WINDOWWIDTH, GROUND, False, False)
                                        p1.updateRect(punch['p1'], kick['p1'], walking['p1'])

                                        p2.update(moveLeft['p2'], moveRight['p2'], jump['p2'], punch['p2'], kick['p2'], frameLength, WINDOWWIDTH, GROUND, False, False)
                                        p2.updateRect(punch['p2'], kick['p2'], walking['p2'])
         # =========================== COLLISIONS AND HP==============================================================================
                                        if p1 == dhalsimplayer1: # dhalsim has special collisions because of his abnormal frames.
                                            # for punches
                                            # 1 on 2
                                            if p1.punchFrameCtr == len(p1.punchImagesRight) - 1:
                                                punchRange = abs(p1.baseRect.width - p1.mainRect.width)
                                                if p1.direction == 'right':
                                                    punchRect1 = Rect(p1.baseRect.x + p1.baseRect.width, p1.baseRect.y, punchRange, p1.baseRect.height)
                                                    if punchRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 2
                                                        punchSound.play()
                                                if p1.direction == 'left':
                                                    punchRect1 = Rect(p1.mainRect.x, p1.baseRect.y, punchRange, p1.baseRect.height)

                                                    if punchRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 2
                                                        punchSound.play()

                                            # 2 on 1
                                            elif p2.punchFrameCtr == len(p2.punchImagesRight) - 1:
                                                punchRange = abs(p2.baseRect.width - p2.mainRect.width)
                                                if p2.direction == 'right':
                                                    punchRect2 = Rect(p2.baseRect.x + p2.baseRect.width - 15, p2.baseRect.y, punchRange + 15, p2.baseRect.height)
                                                    if punchRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 2
                                                        punchSound.play()
                                                if p2.direction == 'left':
                                                    punchRect2 = Rect(p2.mainRect.x, p2.baseRect.y, punchRange, p2.baseRect.height)
                                                    if punchRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 2
                                                        punchSound.play()

                                            # for kicks
                                            # 1 on 2
                                            elif p1.kickFrameCtr == len(p1.kickImagesRight) - 1:
                                                kickRange = abs(p1.baseRect.width - p1.mainRect.width)
                                                if p1.direction == 'right':
                                                    kickRect1 = Rect(p1.baseRect.x + p1.baseRect.width - 30, p1.baseRect.y, kickRange + 30, p1.baseRect.height)
                                                    if kickRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 5
                                                        kickSound.play()
                                                if p1.direction == 'left':
                                                    kickRect1 = Rect(p1.mainRect.x, p1.baseRect.y, kickRange + 30, p1.baseRect.height)

                                                    if kickRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 5
                                                        kickSound.play()

                                            # 2 on 1
                                            elif p2.kickFrameCtr == len(p2.kickImagesRight) - 1:
                                                kickRange = abs(p2.baseRect.width - p2.mainRect.width)
                                                if p2.direction == 'right':
                                                    kickRect2 = Rect(p2.baseRect.x + p2.baseRect.width, p2.baseRect.y, kickRange, p2.baseRect.height)
                                                    if kickRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 5
                                                        kickSound.play()
                                                if p2.direction == 'left':
                                                    kickRect2 = Rect(p2.mainRect.x, p2.baseRect.y, kickRange, p2.baseRect.height)
                                                    if kickRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 5
                                                        kickSound.play()


                                        if p2 == dhalsimplayer2:
                                            # for punches
                                            # 1 on 2
                                            if p1.punchFrameCtr == len(p1.punchImagesRight) - 1:
                                                punchRange = abs(p1.baseRect.width - p1.mainRect.width)
                                                if p1.direction == 'right':
                                                    punchRect1 = Rect(p1.baseRect.x + p1.baseRect.width, p1.baseRect.y, punchRange, p1.baseRect.height)
                                                    if punchRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 2
                                                        punchSound.play()
                                                if p1.direction == 'left':
                                                    punchRect1 = Rect(p1.mainRect.x, p1.baseRect.y, punchRange, p1.baseRect.height)

                                                    if punchRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 2
                                                        punchSound.play()

                                            # 2 on 1
                                            elif p2.punchFrameCtr == len(p2.punchImagesRight) - 1:
                                                punchRange = abs(p2.baseRect.width - p2.mainRect.width)
                                                if p2.direction == 'right':
                                                    punchRect2 = Rect(p2.baseRect.x + p2.baseRect.width, p2.baseRect.y, punchRange, p2.baseRect.height)
                                                    if punchRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 2
                                                        punchSound.play()
                                                if p2.direction == 'left':
                                                    punchRect2 = Rect(p2.mainRect.x, p2.baseRect.y, punchRange, p2.baseRect.height)
                                                    if punchRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 2
                                                        punchSound.play()

                                            # for kicks
                                            # 1 on 2
                                            elif p1.kickFrameCtr == len(p1.kickImagesRight) - 1:
                                                kickRange = abs(p1.baseRect.width - p1.mainRect.width)
                                                if p1.direction == 'right':
                                                    kickRect1 = Rect(p1.baseRect.x + p1.baseRect.width, p1.baseRect.y, kickRange, p1.baseRect.height)
                                                    if kickRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 5
                                                        kickSound.play()
                                                if p1.direction == 'left':
                                                    kickRect1 = Rect(p1.mainRect.x, p1.baseRect.y, kickRange, p1.baseRect.height)

                                                    if kickRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 5
                                                        kickSound.play()

                                            # 2 on 1
                                            elif p2.kickFrameCtr == len(p2.kickImagesRight) - 1:
                                                kickRange = abs(p2.baseRect.width - p2.mainRect.width)
                                                if p2.direction == 'right':
                                                    kickRect2 = Rect(p2.baseRect.x + p2.baseRect.width - 30, p2.baseRect.y, kickRange + 30, p2.baseRect.height)
                                                    if kickRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 5
                                                        kickSound.play()
                                                if p2.direction == 'left':
                                                    kickRect2 = Rect(p2.mainRect.x, p2.baseRect.y, kickRange + 30 , p2.baseRect.height)
                                                    if kickRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 5
                                                        kickSound.play()

                                        if p1 != dhalsimplayer1 and p2 != dhalsimplayer2:
                                            # for punches
                                            # 1 on 2
                                            if p1.punchFrameCtr == len(p1.punchImagesRight) - 1:
                                                punchRange = abs(p1.baseRect.width - p1.mainRect.width)
                                                if p1.direction == 'right':
                                                    punchRect1 = Rect(p1.baseRect.x + p1.baseRect.width, p1.baseRect.y, punchRange, p1.baseRect.height)
                                                    if punchRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 2
                                                        punchSound.play()
                                                if p1.direction == 'left':
                                                    punchRect1 = Rect(p1.mainRect.x, p1.baseRect.y, punchRange, p1.baseRect.height)

                                                    if punchRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 2
                                                        punchSound.play()

                                            # 2 on 1
                                            elif p2.punchFrameCtr == len(p2.punchImagesRight) - 1:
                                                punchRange = abs(p2.baseRect.width - p2.mainRect.width)
                                                if p2.direction == 'right':
                                                    punchRect2 = Rect(p2.baseRect.x + p2.baseRect.width, p2.baseRect.y, punchRange, p2.baseRect.height)
                                                    if punchRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 2
                                                        punchSound.play()
                                                if p2.direction == 'left':
                                                    punchRect2 = Rect(p2.mainRect.x, p2.baseRect.y, punchRange, p2.baseRect.height)
                                                    if punchRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 2
                                                        punchSound.play()

                                            # for kicks
                                            # 1 on 2
                                            elif p1.kickFrameCtr == len(p1.kickImagesRight) - 1:
                                                kickRange = abs(p1.baseRect.width - p1.mainRect.width)
                                                if p1.direction == 'right':
                                                    kickRect1 = Rect(p1.baseRect.x + p1.baseRect.width, p1.baseRect.y, kickRange, p1.baseRect.height)
                                                    if kickRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 5
                                                        kickSound.play()
                                                if p1.direction == 'left':
                                                    kickRect1 = Rect(p1.mainRect.x, p1.baseRect.y, kickRange, p1.baseRect.height)

                                                    if kickRect1.colliderect(p2.mainRect):
                                                        p2.hp -= 5
                                                        kickSound.play()

                                            # 2 on 1
                                            elif p2.kickFrameCtr == len(p2.kickImagesRight) - 1:
                                                kickRange = abs(p2.baseRect.width - p2.mainRect.width)
                                                if p2.direction == 'right':
                                                    kickRect2 = Rect(p2.baseRect.x + p2.baseRect.width, p2.baseRect.y, kickRange, p2.baseRect.height)
                                                    if kickRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 5
                                                        kickSound.play()
                                                if p2.direction == 'left':
                                                    kickRect2 = Rect(p2.mainRect.x, p2.baseRect.y, kickRange, p2.baseRect.height)
                                                    if kickRect2.colliderect(p1.mainRect):
                                                        p1.hp -= 5
                                                        kickSound.play()


                                        print(p1.hp, p2.hp)
                                        p1.draw(punch['p1'], kick['p1'], walking['p1'])
                                        p2.draw(punch['p2'], kick['p2'], walking['p2'])
        ##                                draw.rect(screen, BLUE, punchRect1)
        ##                                draw.rect(screen, BLUE, punchRect2)
        ##                                draw.rect(screen, BLUE, kickRect1)
        ##                                draw.rect(screen, BLUE, kickRect2)
                                        healthBar2()
                                        healthBar1()
                                        display.update()
                                        time.delay(10)
                                        if p1.hp <= 0:
                                            end = True
                                        if p2.hp <= 0:
                                            end = True
                                        if end == True:
                                            time.delay(1500)
                                            if exitPause == True:
                                                pass
                                            elif p1.hp < p2.hp:
                                                screen.blit(p2wins, (0,0))
                                                display.flip()
                                                checkForInput()
                                                time.delay(3000)

                                            elif p2.hp < p1.hp:
                                                screen.blit(p1wins, (0,0))
                                                display.flip()
                                                checkForInput()
                                                time.delay(3000)

                                            elif p1.hp == p2.hp and p1.hp <= 0:
                                                screen.blit(tieGame, (0,0))
                                                display.flip()
                                                checkForInput()
                                                time.delay(3000)

                                            break
                                    if end == True:
                                        break
                                if end == True:
                                    break
                            if end == True:
                                break
                        if end == True:
                            break
                    if end == True:
                        break
                if end == True:
                    break
            if end == True:
                break
                        ##            if player1==True and player2==True:

