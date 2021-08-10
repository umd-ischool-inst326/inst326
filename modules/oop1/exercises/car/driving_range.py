""" A driving range for test-driving instances of the Car class. """

from math import cos, dist, radians, sin
import random
import tkinter as tk
from tkinter import ttk

from car import Car


# constants
CAR_RADIUS = 15
BORDER_WIDTH = 4
ARROW_WIDTH = 3
DRIVE_DISTANCE = 5
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800


class CanvasCar:
    """ Graphical representation of a car on the driving range.
    
    Attributes:
        car (Car): the car object.
        parent (DrivingRange): the widget containing the canvas.
        _self_driving (bool): whether or not the car should drive itself.
        car_obj (Canvas oval object): ID of the circle representing the car.
        orient_obj (Canvas line object): ID of the arrow representing the car's
            heading.
    """
    def __init__(self, parent, x=0, y=0, color="red", bordercolor="dark red",
                 arrowcolor="white", left_key="Left",
                 right_key="Right", drive_key="Up",
                 self_driving_key="Down",
                 self_driving=False):
        """ Initialize a new graphical representation of a car.

        Args:
            parent (DrivingRange): the widget containing the canvas.
            x (int, optional): The initial x coordinate. Defaults to 0.
            y (int, optional): The initial y coordinate. Defaults to 0.
            color (str, optional): the color of the circle. Defaults to "red".
            bordercolor (str, optional): the color of the border of the circle.
                Defaults to "dark red".
            arrowcolor (str, optional): the color of the arrow. Defaults to
                "white".
            left_key (str, optional): KeySym for counterclockwise turn.
                Defaults to "Left".
            right_key (str, optional): KeySym for clockwise turn. Defaults to
                "Right".
            drive_key (str, optional): KeySym to drive. Defaults to "Up".
            self_driving_key (str, optional): KeySym to toggle self-driving.
                Defaults to "Down".
            self_driving (bool, optional): If True, car will drive itself.
                Defaults to False.
        
        Side effects:
            Creates and animates objects on the parent widget's canvas.
            Binds events to the grandparent widget.
        """
        self.car = Car(x=x, y=y)
        self.parent = parent
        self._self_driving = self_driving
        canvas = self.parent.canvas

        self.car_obj = canvas.create_oval(-CAR_RADIUS, -CAR_RADIUS,
                                          CAR_RADIUS, CAR_RADIUS,
                                          fill=color, outline=bordercolor,
                                          width=BORDER_WIDTH)
        self.orient_obj = canvas.create_line(0, -CAR_RADIUS, 0, CAR_RADIUS,
                                             arrow=tk.FIRST, fill=arrowcolor,
                                             width=ARROW_WIDTH)
                
        self.parent.parent.bind(f"<KeyPress-{left_key}>",
                                lambda event: self.turn(-15))
        self.parent.parent.bind(f"<KeyPress-{right_key}>",
                                lambda event: self.turn(15))
        self.parent.parent.bind(f"<KeyPress-{drive_key}>",
                                lambda event: self.drive())
        self.parent.parent.bind(f"<KeyPress-{self_driving_key}>",
                                lambda event: self.toggle_self_driving())
        
        if self._self_driving:
            self.drive_self()
    
    @property
    def self_driving(self):
        """ Getter for self_driving attribute. """
        return self._self_driving
    
    @self_driving.setter
    def self_driving(self, new_value):
        """ Setter for self_driving attribute.
        
        Args:
            new_value (bool): new value for self_driving attribute.
        
        Raises:
            ValueError: new_value is not boolean.
        
        Side effects:
            Animates car; see drive_self().
        """
        if not isinstance(new_value, bool):
            raise ValueError("self_driving attribute must be boolean")
        self._self_driving = new_value
        if new_value:
            self.drive_self()

    def turn(self, degrees):
        """ Turn car.
        
        Args:
            degrees (float or int): number of degrees to turn car. Positive
                values are clockwise; negative values are counterclockwise.
        
        Side effects:
            Changes heading of car.
            Redraws car.
        """
        self.car.turn(degrees)
        self.update_car()
    
    def drive(self):
        """ Drive car forward, if possible.
        
        Side effects:
            Changes position of car.
            Redraws car.
            If the car is driving itself and an obstacle prevents the car from
                moving as specified, changes the car's heading 180 degrees.
        """
        canvas = self.parent.canvas
        # remember old coordinates, in case we can't drive where we wanted to
        old_x = self.car.x
        old_y = self.car.y
        self.car.drive(DRIVE_DISTANCE)
        
        # is car in bounds?
        in_bounds_x = (canvas.canvasx(0) + CAR_RADIUS <= self.car.x <=
                       canvas.canvasx(canvas.winfo_width()) - CAR_RADIUS)
        in_bounds_y = (canvas.canvasy(0) + CAR_RADIUS <= self.car.y <=
                       canvas.canvasy(canvas.winfo_width()) - CAR_RADIUS)

        # has car collided with another car?
        collision = self.parent.detect_collision(self)
        
        # draw car in new position or move back to old position
        if collision or not (in_bounds_x and in_bounds_y):
            self.car.x = old_x
            self.car.y = old_y
            if self._self_driving:
                self.car.turn(180)
        else:
            self.update_car()
    
    def update_car(self):
        """ Draw the car in its new location and heading.
        
        Side effects:
            Redraws car in a new location or heading.
        """
        canvas = self.parent.canvas
        # move the car
        canvas.coords(self.car_obj,
                      self.car.x-CAR_RADIUS, self.car.y-CAR_RADIUS,
                      self.car.x+CAR_RADIUS, self.car.y+CAR_RADIUS)
        
        # move the arrow
        dx = sin(radians(self.car.heading)) * CAR_RADIUS
        dy = -cos(radians(self.car.heading)) * CAR_RADIUS
        canvas.coords(self.orient_obj, self.car.x + dx, self.car.y + dy,
                      self.car.x - dx, self.car.y - dy)
    
    def toggle_self_driving(self):
        """ Toggle self-driving on or off. """
        self.self_driving = not self.self_driving
    
    def drive_self(self):
        """ Turn a random amount and attempt to drive.
        
        If the user has turned off self-driving since the last self-driving
        step, do nothing. Otherwise, schedule the next self-driving step.
        
        Side effects:
            Changes location and heading of car.
        """
        if not self._self_driving:
            return
        # favor slight turns most of the time, but allow turns as sharp as 45°.
        turn = (random.random() * 2 - 1) ** 3 * 45
        self.turn(turn)
        self.drive()
        # schedule next self-driving step
        self.parent.after(200, self.drive_self)


