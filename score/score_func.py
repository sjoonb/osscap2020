import os

def add_score(game, score):
    if score > 999:
        score = 999
    score_index = get_index(game, score)

    if score_index != 2:
        print("You set a new record!")
        while True:
            name = input("Enter your name : ")
            if (name.isalpha() == True) and (len(name) == 3):
                name = name.upper()
                break
            else:
                print("Wrong input!")
                continue
        write_score(game, score, name, score_index)
    else:
        print("You didn't set a new record")

def print_score(game):
    score_list = get_score(game)
    for a in score_list:
        for b in a:
            print(b, end = '')
        print()

def get_index(game, score):
    score_list = get_score(game)
    if game == "dodger":
        for i in range(2):
            if int(score) > int(score_list[i][1]):
                return i
        return 2
    elif game == "brick":
        if int(score) == 0:
            return 2
        for i in range(2):
            if int(score) < int(score_list[i][1]):
                return i
        return 2

def write_score(game, score, name, index):
    score_list = get_score(game)

    score = str(score)
    if len(score) == 1:
        score = '0' + '0' + score
    elif len(score) == 2:
        score = '0' + score

    if index == 0:
        score_list[1][0] = score_list[0][0]
        score_list[1][1] = score_list[0][1]
    score_list[index][0] = name
    score_list[index][1] = score

    f = open_file(game, 'w')
    vstr = ''
    for a in score_list:
        for b in a:
            vstr = vstr + b + ' '
        vstr = vstr.rstrip(' ')
        vstr = vstr + '\n'
    f.writelines(vstr)
    f.close()

def open_file(game, mode):
    if game == "dodger":
        f = open("score_dodger.txt", mode)
    elif game == "brick":
        f = open("score_brick.txt", mode)
    else: print("Wrong!")
    return f

def get_score(game):
    if game == "dodger":
        if os.path.isfile("score_dodger.txt") == False:
            f = open_file(game, 'w')
            f.close()
    elif gamme == "brick":
        if os.path.isfile("score_brick.txt") == False:
            f = open_file(game, 'w')
            f.close()

    f = open_file(game, 'r')
    score_list = []
    #lines = f.readlines()
    #for line in lines:
        #tmp = line.split()
        #score_list.append(tmp)
    for i in range(2):
        line = f.readline()
        if not line:
            if game == "dodger":
                tmp = ["XXX", "000"]
                score_list.append(tmp)
                continue
            elif game == "brick":
                tmp = ["XXX", "999"]
                score_list.append(tmp)
                continue
        tmp = line.split()
        score_list.append(tmp)
    return score_list

def get_alpha_num(game):
    score_list = get_score(game)
    an_list = []
    for a in score_list:
        for b in a:
            for c in b:
                an_list.append(c)
    print(an_list)
    return an_list


def file_reset():
    os.remove("score_dodger.txt")
    os.remove("score_brick.txt")

#file_reset()
#add_score("dodger", 30)
#print_score("dodger")
#get_alpha_num("dodger")
