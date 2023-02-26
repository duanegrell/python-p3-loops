#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    if i == 0:
        print ("Happy New Year!")

# happy_new_year()


def square_integers(int_list):
    list_squared = [int * int for int in int_list]
    print (list_squared)
    return (list_squared)

# square_integers(int_list = [1, 2, 3, 4, 5])

def fizzbuzz():
    i = 1
    for i in range(1,101):
        if (i % 5) == 0 and (i % 3 == 0):
            print("FizzBuzz")
        elif (i % 5) == 0:
            print("Buzz")
        elif (i % 3) == 0:
            print("Fizz")
        else:
            print(i)


fizzbuzz()
