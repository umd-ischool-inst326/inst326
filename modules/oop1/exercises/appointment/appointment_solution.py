class Appointment:
    """ Models an appointment.
    
    Attributes:
        name (str): a name for the appointment.
        start (tuple of int, int): start time for the appointment. The
            first integer is the hour in 24-hour time; the second
            integer is the minutes.
        end (tuple of int, int): end time for the appointment. This
            parameter uses the same format as start.
    """
    def __init__(self, name, start, end):
        """ Initialize the object. """
        self.name = name
        self.start = start
        self.end = end
    
    def overlaps(self, other):
        """ Determine whether this appointment overlaps with other.
        
        Args:
            other (Appointment): appointment that may overlap with self.
            
        Returns:
            bool: True if self and other overlap, otherwise False.
        """
        return (self.start <= other.start < self.end
                or other.start <= self.start < other.end
                or self.start <= other.end < self.end
                or other.start <= self.end < other.end)