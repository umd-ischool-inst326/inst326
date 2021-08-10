from argparse import ArgumentParser
import sys


def evaluate(expr):
    operands = []
    tokens = expr.strip().split(" ")
    for token in tokens:
        try:
            operands.append(float(token))
        except ValueError:
            num2 = operands.pop()
            num1 = operands.pop()
            if token == "+":
                result = num1 + num2
            elif token == "-":
                result = num1 - num2
            elif token == "*":
                result = num1 * num2
            elif token == "/":
                result = num1 / num2
            operands.append(result)
    return operands.pop()


def main(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            result = evaluate(line)
            print(f"{line.strip()} = {result}")


def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