class DrivingRange(ttk.Frame):
    """ Main widget of the program. Contains a canvas on which cars are
    animated.
    
    Attributes:
        cars (list of CanvasCar): list of all CanvasCar objects.
        parent (widget): tkinter widget that contains this DrivingRange widget.
        canvas (tkinter.Canvas): canvas on which cars are animated.
    """
    def __init__(self, parent, *args, **kwargs):
        """ Initialize the DrivingRange widget.
        
        Args:
            parent (widget): the tkinter widget that contains this DrivingRange
                widget.
            *args, **kwargs: arguments to pass to Canvas widget.
        
        Side effects:
            Creates and populates a widget.
        """
        self.cars = []
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.canvas = tk.Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                                borderwidth=0, background="white")
        self.canvas.grid(column=0, row=0, sticky="nsew")

        self.canvas.configure(scrollregion=(-CANVAS_WIDTH/2, -CANVAS_HEIGHT/2,
                                            CANVAS_WIDTH/2, CANVAS_HEIGHT/2))
        self.canvas.xview_moveto(0.5)
        self.canvas.yview_moveto(0.5)
        
    def add_car(self, *args, **kwargs):
        """ Create a new CanvasCar. """
        self.cars.append(CanvasCar(self, *args, **kwargs))        
    
    def detect_collision(self, car):
        """ Determine whether car overlaps with any other car.
        
        Args:
            car (CanvasCar): car that may have collided with another.
        
        Returns:
            bool: True if a collision is detected between car and another car;
                otherwise False.
        """
        for other_car in self.cars:
            if car == other_car:
                continue
            d = dist((car.car.x, car.car.y), (other_car.car.x, other_car.car.y))
            if d < CAR_RADIUS * 2:
                return True
        return False


def main():
    """ Create the application. """
    root = tk.Tk()
    dr = DrivingRange(root)
    dr.grid(column=0, row=0, sticky="nsew")
    dr.add_car(x=-CAR_RADIUS, self_driving=True)
    dr.add_car(x=CAR_RADIUS, color="blue", bordercolor="dark blue",
               arrowcolor="yellow", left_key="a", right_key="d",
               drive_key="w", self_driving_key="s", self_driving=True)
    root.resizable(False, False)
    root.title("The driving range!")
    root.mainloop()


if __name__ == "__main__":
    main()
