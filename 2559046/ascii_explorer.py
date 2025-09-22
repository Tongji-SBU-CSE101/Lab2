# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:18:14 2025

@author: rosem
"""

print("=== ASCII Character Explorer ===")

letter = input("Enter a single character: ")
ascii_code = ord(letter) # ord() gets the ASCII code

print("The ASCII code of '" + letter + "' is: " + str(ascii_code))

print("\n--- Reverse Conversion ---")
code = int(input("Enter an ASCII code (try 65-90 for uppercase letters): "))
character = chr(code) # chr() converts code to character
print("ASCII code " + str(code) + " represents: '" + character + "'")


print("\n--- Fun Facts ---")
print("'A' = " + str(ord('A')))
print("'Z' = " + str(ord('Z')))
print("'a' = " + str(ord('a')))
print("'0' = " + str(ord('0')))


# The ASCII code for A is 65, the ASCII code for Z is 90
# Uppercase letters are ranged from 65-90 in the computer programming, and lowercase letters are further back in the numbering list. 
# No-- they represent spaces