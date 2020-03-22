#!/usr/bin/env python
from datetime import * 
import sys 
import os
import convert_temp

#######################################
#           Main Loop                 #
#######################################
def main_loop():
    os.system('clear')
    print(' ')
    print('          Temperature Conversion   ')
    print(' ')
    print('     1.   Convert to Celsius   ')
    print(' ')
    print('     2.   Convert to Farenheight')
    print(' ')
    print('     99.  Exit')
    print(' ')
    option = input('        Enter option : ')

    if option == 1:    
        os.system('clear')  
        Cel = 0
        Far = 0
        float(Far)
        Far = input('Please enter the temperature in Farenheight: ')
        convert_temp.Far_to_Celcius(Far)
#        x = input(' ')
#        print(' ', x)
        
         
    elif option == 2:      
        os.system('clear')  
        Far = 0
        Cel = 0
        float(Cel)
        Cel = input('Please enter the temperature in Celsius: ')
        convert_temp.Celcius_to_Far(Cel)
#        x = input(' ')
#        print(' ', x)
                 
    elif  option == 99:
         
     
        os.system('clear')
        exit()

#######################################
#           Start of Program          #
#######################################
while True: 
    os.system('clear')
    main_loop()
    x = raw_input('Press Enter to continue')
    continue


