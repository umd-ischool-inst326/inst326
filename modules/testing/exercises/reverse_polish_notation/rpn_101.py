from argparse import ArgumentParser
import sys


def evaluate(expr):
    expr = expr.rstrip()
    tokens = expr.split(" ")
    numbers = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            op2 = numbers.pop()
            op1 = numbers.pop()
            if token == "+":
                result = op1 + op2
            elif token == "-":
                result = op1 - op2
            elif token == "*":
                result = op1 * op2
            elif token == "/":
                result = op1 / op2
            numbers.append(result)
        else:
            numbers.append(float(token))
    return numbers[-1]


def main(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            result = evaluate(line)
            print(f"{line} = {result}")


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
