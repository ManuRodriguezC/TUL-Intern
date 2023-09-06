# TUL-Intern

## Exercise 1 palindrome.

## Explanation

I selected this exercise because I find it fun and because it uses logic to determine and compare various positions of a piece of data and be able to control the changes depending on them, but at the same time it handles other variables such as the size and number of changes. .

To fix it, I first wanted the user or person running the code to be able to interact with the program and get excited about doing different tests and cases. But controlling and managing the data you enter. It then compares the positions from left to right, finding which of these is the greatest number and changing it, in this way, to form the highest-numbered palindrome. In the case of unused changes remaining after forming the palindrome, it is traversed again to convert it to the largest number. If the string happens to be a palindrome, it will return it; if not, it will return -1.

## Instructions

To run the program you must have python on your system.

Run `python --version` or `python3 --version` to check if you have python on your system.
If you don't have python in your system you can follow this tutorial https://en.wikihow.com/install-python to install it

Check with `python3 --version`

Files: 
- palin.py: This file contains the code for the palindrome program.

Run `./palin.py` to run the program in your terminal.

This program will request the necessary data to function:
- Number of digits of the palindrome.
- Number of changes allowed to convert the string into a palindrome if it is not.
- The string or palindrome to verify.

### Requirements
- The number of digits and the number of changes must be greater than 0 and less than 100,000 if it does not present an error and you must re-enter it.
- The number of digits must be equal to the size of the string entered, otherwise it will present an error and you must enter the string again.

If the string is a palindrome or can change some digits to be, it will return the palindrome, otherwise it will return -1.
Successful Palindrome
Failed -1

### Example

Run `./palin.py`

Successful

```
Enter the number of digits in the palindrome: 7
Enter the number of the changes in the palindrome: 3
Enter the palindrome in numbers: 6325123
6325236
```

Failed

```
Enter the number of digits in the palindrome: 7
Enter the number of the changes in the palindrome: 1
Enter the palindrome in numbers: 6325123
-1
```

Greater number.

```
Enter the number of digits in the palindrome: 7
Enter the number of the changes in the palindrome: 3   
Enter the palindrome in numbers: 1234371
9734379
```