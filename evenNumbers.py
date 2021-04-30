# 10. Write a Python program to print the even numbers from a given list.
# https://www.w3resource.com/python-exercises/python-functions-exercises.php

Nlist = [1,2,3,4,5,6,7,8,9,12,31,45,56,78,99,101,120]
even_C, odd_C = 0,0
evens = []

# iterate through list
for n in Nlist:

    # check if even or odd
    if n % 2 == 0:
        even_C += 1
        evens.append(n)

    else: 
        odd_C += 1
# output 
print("Even numbers in the list: ", even_C)
print("Odd numbers in the list: ", odd_C)
print('The even numbers are: ' , evens)
