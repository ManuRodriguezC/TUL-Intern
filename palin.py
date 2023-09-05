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
while int(k) < 0 or int(n) > 100000:
    n = input("The changes must be greater than 0 and less than 100,000: ")

s = input("Enter the palindrome in numbers: ")
while int(n) != int(len(s)):
    s = input("The palindrome must be equal to the number of digits: ")

# Convert the string to a list and a reverse copy to loop through them in time
string = list(s)
s_rev = list(s[::-1])
changes = 0
position = 0

# Loop through both lists halfway.
while position < (int(n) / 2):
    """
    If there is a different value and the allowed changes have
    not been used, it changes them to be the same.
    """
    if string[position] != s_rev[position] and changes < int(k):
        s_rev[position] = string[position]
        changes += 1
    position += 1

palin = "".join(s_rev)
# if it is a palindrome returnal palindrome is does not return -1
if palin == palin[::-1]:
    print(palin)
else:
    print("-1")
