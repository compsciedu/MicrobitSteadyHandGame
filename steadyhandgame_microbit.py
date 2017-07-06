#Microbit Steady Hand Game
from microbit import *
wand_pin = pin0
buzzer = pin1
while True:
    buzzer.write_digital(0)
    display.show(Image.HAPPY)
    if wand_pin.is_touched():
        display.show(Image.SAD)
        buzzer.write_digital(1)
        sleep(100)
        
        