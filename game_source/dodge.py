
# By Al Sweigart al@inventwithpython.com

# This program is a demo for the Pygcurse module.
# Simplified BSD License, Copyright 2011 Al Sweigart

import pygame, random, sys, time, pygcurse
from pygame.locals import *

import LED_display as TLD
import HC_SR04 as RS
import random
import threading
import keyboard
#import time
import os
import copy

GREEN = (0, 255, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

WINWIDTH = 32
WINHEIGHT = 16
TEXTCOLOR = WHITE
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 20
BADDIEMINSIZE = 1
BADDIEMAXSIZE = 5
BADDIEMINSPEED = 4
BADDIEMAXSPEED = 1
ADDNEWBADDIERATE = 50
isfullscreen = False

# Mode
mode_list = ['mouse', 'keyboard', 'sensor']
mode = mode_list[2]

if mode == 'mouse':
    isfullscreen = True


# Make board
win = pygcurse.PygcurseWindow(WINWIDTH, WINHEIGHT, fullscreen=isfullscreen)
pygame.display.set_caption('Pygcurse Dodger')
win.autoupdate = False

# Modified to play in LED Matrix

t=threading.Thread(target=TLD.main, args=())
t.setDaemon(True)
t.start()

# Screen
iScreen = [[0 for i in range(WINWIDTH)] for j in range(WINHEIGHT)]


moveLeft = False
moveRight = False
counter = 0

def main():
    global moveLeft, moveRight, counter
    showStartScreen()
    pygame.mouse.set_visible(False)
    mainClock = pygame.time.Clock()
    gameOver = False

    newGame = True
    while True:
        if gameOver and time.time() - 4 > gameOverTime:
            newGame = True
        
        # First setting
        if newGame:
            newGame = False
            
            # Set first position of character
            pygame.mouse.set_pos(win.centerx * win.cellwidth, (win.bottom) * win.cellheight)
            mousex, mousey = pygame.mouse.get_pos()
            cellx, celly = WINWIDTH//2, WINHEIGHT-1
            before_cellx_arr = [WINWIDTH//2] * 3
            print(before_cellx_arr)
            baddies = []
            baddieAddCounter = 0
            gameOver = False
            score = 0

        win.fill(bgcolor=BLACK)

        if mode == 'sensor':
            if not gameOver:
                cellx = RS.get_distance()-10


        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                terminate()
        # Character's move

            # mouse mode
            if mode == 'mouse':
                if event.type == MOUSEMOTION and not gameOver:
                    mousex, mousey = event.pos
                    cellx, celly = win.getcoordinatesatpixel(mousex, mousey)

            # keyboard mode
            elif mode == 'keyboard':
                if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == ord('a'):
                        if not gameOver:
                            cellx -= 1
                            counter += 1
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT or event.key == ord('d'):
                        if not gameOver:
                            cellx += 1
                            counter += 1
                        moveLeft == False
                        moveRight = True
                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == ord('a'):
                        counter = 0
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        counter = 0
                        moveRight = False 

                

        # add new baddies if needed
        # ADDNEWBADDIERATE determines amount of new baddies
        if baddieAddCounter == ADDNEWBADDIERATE:
            speed = random.randint(BADDIEMAXSPEED, BADDIEMINSPEED)
            baddies.append({'size': random.randint(BADDIEMINSIZE, BADDIEMAXSIZE),
                            'speed': speed,
                            'x': random.randint(0, win.width),
                            'y': -BADDIEMAXSIZE,
                            'movecounter': speed})
            baddieAddCounter = 0
        else:
            baddieAddCounter += 1


        # move baddies down, remove if needed
        for i in range(len(baddies)-1, -1, -1):
            if baddies[i]['movecounter'] == 0:
                baddies[i]['y'] += 1
                baddies[i]['movecounter'] = baddies[i]['speed']
            else:
                baddies[i]['movecounter'] -= 1
    
            # print(i, baddies[i]['y'])
            
            if baddies[i]['y'] > win.height:
                del baddies[i]
            


        # check if hit
        if not gameOver:
            for baddie in baddies:
                if cellx >= baddie['x'] and WINHEIGHT-1 >= baddie['y'] and cellx < baddie['x']+baddie['size'] and WINHEIGHT-1 < baddie['y']+baddie['size']:
                    gameOver = True
                    gameOverTime = time.time()
                    break
            score += 1

        # draw screen
        oScreen = copy.deepcopy(iScreen)

        # draw baddies to screen (Mouse Mode)
        for baddie in baddies:
            win.fill('#', GREEN, BLACK, (baddie['x'], baddie['y'], baddie['size'], baddie['size']))
            fillMatrix(baddie['x'], baddie['y'], baddie['size'], oScreen, WINWIDTH, WINHEIGHT)
            #for i in oScreen:
            #    print(i)


        if mode == 'keyboard': 
            # todo - Boost
            if not gameOver:
                if counter > 3:
                    if moveRight: cellx += 1
                    if moveLeft: cellx -= 1
                elif moveRight or moveLeft:
                    counter += 1

                if cellx < 0:
                    cellx = 0
                if cellx > WINWIDTH -1:
                    cellx = WINWIDTH-1

        elif mode == 'sensor':
            if not gameOver:
                if cellx < 0 or cellx > WINWIDTH -1:
                    cellx = before_cellx_arr[-1]
                if abs(cellx - before_cellx_arr[-1]) > 10:
                    cellx = before_cellx_arr[-1] 
                else:
                    cellx = sum(before_cellx_arr[1:]+[cellx],1)//len(before_cellx_arr)
                    before_cellx_arr.pop(0)
                    before_cellx_arr.append(cellx)
                    cellx = before_cellx_arr[-1]

      
        # draw character to screen
        if not gameOver:
            playercolor = WHITE
            oScreen[WINHEIGHT-1][cellx] = 2
        else:
            playercolor = RED
            oScreen[WINHEIGHT-1][cellx] = 3
            win.putchars('GAME OVER', win.centerx-4, win.centery, fgcolor=RED, bgcolor=BLACK)
  

        win.putchar('@', cellx, WINHEIGHT-1, playercolor)
        win.putchars('Score: %s' % (score), win.width - 14, 1, fgcolor=WHITE)
        win.update()
        

        drawMatrix(oScreen)
        mainClock.tick(FPS)


def showStartScreen():
    while checkForKeyPress() is None:
        win.fill(bgcolor=BLACK)
        win.putchars('Pygcurse Dodger', win.centerx-8, win.centery, fgcolor=TEXTCOLOR)
        if int(time.time() * 2) % 2 == 0: # flashing
            win.putchars('Press a key to start!', win.centerx-11, win.centery+1, fgcolor=TEXTCOLOR)
        win.update()


def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        if event.key == K_ESCAPE:
            terminate()
        return event.key
    return None

# Game display

def fillMatrix(bx, by, size, screen, w, h):
    for i in range(by, by+size):
        for j in range(bx, bx+size):
            if i < 0 or i >= h or j < 0 or j >= w:
                continue
            #print(i, j)
            screen[i][j] = 1  

def fillCharacter(cx, cy, screen): 
    if i < 0 or i >= h or j < 0 or j >= w:
        return

def drawMatrix(array):
    for x in range(len(array[0])):
        for y in range(len(array)):
            if array[y][x] == 0:
                TLD.set_pixel(x, y, 0)
            elif array[y][x] == 1:
                TLD.set_pixel(x, y, 2)
            elif array[y][x] == 2:
                TLD.set_pixel(x, y, 7)
            elif array[y][x] == 3:
                TLD.set_pixel(x, y, 1)
            else:
                continue

# Game mode

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
