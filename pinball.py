import time
from pymata4 import pymata4
import vlc

# Create the board object
board = pymata4.Pymata4()

# Initialize LED and tilt sensor pins
PIN_TOP = 10
PIN_RIGHT = 11
PIN_LEFT = 12
PIN_END = 13

LED_TOP = 6
LED_LEFT = 5
LED_RIGHT = 4
LED_END = 3
PIN_MOTOR = 2

# Initialize input pins
board.set_pin_mode_digital_input(PIN_TOP)
board.set_pin_mode_digital_input(PIN_LEFT)
board.set_pin_mode_digital_input(PIN_RIGHT)
board.set_pin_mode_digital_input(PIN_END)

# Initialize output LEDs
board.set_pin_mode_digital_output(LED_TOP)
board.set_pin_mode_digital_output(LED_LEFT)
board.set_pin_mode_digital_output(LED_RIGHT)
board.set_pin_mode_digital_output(LED_END)
board.set_pin_mode_digital_output(PIN_MOTOR)

# Create sound output objects
womp = 'end.mp3'
ding = 'ding.mp3'
zap = 'zap.mp3'
wham = 'wham.mp3'
wompPlay = vlc.MediaPlayer(womp)
dingPlay = vlc.MediaPlayer(ding)
zapPlay = vlc.MediaPlayer(zap)
whamPlay = vlc.MediaPlayer(wham)

# Read the state of the sensors in a loop
while True:
    # Pin returns
    val1, blankTime = board.digital_read(PIN_TOP) 
    val2, blankTime = board.digital_read(PIN_LEFT)
    val3, blankTime = board.digital_read(PIN_RIGHT)
    valEnd, blankTime = board.digital_read(PIN_END)

    # Turn on or off the LED based on the shock sensor state
    if val1 == 0: # If the reading is 0 (it's been touched)
        board.digital_write(LED_TOP, 1) # Turn the LED on
        # Play designated sound, pause to let it play, stop sound
        whamPlay.play()
        time.sleep(1) # Pause the loop for 1 second, keeps the light on for 1 second
        board.digital_write(LED_TOP, 0) # Turn the LED back off
        whamPlay.stop() # Ensure sound stops
    if val2 == 0: # Same as previous loop, different input
        board.digital_write(LED_LEFT, 1)
        dingPlay.play()
        # Turn on motor for 2 seconds, new part of pinball machine moving
        board.digital_write(PIN_MOTOR, 1)
        time.sleep(1)
        board.digital_write(LED_LEFT, 0)
        dingPlay.stop()
        board.digital_write(PIN_MOTOR, 0)
    if val3 == 0: #Same as previous loops, different input
        board.digital_write(LED_RIGHT, 1)
        zapPlay.play()
        # Turn on motor for 2 seconds, new part of pinball machine moving
        board.digital_write(PIN_MOTOR, 1)
        time.sleep(1)
        board.digital_write(LED_RIGHT, 0)
        zapPlay.stop()
        board.digital_write(PIN_MOTOR, 0)
    if valEnd == 0: #Same as previous loops, different input and output
        board.digital_write(LED_END, 1)
        wompPlay.play()
        time.sleep(5)
        board.digital_write(LED_END, 0)
        wompPlay.stop()
