import pygame, pygcurse
from pygame.locals import *

import LED_display as LD
import stt_thread as ST
import HC_SR04 as RS
import threading
import time
import copy
import list_set
import sys
import scoreboard


WINWIDTH = 32
WINHEIGHT = 16
FPS = 20
delay = 0.03


mode_list = ['mouse', 'keyboard', 'sensor']
mode = mode_list[2]
#mode = sys.argv[1]

isfullscreen = False

if mode == 'mouse':
    isfullscreen = True

iScreen = [[0 for i in range(WINWIDTH)] for j in range(WINHEIGHT)]
# - Pygcurse board

win = pygcurse.PygcurseWindow(WINWIDTH, WINHEIGHT, fullscreen=isfullscreen)

t=threading.Thread(target=LD.main, args=())
t.setDaemon(True)
t.start()


def main():
    newGame = True
    gameOver = False
    gameWin = 0
    start_time = time.time()
    mainClock = pygame.time.Clock()

    while True:

        if gameOver:
            oScreen = copy.deepcopy(iScreen)
            print_GameOver(oScreen)
            drawMatrix(oScreen)
            time.sleep(3)
            pygame.quit()
            scoreboard.main('brick', 0)
            sys.exit()
        elif gameWin == 2:
            oScreen = copy.deepcopy(iScreen)
            print_Clear(oScreen)
            drawMatrix(oScreen)
            time_score = round(time.time() - start_time)
            time.sleep(3)
            pygame.quit()
            scoreboard.main('brick', time_score)
            sys.exit()
        
        
        if newGame:
            pygame.mouse.set_pos(win.centerx * win.cellwidth, (win.bottom) * win.cellheight)
            mousex, mousey = pygame.mouse.get_pos()
            before_cellx_arr = [WINWIDTH//2] * 3
            cellx, celly = WINWIDTH//2, WINHEIGHT -2
            ballx, bally = cellx, WINHEIGHT - 3
            ball_direction = {'NW' : [-1, -1], 'N' : [0, -1], 'NE' : [1, -1], 'SW' : [-1, 1], 'S' : [0, 1], 'SE' : [1, 1]}
            ballspeed = 2

            ballspeed = 4 - ballspeed
            ballcnt = 0
            ballmv = ball_direction['N']
            
            bricks =[[1,1], [6,1], [11,1], [16,1], [21, 1], [26,1], [3,4], [8,4], [13,4], [18,4], [23,4]]

            if mode == 'keyboard':
                counter = 0
                moveRight = False
                moveLeft = False
            gameOver = False
            newGame = False


        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == ord('q')):
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN and event.key == ord('v')):
                time_score = round(time.time() - start_time)
                t2=threading.Thread(target=ST.ST_main, args=('b', str(time_score))) 
                t2.setDaemon(True)
                t2.start()
                
        # Input

            # mouse mode
            if mode == 'mouse':
                if event.type == MOUSEMOTION and not gameOver:
                    mousex, mousey = event.pos
                    cellx, celly = win.getcoordinatesatpixel(mousex, mousey)
                    celly = WINHEIGHT - 2

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

        if mode == 'sensor':
            if not gameOver:
                cellx = RS.get_distance()-10

        # Act
        oScreen = copy.deepcopy(iScreen) 


        drawBricks(bricks, oScreen)

        if mode == 'keyboard': 
            if not gameOver:
                if counter > 2:
                    if moveRight: cellx += 1
                    if moveLeft: cellx -= 1
                elif moveRight or moveLeft:
                    counter += 1

                if cellx < 2:
                    cellx = 2
                if cellx > WINWIDTH-3:
                    cellx = WINWIDTH-3

        elif mode == 'mouse':
            if cellx < 2:
                cellx = 2
            if cellx > WINWIDTH-3:
                cellx = WINWIDTH-3
        
        elif mode == 'sensor':
            if not gameOver:
                if cellx < 1 or cellx > WINWIDTH -2:
                    cellx = before_cellx_arr[-1]
                if abs(cellx - before_cellx_arr[-1]) > 10:
                    cellx = before_cellx_arr[-1] 
                else:
                    cellx = sum(before_cellx_arr[1:]+[cellx],1)//len(before_cellx_arr)
                    before_cellx_arr.pop(0)
                    before_cellx_arr.append(cellx)
                    cellx = before_cellx_arr[-1]


    

        # Ball check
        hit = oScreen[bally][ballx]
        if ballcnt == 0:
            # Hit wall
            if bally <= 0 or bally >= WINHEIGHT -1 or ballx <= 0 or ballx >= WINWIDTH - 1:
                if bally <= 0:
                    ballmv = [ballmv[0], -ballmv[1]]
                if ballx <= 0 or ballx >= WINWIDTH - 1:
                    ballmv = [-ballmv[0], ballmv[1]]
                if bally >= WINHEIGHT - 1:
                    gameOver = True
                    ballmv = [-ballmv[0], -ballmv[1]]
                    # GameOver

            # Hit brick
            elif hit == 3:
                bricks = breakBrick(ballx, bally, oScreen, bricks)
                
                for key, value in ball_direction.items():
                    if ballmv == value:
                        direction = key
                
                if direction[0] == 'N':
                    direction = 'S' + direction[1:] 
                elif direction[0] == 'S':
                    direction = 'N' + direction[1:]

                ballmv = ball_direction[direction]



            # Hit pad
            elif (bally == celly-1 or bally == celly) and ballx >= cellx -2 and ballx <= cellx + 2: 
                if ballx < cellx:
                    ballmv = ball_direction['NW']
                elif ballx > cellx:
                    ballmv = ball_direction['NE']
                else:
                    ballmv = ball_direction['N']

        # Draw ball
        if not gameOver:
            oScreen[bally][ballx] = 2
        else:
            oScreen[bally][ballx] = 4

        # Ball movement
        if ballcnt >= ballspeed:
            ballx += ballmv[0]
            bally += ballmv[1]
            ballcnt = 0
        else:
            ballcnt += 1

        # - Draw Matrix
        # consoleMatrix(oScreen)
        #pygcurseMatrix(oScreen)

        if len(bricks) == 0:
            gameWin += 1


        drawPad(cellx, celly, oScreen)
        drawMatrix(oScreen)
        mainClock.tick(FPS)

