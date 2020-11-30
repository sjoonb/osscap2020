import stt
import os

while(True):
    print('Game or Weather')
    word = stt.main()
    
    if word == '게임':
        print("게임!!")
        kindofgame = stt.main()
        if kindofgame == '피하기':
            print("pihagi!!")
            os.system("python3 dodge.py")
        elif kindofgame == '벽돌':
            os.system("python3 brick.py")
        else:
            pass
    elif word == '날씨':
        pass

    print(word)
