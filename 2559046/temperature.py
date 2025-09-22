# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:36:16 2025

@author: rosem
"""

print ("=== Temperature Converter ===")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Formula: C = (F - 32) x 5/9
celsius = (fahrenheit - 32) * 5 / 9

print(str(fahrenheit) + "F = " + str(celsius) + "C")

# Bonus: add the reverse conversion! 
print("\n--- Celsius to Fahrenheit ---")
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_result = celsius_input * 9 / 5 + 32
print(str(celsius_input) + "C= " + str(fahrenheit_result) + "F")
