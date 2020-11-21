import os

def add_score_dodger(name, score):
    f = open("score_dodger.txt", 'a')
    data = str(name) + ' ' + str(score) + '\n'
    f.write(data)
    f.close()

def add_score_bb(name, score):
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
    s_score = sorted(score_dict.items(), key = lambda x:x[1], reverse = True)
    for i in range(3):
        print("{} : {}".format(s_score[i][0], s_score[i][1]))
    f.close()

def clear_score():
    os.remove("score_dodger.txt")

def clear_score():
    os.remove("score_bb.txt")
