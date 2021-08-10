from math import cos, radians, sin


class Car:
    """ A car that can drive and turn.
    
    Attributes:
        x (float): x coordinate.
        y (float): y coordinate.
        heading (float): direction to drive in, in degrees.
    """
    def __init__(self, x=0, y=0, heading=0):
        """ Initialize the object. """
        self.x = x
        self.y = y
        self.heading = heading
        
    def turn(self, degrees):
        """ Turn a number of degrees (positive or negative).
        
        Args:
            degrees (float): the number of degrees to turn.
            
        Side effects:
            Modifies self.heading.
        """
        self.heading = (self.heading + degrees) % 360
    
    def drive(self, distance):
        """ Drive the specified distance.
        
        Args:
            distance (float): a distance to drive.

        Side effects:
            Updates self.x and self.y.
        """
        self.x += sin(radians(self.heading)) * distance
        self.y -= cos(radians(self.heading)) * distance
    

def sanity_check():
    """ Test the Car class.
    
    Returns:
        Car: an instance of the Car class.
    
    Side effects:
        Writes to stdout.
    """
    c = Car()
    c.turn(90)
    c.drive(10)
    c.turn(30)
    c.drive(20)
    print(f"Location: {c.x}, {c.y}")
    print(f"Heading: {c.heading}")
    return c

if __name__ == "__main__":
    sanity_check()
