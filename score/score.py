from matrix import *
import LED_display as LMD
import os
import alphabet
import number

def draw_matrix(m):
    array = m.get_Array()
    for y in range(m.get_dy()-4):
        for x in range(4, m.get_dx()-4):
            if array[y][x] == 0:
                LMD.set_pixel(y, 19-x, 0)
            elif array[y][x] == 1:
                LMD.set_pixel(y, 19-x, 4)
            else:
                continue
        print()

def add_score_dodger(score):
    while True:
        name = input("Enter your name : ")
        if (name.isalpha() == True) and (name.isupper() == True) and (len(name) == 3):
            break
        else:
            print("Wrong input!")
            continue
    f = open("score_dodger.txt", 'a')
    data = str(name) + ' ' + str(score) + '\n'
    f.write(data)
    f.close()

def add_score_bb(score):
    while True:
        name = input("Enter your name : ")
        if (name.isalpha() == True) and (name.isupper() == True) and (len(name) == 3):
            break
        else:
            print("Wrong input!")
            continue
    f = open("score_bb.txt", 'a')
    data = str(name) + ' ' + str(score) + '\n'
    f.write(data)
    f.close()

def print_score_dodger():
    score_dict = {}
    f = open("score_dodger.txt", 'r')
    lines = f.readlines()
    for line in lines:
        tmp = line.split()
        score_dict[tmp[0]] = int(tmp[1])
    s_score = sorted(score_dict.items(), key = lambda x:x[1], reverse = True)
    for i in range(3):
        print("{} : {}".format(s_score[i][0], s_score[i][1]))
    f.close()

def print_score_bb():
    score_dict = {}
    f = open("score_bb.txt", 'r')
    lines = f.readlines()
    for line in lines:
        tmp = line.split()
        score_dict[tmp[0]] = int(tmp[1])
    s_score = sorted(score_dict.items(), key = lambda x:x[1])
    for i in range(3):
        print("{} : {}".format(s_score[i][0], s_score[i][1]))
    f.close()

def clear_score_dodger():
    os.remove("score_dodger.txt")

def clear_score_bb():
    os.remove("score_bb.txt")
