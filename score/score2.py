from matrix import *
import LED_display as LMD
import os
import alphabet
import number

def add_score(game, score):
    while True:
        name = input("Enter your name : ")
        if (name.isalpha() == True) and (len(name) == 3):
            name = name.upper()
            break
        else:
            print("Wrong input!")
            continue

    if game == "dodger":
        f = open("score_dodger.txt", 'a')
    elif game == "brick":
        f = open("score_brick.txt", 'a')
    else: print("Wrong!")

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
