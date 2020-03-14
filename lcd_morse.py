#
# Morse code trainer
# PJ Evans <pj@mrpjevans.com>
# MIT Licence
#

import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

# Change these values (in seconds) to suit your style (or 'fist')
dash_timeout = 0.15
letter_threshold = 1

# Set up the LCD screen
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.color = [100, 0, 0]
lcd.clear()
lcd.home()
lcd.blink = True

# Track the key presses and generated morse
morse_key_pressed = False
morse_key_start_time = 0
morse_key_duration = 0
current_letter = ""
message = ""

# The morse alphabet as a dict
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

print('Ready')

try:

    while True:

        # If the key has been pressed
        if lcd.right_button:

            # Note the start time
            if not morse_key_pressed:
                morse_key_start_time = time.time()
                morse_key_pressed = True

        elif morse_key_pressed:

            # This triggers when the key is released
            morse_key_duration = time.time() - morse_key_start_time
            morse_key_pressed = False

            # From the duration, was it a dot or a dash?
            lcd.cursor_position (len(current_letter), 1)
            if morse_key_duration > dash_timeout:
                print('-', end='', flush=True)
                lcd.message = '-'
                current_letter += '-'
            else:
                print('.', end='', flush=True)
                lcd.message = '.'
                current_letter += '.'

        elif len(current_letter) > 0:

            # No activity but we're in the process of constructing a letter
            # After 1 second, match the letter
            time_since_last_release = time.time() -  (morse_key_start_time + morse_key_duration)
            if time_since_last_release > 1:
                lcd.cursor_position (len(message), 0)
                if current_letter in morse:
                    print(" " + morse[current_letter])
                    message +=  morse[current_letter]
                    lcd.message = morse[current_letter]
                else:
                    print(" ?")
                current_letter = ""
                lcd.cursor_position(0, 1)
                lcd.message = "                "
                lcd.cursor_position(len(message), 0)

        # Clear the message
        if lcd.up_button:
            message = ""
            current_letter = ""
            lcd.clear()
            time.sleep(0.2) # Debounce

        # Backspace
        if lcd.left_button and len(message) > 0:
            lcd.cursor_position(len(message) - 1 ,0)
            lcd.message = ' '
            message = message[:-1]
            lcd.cursor_position(len(message), 0)
            time.sleep(0.2) # Debounce

        # Add a space
        if lcd.down_button:
            lcd.cursor_position (len(message), 0)
            lcd.message = " "
            message += " "
            time.sleep(0.2) # Debounce
            
        # Let the CPU breathe
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stopping...")
    # Clean up
    lcd.display = False
    lcd.backlight = False
    lcd.clear()

    
