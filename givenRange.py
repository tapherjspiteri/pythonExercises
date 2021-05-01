# 6. Write a Python function to check whether a number is in a given range.
# https://www.w3resource.com/python-exercises/python-functions-exercises.php
# Thanks to Essence1337 on reddit for correcting my condition statement. See comments in code
target = input ("Enter a number between 1 and 500: ")
lower = 1
upper = 500

t = int(target)

def givenRange(n):
    if lower <= n <= upper:        # DOES NOT WORK --> n <= upper >= lower: 
        print ("Yes it is!")

    else: 
        print ("nope!")


givenRange(t)