def breakBrick(x, y, screen, bricks):
    for brick in bricks:
        if x >= brick[0] and x <= brick[0] + 3 and y >= brick[1] and y <= brick[1] + 1:
            bricks.pop(bricks.index(brick))
            break
    
    return bricks


def drawBricks(bricks, screen):
    for brick in bricks:
        for i in range(brick[0], brick[0]+4):
            for j in range(brick[1], brick[1]+2):
                    screen[j][i] = 3

def drawPad(x, y, screen):
    for i in range(x-2,x+3,1):
        screen[y][i] = 1
    

def drawMatrix(array):
    for x in range(len(array[0])):
        for y in range(len(array)):
            if array[y][x] == 0:
                LD.set_pixel(x, y, 0)
            elif array[y][x] == 1:
                LD.set_pixel(x, y, 3)
            elif array[y][x] == 2:
                LD.set_pixel(x, y, 6)
            elif array[y][x] == 3:
                LD.set_pixel(x, y, 2)
            elif array[y][x] == 4:
                LD.set_pixel(x, y, 1)
            else:
                continue
            
            # color = 0 : 'None', 1 : 'Red', 2 : 'Green', 3 : 'Yellow', 4 : 'Blue', 5 : 'Purple', 6 : 'Crystal', 7 : 'White'

def drawChar(char, screen, width, height, direction, color):
    for i in range(width):
        for j in range(height):
            if char[j][i] == 1:
                screen[direction[1]+j][direction[0]+i] = color

def print_Clear(oScreen):
    drawChar(list_set.alpha_C, oScreen, 5, 7, (1,4), 2)
    drawChar(list_set.alpha_l, oScreen, 5, 7, (7, 4), 2)
    drawChar(list_set.alpha_e, oScreen, 5, 7, (13, 4), 2)
    drawChar(list_set.alpha_a, oScreen, 5, 7, (19, 4), 2)
    drawChar(list_set.alpha_r, oScreen, 5, 7, (25, 4), 2)

def print_GameOver(oScreen):
    drawChar(list_set.alpha_G, oScreen, 5, 7, (1,1), 4)
    drawChar(list_set.alpha_a, oScreen, 5, 7, (7,1), 4)
    drawChar(list_set.alpha_m, oScreen, 5, 7, (13,1), 4)
    drawChar(list_set.alpha_e, oScreen, 5, 7, (19,1), 4)
    drawChar(list_set.alpha_O, oScreen, 5, 7, (8, 9), 4)
    drawChar(list_set.alpha_v, oScreen, 5, 7, (14, 9), 4)
    drawChar(list_set.alpha_e, oScreen, 5, 7, (20, 9), 4)
    drawChar(list_set.alpha_r, oScreen, 5, 7, (26, 9), 4)

if __name__ == '__main__':
    main()
