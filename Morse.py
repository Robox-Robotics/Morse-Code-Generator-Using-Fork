# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:37:42 2021

@author: Anirudha Gaikwad
"""
import time
from forkapi.fork import Fork

myFork = Fork('192.168.0.205')

time_unit = 0.2
value_dash = 3*time_unit
value_idle = 1*time_unit
value_space = 3*time_unit
value_words = 7*time_unit

def morse(txt):
    encrypt = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'.....'}
    decrypt = {v: k for k, v in encrypt.items()}
    
    if '-' in txt:
        return ''.join(decrypt[i] for i in txt.split())
    return ' '.join(encrypt[i] for i in txt.upper())

def convert_morse_to_LED(morse_code):
    for i in range(len(morse_code)):
        print(morse_code[i],end ="")
        if(morse_code[i] == '.'):
            
            status = myFork.aoSet(0,10)
            time.sleep(time_unit)
            status = myFork.aoSet(0,0)
            time.sleep(value_idle)
        elif(morse_code[i] == '-'):
                status = myFork.aoSet(0,10)
                time.sleep(value_dash)
                status = myFork.aoSet(0,0)
                time.sleep(value_idle)
    return
        
def Relay_init():
    status = myFork.aoSet(1,10)
    if(status):
        return "Relay init successful"
    else:
        return "Relay init unsuccessful"

print(Relay_init())
while True:
    
    morse_value = morse("Hello World")
    convert_morse_to_LED(morse_value)
    print(morse_value)
    print("Done printing the text")
    time.sleep(1)