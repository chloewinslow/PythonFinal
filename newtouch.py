import time
from pymata4 import pymata4

# Create board object
board = pymata4.Pymata4()

# Initializing LED and tilt sensor pins
LED_PIN = 13
PIN = 8

# Set up LED pin as OUTPUT and Shock pin as INPUT
board.set_pin_mode_digital_output(LED_PIN)
board.set_pin_mode_digital_input(PIN)


while True:
    # Reading the state of the shock sensor in a loop
    val, timeOf = board.digital_read(PIN) # Pin return 
    print(val)
    # Turn on or off the LED based on the shock sensor state
    if val == 0:
        board.digital_write(LED_PIN, 1)
        time.sleep(1)
    board.digital_write(LED_PIN, 0)
    time.sleep(0.1)  # Add a small delay to avoid rapid state changes
