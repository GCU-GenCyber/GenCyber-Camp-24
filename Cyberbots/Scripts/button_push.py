#Simple movement with button presses
from cyberbot import *
from microbit import *


while True:
    if button_a.is_pressed(): #This should make the bot go forwards
        bot(18).servo_speed(75)
    	  bot(19).servo_speed(-75)
        display.scroll("Wheeeee!")
    if button_b.is_pressed(): #This should make the bot go backwards
        bot(18).servo_speed(-75)
    	  bot(19).servo_speed(75)
        display.scroll("Woooooo!")
    else: #Bot doesn't move and asks for input
        bot(18).servo_speed(0)
    	  bot(19).servo_speed(0)
        display.scroll("Press any button.")
