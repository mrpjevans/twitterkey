# twitterkey
Tweet using a Morse key - Tutorial for MagPi #92

Please see <https://magpi.raspberrypi.org/issues/92> for a full tutorial on how
to complete this project.

## Requirements

- Raspberry Pi (any model)
- Adafruit 16x2 LCD Pi Plate
- Morse code / telegraph key (optional)

This is a Python 3 project.

## Installation

To install all dependancies:

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
sudo pip3 install adafruit-circuitpython-charlcd
sudo pip3 install python-twitter
```

Clone this repo:

```bash
cd
git clone https://github.com/mrpjevans/twitterkey.git
cd twitterkey
```

## Starting

Morse code practice:

```
python3 lcd_morse.py
```

With Twitter capability:

```
python3 lcd_morse_twitter.py
```

## Using With Twitter

You need to have a Twitter developer account. (It's free) Then you must create an 'app' and get credentials for it

Instructions can be found here: <https://python-twitter.readthedocs.io/en/latest/>

You should end up with:

- Consumer Key
- Consumer Secret
- Application Token Key
- Application Token Secret

Once you have these, enter them into the corresponding variables at the start of `lcd_morse_twitter.py`.

## Controls

- Right: Morse key
- Up: Clear the current message
- Down: Space
- Left: Backspace 
- Select: Tweet (Twitter script only)

Have fun!

PJ


