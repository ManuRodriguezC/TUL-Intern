#!/usr/bin/python3
"""
    This program determines if the entered string is a palindrome or not.
    It receives three arguments:
    n: The size of the palindrome.
    k: The number of the changes.
    s = The palindrome
    Return the palindrome on success or -1 on failure.
"""

n = input("Enter the number of digits in the palindrome: ")
while int(n) < 0 or int(n) > 100000:
    n = input("The number must be greater than 0 and less than 100,000: ")

k = input("Enter the number of the changes in the palindrome: ")
while int(k) < 0 or int(k) > 100000:
    k = input("The changes must be greater than 0 and less than 100,000: ")

s = input("Enter the palindrome in numbers: ")
while int(n) != int(len(s)):
    s = input("The palindrome must be equal to the number of digits: ")

# Convert the string to a list and a reverse copy to loop through them in time
string = list(s)
changes = 0
left = 0
right = len(string) - 1

# Loop through both lists halfway.
while left < (int(n) / 2):
    """
    If there is a different value and the allowed changes have
    not been used, it changes them to be the same.
    """
    if string[left] != string[right] and changes < int(k):
        if string[left] > string[right]:
            string[right] = string[left]
        else:
            string[left] = string[right]
        changes += 1
    left += 1
    right -= 1
"""
This condition seeks to change the palindrome so that it is the
largest number in case it still contains possible changes.
"""
if changes < int(k):    
    left = 0
    right = len(string) - 1
    while left < (int(n) / 2) and changes < int(k):
        # If the value is different from 9 change it to 9
        if string[left] != 9:
            string[left] = "9"
            string[right] = "9"
            changes += 1
        left += 1
        right -= 1

palin = "".join(string)
# if it is a palindrome returnal palindrome is does not return -1
if palin == palin[::-1]:
    print(palin)
else:
    print("-1")
