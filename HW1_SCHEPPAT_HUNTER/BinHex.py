# description: conversion of a decimal number to binary and hexadecimal
# author: SCHEPPAT, Hunter
# date: 9.7.2022

print("This program converts a decimal positive integer to both binary and hexadecimal")

# get the user's input as an in
first_num = int(input("Enter a positive integer: "))

# find the binary and hex values
binary_value = bin(first_num)
hex_value = hex(first_num)

# print the binary and hex values for the user
print("The decimal value of " + str(first_num) + " is:")
print(str(binary_value) + " in binary")
print(str(hex_value) + " in hexadecimal")













