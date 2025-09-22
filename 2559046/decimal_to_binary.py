# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:56:18 2025

@author: rosem
"""

print("=== Decimal to Binary Converter ===")
decimal = int(input("Enter a decimal number (0-15): "))
 
bit3 = decimal // 8
remainder = decimal % 8
bit2 = remainder // 4
remainder = remainder % 4
bit1 = remainder // 2
bit0 = remainder % 2 
  
print("\nDecimal: " + str(decimal))
print("Binary: " + str(bit3) + str(bit2) + str(bit1) + str(bit0))
  