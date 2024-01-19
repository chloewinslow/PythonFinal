import time
from pymata4 import pymata4

# Create board object
board = pymata4.Pymata4()

# Define LED pin
LED_OUTPUT_PIN = 3
LED_OUTPUT_PIN2 = 4

# Set LED pin state as digital output pin
board.set_pin_mode_digital_output(LED_OUTPUT_PIN)
board.set_pin_mode_digital_output(LED_OUTPUT_PIN2)

#Blink the LED while checking keyboard interrupts
while True:
    board.digital_write(LED_OUTPUT_PIN, 1)
    time.sleep(1)
    board.digital_write(LED_OUTPUT_PIN, 0)
    time.sleep(1)
    board.digital_write(LED_OUTPUT_PIN2, 1)
    time.sleep(1)
    board.digital_write(LED_OUTPUT_PIN2, 0)
    time.sleep(1)