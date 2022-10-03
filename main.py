import pyautogui
from time import sleep
import argparse

def __main__():
    # parse arguments
    #get sleep time, xbound, yPos, xPos 
    argpaser = argparse.ArgumentParser()
    argpaser.add_argument("-s", "--sleep", help="sleep time", type=int, default=2.5)
    argpaser.add_argument("-x", "--xbound", help="x bound", type=int, default=100)
    argpaser.add_argument("-ypos", "--ypos", help="y bound", type=int, default=1900)
    argpaser.add_argument("-xpos", "--xpos", help="x position", type=int, default=100)
    args = argpaser.parse_args()

    while True:
        if(pyautogui.position().x > args.xbound):
            pyautogui.moveTo(args.xpos, args.ypos)
            pyautogui.click()
        sleep(args.sleep)

if __name__ == "__main__":
    __main__()