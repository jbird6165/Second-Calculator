'''This is my second attempt at a Calculator using better practices
it's not perfect but it's functional. I will continue to make updates as I learn.'''


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


def rt_equat(rt, op, num):
    '''This takes the sign entered i.e. "+ - * / =" and returns the appropriate equation'''
    if op == "+":
        rt += num
        return rt
    elif op == "-":
        rt -= num
        return rt
    elif op == "*":
        rt *= num
        return rt
    elif op == "/":
        rt /= num
        return rt


def computations(rt, op, ent):
    '''This is the loop that continues calculations until the "=" sign is entered.'''
    while True:
        if op != "=":
            num = number_input(input())
            rt = rt_equat(rt, op, num)
            ent.append(num)
            op = op_input(input())
            ent.append(op)
        else:
            if ent[1] == "=":
                print("Total: 0")
                ent.clear()
                rt = 0
                return
            else:
                print("Total: " + "" .join(str(x) for x in ent) + str(round(rt, 10)))    # I need to figure out how to remove the .0 when a float returns a .0
                ent.clear()                                                              # value. Haven't figured that out yet.
                rt = 0
            return


def zero_test(n):
    '''This tests the number to see if it's a 0. Will get a new number if it is.'''
    while True:
        if n == 0:
            n = number_input(input("Cannot Divide by 0. Please enter a valid #."))
        else:
            return n


entries = []
print("Welcome to Calculator 2.0.\n"
"You can add, subtract, multiply, and divide!")
while True:
    run_total = number_input(input())
    entries.append(run_total)
    operator = (op_input(input()))
    entries.append(operator)
    computations(run_total, operator, entries)
