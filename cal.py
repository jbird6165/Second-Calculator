import math

#This is a test

def number_input(n):
    while False:
        try:
            float(n)
            return n
        except ValueError:
            n = print(input(("Not a Valid #.")))



def op_input(o):
    while False:
        l = ["+", "-", "*", "/", "="]
        for i in l:
            if i != l:
                o = print(input("Please enter + - * / or =."))
            elif i == l:


def plus(rt, op):

    return print("Plus")




run_total = number_input(input)

op = input()
if op == "+":