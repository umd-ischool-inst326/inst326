from car import Car

def main():
    """ Try out the Car class. """
    c = Car()
    c.turn('l')
    c.drive(10)
    c.turn('l')
    c.drive()
    c.status()
    assert c.x == -10
    assert c.y == -1
    assert c.heading == "s"

if __name__ == "__main__":
    main()
