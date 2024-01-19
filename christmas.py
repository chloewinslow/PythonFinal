import time
from pymata4 import pymata4

board = pymata4.Pymata4()

# Initializing LED and tilt sensor pins
LED1 = 4
LED2 = 3
LED3 = 2
PIN1 = 13
PIN2 = 12
PIN3 = 11


# Set up LED pin as OUTPUT and Shock pin as INPUT
board.set_pin_mode_digital_output(LED1)
board.set_pin_mode_digital_input(PIN1)

board.set_pin_mode_digital_output(LED2)
board.set_pin_mode_digital_input(PIN2)

board.set_pin_mode_digital_output(LED3)
board.set_pin_mode_digital_input(PIN3)



while True:
    # Reading the state of the shock sensor in a loop
    val1, timeOf1 = board.digital_read(PIN1) # Pin return 
    # Turn on or off the LED based on the shock sensor state
    if val1 == 0:
        board.digital_write(LED1, 1)
        time.sleep(0.1)
        board.digital_write(LED1, 0)


    # Reading the state of the shock sensor in a loop
    val2, timeOf2 = board.digital_read(PIN2) # Pin return 
    # Turn on or off the LED based on the shock sensor state
    if val2 == 0:
        board.digital_write(LED2, 1)
        time.sleep(0.1)
        board.digital_write(LED2, 0)


    # Reading the state of the shock sensor in a loop
    val3, timeOf3 = board.digital_read(PIN3) # Pin return 
    # Turn on the LED based on the shock sensor state
    if val3 == 0:
        board.digital_write(LED3, 1)
        time.sleep(0.1)
        board.digital_write(LED3, 0)


