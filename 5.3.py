import time
import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

Morse_code = { 'A' : '.-' ,
               'B' : '-...' ,
               'C' : '-.-.' ,
               'D' : '-..' ,
               'E' : '.' ,
               'F' : '..-.' ,
               'G' : '--.' ,
               'H' : '....' ,
               'I' : '..' ,
               'J' : '.---' ,
               'K' : '-.-' ,
               'L' : '.-..' ,
               'M' : '--' ,
               'N' : '-.' ,
               'O' : '---' ,
               'P' : '.--.' ,
               'Q' : '--.-' ,
               'R' : '.-.' ,
               'S' : '...' ,
               'T' : '-' ,
               'U' : '..-' ,
               'V' : '...-' ,
               'W' : '.--' ,
               'X' : '-..-' ,
               'Y' : '-.--' ,
               'Z' : '--..' }

LED = 16
GPIO.setup(LED, GPIO.OUT)

win = Tk()
win.title(" Converter - MORSE_CODE")
Font = tkinter.font.Font( family = 'Helvertica', size = 14, weight = "bold")

def dot():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)

def dash():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)

def Convert_into_Morse():
    if len(value) > 12:
        print(" Name cannot be converted")
        win.destroy()
    value = INPUT.get()
    for letter in value:
        for sign in Morse_code[ letter.upper()]:
            if sign == '-':
                dash()
            elif sign == '.':
                dot()
            else:
                time.sleep(0.5)
        time.sleep(0.5) 

INPUT = Entry(win, font = Font, width = 20)
INPUT.grid(row = 0, column = 0)

Convert_button = Button(win, text = 'Convert', font = Font, command = lambda: Convert_into_Morse(inputName.get()), height = 2, width = 10)
Convert_button.grid( row =1, column = 0)

win.mainloop()
                



