import operator

'''This is my second attempt at a Calculator using better practices
it's not perfect but it's functional. I will continue to make updates as I learn.'''

#New pull request so you can read it easier.
def Calculator():
    '''This is the loop that continues calculations until the "=" sign is entered.'''
    ent = []
    rt = 0
    op = None
    while True:
        num = number_input(input())
        ent.append(num)
        rt = rt_equat(rt, op, num, ent)
        op = op_input(input())
        ent.append(op)
        if op == "=":
            total(rt, ent)
            return


def total(rt, ent):
    if ent[1] == "=":
        print(ent[0])
    else:
        print("Total: " + " " .join(str(x) for x in ent) + " " + str(round(rt, 10)))    # I need to figure out how to remove the .0 when a float returns a .0
    ent.clear()
    return


def number_input(n):
    '''This will float the input and request input again if error occurs'''
    while True:
        try:
            return float(n)
        except ValueError:
            n = input("Not a Valid #. Pleae enter a valid #:")


def op_input(o):
    '''This tests operator input and requests new input if operator was not accurate'''
    while True:
        l = ["+", "-", "*", "/", "="]
        for i in l:
            if o == i:
                return o
        o = input("Please enter + - * / or =:")


def rt_equat(rt, op, num, ent):
    '''This takes the sign entered i.e. "+ - * / =" and returns the appropriate equation'''
    if op == "+":
        rt = operator.add(rt, num)
        return rt
    elif op == "-":
        rt = operator.sub(rt, num)
        return
    elif op == "*":
        rt = operator.mul(rt, num)
        return rt
    elif op == "/":
        num = zero_test(num, ent)
        rt = operator.truediv(rt, num)
        return rt
    elif op == None:
        rt = operator.add(rt, num)
        return rt


def zero_test(num, ent):
    '''This tests the number to see if it's a 0. Will get a new number if it is.'''
    while True:
        if num == 0:
            ent.pop()
            num = number_input(input("Cannot Divide by 0. Please enter a valid #."))
            ent.append(num)
        else:
            return num



print("Welcome to Calculator 2.0.\nYou can add, subtract, multiply, and divide!")
while True:
    Calculator()
