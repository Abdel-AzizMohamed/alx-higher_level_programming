#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args_length = len(sys.argv)
    if args_length != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    if op == "+":
        print("{:d} {:s} {:d} = {:d}".format(num1, op, num2, add(num1, num2)))
    elif op == "-":
        print("{:d} {:s} {:d} = {:d}".format(num1, op, num2, sub(num1, num2)))
    elif op == "*":
        print("{:d} {:s} {:d} = {:d}".format(num1, op, num2, mul(num1, num2)))
    elif op == "/":
        print("{:d} {:s} {:d} = {:d}".format(num1, op, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
