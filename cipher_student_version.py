# HOMEWORK 4 --- ES2
# Caesar Cipher

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Hector Rivera
# NUMBER OF HOURS TO COMPLETE: 4
# YOUR COLLABORATION STATEMENT(s): While I didn't work with anyone, i did look for multiple sources of inspiration
#online and tried to follow many tutorials.
#
#
#*****************************************

# For this assignment you are going to implement a Caesar Cipher
# A Caesar cipher works by shifting every letter in the alphabet by a set amount.
# For example the string 'abc', with a shift of 1, would become 'bcd'
# For more information: https://en.wikipedia.org/wiki/Caesar_cipher

# Decode the following messages and say what shift you used to do so.
# 1. 'sn ad, nq mns sn ad: sgzs hr sgd ptdrshnm:'
# 2. 'sg2 wg am tojcfwhs qzogg'
# 3. 'nwcz akwzm ivl amdmv gmiza iow'

# ****************Answers****************
# 1.Message: TO BE or not to be: that is the question:
#   Shift Amt: 1
# 2.Message:  ES2 IS MY FAVORITE CLASS
#   Shift Amt: 12
# 3.Message: FOUR SCORE AND SEVEN YEARS AGO
#   Shift Amt: 18

# message: string to be encrypt
# shift: integer number of letters to shift by.
#   You can assume we will only test with integers between 0 and 25
#   However, you can write your function to work with negatives and numbers greater than 25 if you wish
import math
import time
message = input("What word or phrase would you like to encrypt today?:")
shift_amount = input("By what factor would you like to shift_amount your message today?")

def encrypt(message, shift_amount):
    string = ""
    if str.isdigit(shift_amount) == True:
        shift_amount = int(shift_amount)
        for i in message:
            t = ord(i)
            if t<= 65 and t <= 90:
                t = t + 34
            if t >= 97 and t <= 122:
                t = t + shift_amount
            if t > 122:
                t = 96 + (t - 122)
            string = string + chr(t)
    else:
        print ("Error, only digits are accepted ")
    return string
print(encrypt(message, shift_amount))
