""" Read orders from a file and calculate the total cost of an order.
Each line in an order file will consist of a product name, a quantity, and a
unit price, separated by commas. """


def process_line(line):
    """ Parse a line from an order file; print information about the line;
    return the cost of this line of the order.
    
    Args:
        line (str): one line from the order file; contains product name,
            quantity ordered, and unit price, separated by commas.
    
    Returns:
        float: the cost of this line (quantity * unit price).
    
    Side effects:
        Writes information about this line to stdout.
    """
    values = line.strip().split(",")
    product = values[0]
    quantity = int(values[1])
    unit_price = float(values[2])
    ending = "" if quantity == 1 else "s"
    line_cost = quantity * unit_price
    print(f"{quantity} {product}{ending} @ ${unit_price}: {line_cost}")
    return line_cost


def total_cost(filepath):
    """ Read an order and calculate the total cost.
    
    Args:
        filepath (str): order file containing one item ordered per line
            (product name, quantity, unit cost).
    
    Side effects:
        Writes the total cost to stdout.
    """
    total = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            total += process_line(line)
    print(f"Total cost: ${total}")


total_cost("order.txt")
