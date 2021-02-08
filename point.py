class Point:
    """Implement your Point class in here!"""
    def __init__ (self, x=0, y=0):
        self._x = float(x)
        self._y = float(y)
        
    def __repr__(self):
        return (f'x coordinate: {self._x}, y coordinate: {self._y}')

    def __str__(self):
        return f'a point ({self._x}, {self._y})'
    
    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)


if __name__ == '__main__':
    # This won't work until you finish implementing the Point class.
    origin = Point()
    point = Point(4, 1)
    other_point = Point(3, -3)
    third_point = point + other_point

    print(point)
    print(other_point)
    print(third_point)