# TUL-Intern

## Exercise 1 palindrome.

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
Enter the number of the changes in the palindrome:
Enter the palindrome in numbers: 6325123
-1
```