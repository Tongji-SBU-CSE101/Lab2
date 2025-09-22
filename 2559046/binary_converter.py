# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:30:19 2025

@author: rosem
"""

print("=== Binary to Decimal Converter ===")
print("Enter a 4-bit binary number (each bit is 0 or 1)")

bit3 = int(input("Enter bit 3 (leftmost): "))
bit2 = int(input("Enter bit 2: "))
bit1 = int(input("Enter bit 1: "))
bit0 = int(input("Enter bit 3 (rightmost): "))

decimal = bit3 * 8 + bit2 * 4 + bit1 * 2 + bit0 * 1

print("\nBinary: " + str(bit3) + str(bit2) + str(bit1) + str(bit0))
print("Decimal: " + str(decimal))

 