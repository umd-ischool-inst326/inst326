from argparse import ArgumentParser
import sys


def evaluate(expression):
    """ Evaluate a postfix expression and return the result.
    
    The following operators are permitted: + - * /. All operators take two
    operands.
    
    Args:
        expression (str): a postfix expression.
    
    Returns:
        float: the result of the expression.
    """
    expression = expression.strip()
    stack = []
    for token in expression.split(" "):
        if token in ["+", "-", "*", "/"]:
            value2 = stack.pop()
            value1 = stack.pop()
            if token == "+":
                result = value1 + value2
            elif token == "-":
                result = value1 - value2
            elif token == "*":
                result = value1 * value2
            elif token == "/":
                result = value1 / value2
            stack.append(result)
        else:
            stack.append(float(token))
    return stack[0]


def main(filepath):
    """ Read postfix expressions from a file, evaluate each one, and print the
    result.
    
    Args:
        filepath (str): path to a text file containing one expression per line.
    
    Side effects:
        Writes to stdout.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
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
