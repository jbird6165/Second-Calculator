import math
import classCalculator

cal = True
equation = classCalculator.equation()
run_tot = classCalculator.run_tot()




def float_try(n):
    try:
        return float(n)
    except ValueError:
        return False

def op_check(op, num, tot):
    if op == "+":
        return tot + num
    elif op == "-":
        return tot - num
    elif op == "*":
        return tot * num
    elif op == "/":
        if num == 0:
            return "Can't divide by 0."
        else:
            return tot / num
    elif op == "=":
        return


# def get_first_op(o):
#     if op == "+" or op == "-" or op == "*" or op == "/":




print("This calculator can add, subtract, multiply, and divide.")
while cal is True:
    first_num = True
    while first_num is True:
        attempt = float_try(input("Enter #: "))
        if attempt is False:
            print("Not a valid #.")
        else:
            run_tot = attempt
            equation.append(attempt)
            print("" .join(str(x) for x in equation))
            print(str(run_tot) + " = total test")         # test to see if running total is going up. Will need to remove.
            first_num = False
    first_op = True
    while first_op is True:
        op = input(" ")
        if op == "+" or op == "-" or op == "*" or op == "/":
            equation.append(op)
            print("".join(str(x) for x in equation))
            print(str(run_tot) + " = total test")  # test to see if running total is going up. Will need to remove.
            first_op = False
        elif op == "=":
            equation.append(op)
            print("".join(str(x) for x in equation) + " " + (str(round(run_tot, 10))))
            run_tot = 0
            first_num = True
    cal_loop = True
    while cal_loop is True:
        num_loop = True
        while num_loop is True:
            attempt = float_try(input("Enter #: "))
            if attempt is False:
                print("Not a valid #.")
            else:
                equation.append(attempt)
                op_check(equation[-2], equation[-1], run_tot)
                # run_tot += attempt
                print("".join(str(x) for x in equation))
                print(str(run_tot) + " = total test")  # test to see if running total is going up. Will need to remove.
                num_loop = False
        # op_loop = True
        # while op_loop is True:
        #     op = input(" ")
        # if op == "+" or op == "-" or op == "*" or op == "/":
        #     if op == "+":
        #     equation.append(op)
        #     print("".join(str(x) for x in equation))
        #     print(str(run_tot) + " = total test")  # test to see if running total is going up. Will need to remove.
        #     first_op = False
        # elif op == "=":
        #     equation.append(op)
        #     print("".join(str(x) for x in equation) + " " + (str(round(run_tot, 10))))
        #     run_tot = 0
        #     first_num = True
