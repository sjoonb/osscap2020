import stt
import os
import time

def main():
    while(True):
        print('Game or Weather')
        word = stt.main()
        
        if word == '게임':
            # txt file time
            while(True):
                print("게임!!")
                kindofgame = stt.main()
                if kindofgame == '피하기':
                    print("pihagi!!")
                    mode = selectMode()
                    if mode:
                        print("mode!!", mode)
                        os.system("python3 dodge.py {0}".format(mode))
                elif kindofgame == '벽돌':
                    print("Byukdoll!!")
                    mode = selectMode()
                    if mode:
                        os.system("python3 brick.py {0}".format(mode))
                elif kindofgame == 'back':
                    print("뒤로")
                    break

                else:
                    pass

        elif word == '날씨':
            os.system("python3 weatherstation.py")


def selectMode():
    mode = stt.main()
    if mode == 'keyboard' or mode == 'mouse' or mode == 'sensor':
        return mode

    else:
        return None
   

if __name__ == "__main__":
    main()
