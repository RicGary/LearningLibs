import easyocr
import keyboard
import pyautogui
import time, sys


def recognize_text(img_path):
    """Load and read text from images."""

    reader = easyocr.Reader(['pt'], gpu=False, verbose=False)
    return reader.readtext(img_path)


def Calibrating():
    """Function to calibrate screenshot coordinates."""

    print("Position your mouse on the corner shown and than press the required key.")

    print("Calibrating coordinates: top left")
    print("Press 'y' when ready:")
    while True:
        if keyboard.is_pressed('y'):
            mouse_position = pyautogui.position()
            with open('coordinates_top.txt', 'w') as coordinates:
                coordinates.write(f"dict(x={mouse_position[0]},y={mouse_position[1]})")
            break

    time.sleep(1)

    print("Calibrating coordinates: down right")
    print("Press 'y' when ready:")
    while True:
        if keyboard.is_pressed('y'):
            mouse_position = pyautogui.position()
            with open('coordinates_down.txt', 'w') as coordinates:
                coordinates.write(f"dict(x={mouse_position[0]},y={mouse_position[1]})")

            break


def ReturnDict(text):
    with open(text) as coord_dict:
        coords = coord_dict.read()
        return eval(coords)


def Screenshot():
    """Takes screenshot of a region."""

    coord_top = ReturnDict('coordinates_top.txt')
    coord_down = ReturnDict('coordinates_down.txt')

    height = coord_down['y'] - coord_top['y']
    width = coord_down['x'] - coord_top['x']

    left = coord_top['x']
    top = coord_top['y']

    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    return screenshot


def SusInAction():
    """Make Whatsapp sus."""

    word = input("What word you want to save? ")

    while True:
        try:
            img = Screenshot().save('img.jpg')
            text = recognize_text('img.jpg')[0][1].lower()
            if text == word:
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
        except:
            print('Not found')

        if keyboard.is_pressed('q'):
            print("Thanks for supporting!")
            time.sleep(2)
            import sys
            sys.exit()


def Instructions():
    """Print the readme.txt file and starts the code."""

    with open('readme.txt', encoding='utf-8') as readme:
        for line in readme.readlines():
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(0.1)

    calibrating = input("Do you want to calibrate?Press 'y' or 'n'")

    if calibrating == 'y':
        Calibrating()
        print("Calibration completed.")

    print("If you are ready to start, press 'y' once.")
    while True:
        if keyboard.is_pressed('y'):
            print("Initializing...")
            time.sleep(1)
            print("If want to end, press 'q'.")
            SusInAction()


Instructions()
