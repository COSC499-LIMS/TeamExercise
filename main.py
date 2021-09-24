import math
user_input  = input("enter your string: ")


def first_half(input):
    end = math.floor(len(input)/2)
    print(input[0:end])

first_half(user_input)