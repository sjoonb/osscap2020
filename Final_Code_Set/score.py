import LED_display as LD
import threading

import time
import copy
import os
import sys

import list_set
from score_func import *

delay = 0.1

t=threading.Thread(target=LD.main, args=())
t.setDaemon(True)
t.start()

#drawChar(alphabet.alpha_a, oScreen, 5, 7, (1, 1), 1)

iScreen =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

w_list = [5, 5, 5, 3, 3, 3, 5, 5, 5, 3, 3, 3]
h_list = [7, 7, 7, 5, 5, 5, 7, 7, 7, 5, 5, 5]
xy_list = [(1, 1), (7, 1), (13, 1), (20, 2), (24, 2), (28, 2), (1, 9), (7, 9), (13, 9), (20, 10), (24, 10), (28, 10)]
color_list1 = [3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7]
color_list2 = [7, 7, 7, 7, 7, 7, 3, 3, 3, 3, 3, 3]

def main():
    game_num = sys.argv[1] # 'dodger' or 'brick'
    game_score = sys.argv[2] # 0 s 1~999
    if game_num == 1:
        game = "dodger"
    elif game_num == 2:
        game = "brick"
    score = int(input("score : "))
    index = get_index(game, score)
    add_score(game, score)
    matrix_list = get_matrix_list(game)


    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        
        oScreen = copy.deepcopy(iScreen) 
 
        # fill matrix 

        # - Change oScreen matrix output in this area
        if index == 0:
            for i in range(len(matrix_list)):
                drawChar(matrix_list[i], oScreen, w_list[i], h_list[i], xy_list[i], color_list1[i])
        elif index == 1:
            for i in range(len(matrix_list)):
                drawChar(matrix_list[i], oScreen, w_list[i], h_list[i], xy_list[i], color_list2[i])
        elif index == 2:
            for i in range(len(matrix_list)):
                drawChar(matrix_list[i], oScreen, w_list[i], h_list[i], xy_list[i], 7)


        '''
        drawChar(char1, oScreen, 5, 7, (1,1), 2)
        drawChar(char2, oScreen, 5, 7, (7,1), 2)
        drawChar(char3, oScreen, 5, 7, (13,1), 2)
        drawChar(num1, oScreen, 3, 5, (20,2), 2)
        drawChar(num2, oScreen, 3, 5, (24,2), 2)
        drawChar(num3, oScreen, 3, 5, (28,2), 2)
        drawChar(char4, oScreen, 5, 7, (1,9), 2)
        drawChar(char5, oScreen, 5, 7, (7,9), 2)
        drawChar(char6, oScreen, 5, 7, (13,9), 2)
        drawChar(num4, oScreen, 3, 5, (20,10), 2)
        drawChar(num5, oScreen, 3, 5, (24,10), 2)
        drawChar(num6, oScreen, 3, 5, (28,10), 2)
        '''

        # - Draw Matrix
        consoleMatrix(oScreen)
        drawMatrix(oScreen)


        time.sleep(delay)
        
        os.system('cls' if os.name == 'nt' else 'clear')



def consoleMatrix(screen):
    for i in screen:
        print(i)


def drawChar(char, screen, width, height, direction, color):
    for i in range(width):
        for j in range(height):
            if char[j][i] == 1:
                screen[direction[1]+j][direction[0]+i] = color

def get_matrix_list(game):
    matrix_list = []
    an_list = get_alpha_num(game)
    for i in an_list:
        if i == '0':
            matrix_list.append(list_set.num_0)
        elif i == '1':
            matrix_list.append(list_set.num_1)
        elif i == '2':
            matrix_list.append(list_set.num_2)
        elif i == '3':
            matrix_list.append(list_set.num_3)
        elif i == '4':
            matrix_list.append(list_set.num_4)
        elif i == '5':
            matrix_list.append(list_set.num_5)
        elif i == '6':
            matrix_list.append(list_set.num_6)
        elif i == '7':
            matrix_list.append(list_set.num_7)
        elif i == '8':
            matrix_list.append(list_set.num_8)
        elif i == '9':
            matrix_list.append(list_set.num_9)
        elif i == 's':
            matrix_list.append(list_set.num_s)
        elif i == 'A':
            matrix_list.append(list_set.alpha_A)
        elif i == 'B':
            matrix_list.append(list_set.alpha_B)
        elif i == 'C':
            matrix_list.append(list_set.alpha_C)
        elif i == 'D':
            matrix_list.append(list_set.alpha_D)
        elif i == 'E':
            matrix_list.append(list_set.alpha_E)
        elif i == 'F':
            matrix_list.append(list_set.alpha_F)
        elif i == 'G':
            matrix_list.append(list_set.alpha_G)
        elif i == 'H':
            matrix_list.append(list_set.alpha_H)
        elif i == 'I':
            matrix_list.append(list_set.alpha_I)
        elif i == 'J':
            matrix_list.append(list_set.alpha_J)
        elif i == 'K':
            matrix_list.append(list_set.alpha_K)
        elif i == 'L':
            matrix_list.append(list_set.alpha_L)
        elif i == 'M':
            matrix_list.append(list_set.alpha_M)
        elif i == 'N':
            matrix_list.append(list_set.alpha_N)
        elif i == 'O':
            matrix_list.append(list_set.alpha_O)
        elif i == 'P':
            matrix_list.append(list_set.alpha_P)
        elif i == 'Q':
            matrix_list.append(list_set.alpha_Q)
        elif i == 'R':
            matrix_list.append(list_set.alpha_R)
        elif i == 'S':
            matrix_list.append(list_set.alpha_S)
        elif i == 'T':
            matrix_list.append(list_set.alpha_T)
        elif i == 'U':
            matrix_list.append(list_set.alpha_U)
        elif i == 'V':
            matrix_list.append(list_set.alpha_V)
        elif i == 'W':
            matrix_list.append(list_set.alpha_W)
        elif i == 'X':
            matrix_list.append(list_set.alpha_X)
        elif i == 'Y':
            matrix_list.append(list_set.alpha_Y)
        elif i == 'Z':
            matrix_list.append(list_set.alpha_Z)
    return matrix_list

            
def drawBricks(bricks, screen):
    for brick in bricks:
        cnt = 0
        for i in range(brick[0], brick[0]+4):
            cnt += 1
            for j in range(brick[1], brick[1]+2):
                if cnt == 1 or cnt == 4:
                    screen[j][i] = 4
                else:
                    screen[j][i] = 3

def drawMatrix(array):
    for x in range(len(array[0])):
        for y in range(len(array)):
             LD.set_pixel(x, y, array[y][x])
            
            # color = 0 : 'None', 1 : 'Red', 2 : 'Green', 3 : 'Yellow', 4 : 'Blue', 5 : 'Purple', 6 : 'Crystal', 7 : 'White'

if __name__ == '__main__':
    main()
