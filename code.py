import board
import digitalio
import time

# Button setup
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Pico onboard LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    if not button.value:
        print("Button Pressed")
        led.value = True
        time.sleep(0.5)
        led.value = False
    time.sleep(0.1)