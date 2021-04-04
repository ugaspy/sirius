import keyboard
import time


def main():
    while True:

        if keyboard.is_pressed("space"):
            while True:
                time.sleep(0.00015)
                keyboard.press_and_release("space")
                time.sleep(0.030)


main()
                                                                                                                                                                                                                                                              