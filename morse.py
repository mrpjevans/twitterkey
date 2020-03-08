from gpiozero import Button
import time

button = Button(21)  # GPIO Pin 40
dot_timeout = 0.15
dash_timeout = 1
current_letter = ""

morse = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
    ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
    "-----": "0"
}

while True:

    # Wait for a keypress or until a letter has been completed
    button.wait_for_press(dash_timeout)

    # If we've timed out and there's been previous keypresses, show the letter
    if button.is_pressed is False and len(current_letter) > 0:
        print("\nMorse: " + current_letter)
        if current_letter in morse:
            print("Letter: " + morse[current_letter])
        else:
            print("Not recognised")
        current_letter = ""

    elif button.is_pressed:

        # The key has been pressed, work out if it's a dot or a dash
        button_down_time = time.time()
        button.wait_for_release()
        button_up_time = time.time()
        button_down_length = button_up_time - button_down_time

        # Was it a dot or dash?
        if button_down_length > dot_timeout:
            print('-', end='', flush=True)
            current_letter += '-'
        else:
            print('.', end='', flush=True)
            current_letter += '.'

    time.sleep(0.1)
