""" basic geometry classes to describe canvas points """
import math
from typing import Self

# tolerance on coordinates within which two points are considered equal
COORD_TOLERANCE = 0.000_001


class Canvas:
    """ representation of a rectangular drawing area
    with the origin (0,0) in the top left corner """
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Canvas(width={self.width}, height={self.height})"

    def __contains__(self, item) -> bool:
        """ check whether the item is contained within the canvas"""
        if isinstance(item, Vector):
            if (item.x < 0 or item.x > self.width or
                item.y < 0 or item.y > self.height):
                return False
            return True
        raise TypeError(f"__contains__ not defined for type '{type(item)}'")


class Vector:
    """ a vector (or point) within a canvas """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        """ two points are equal, if their coordinates are equal within COORD_TOLERANCE """
        if not isinstance(other, Vector):
            raise TypeError("Can only compare with another CanvasPoint instance")
        return (math.fabs(self.x - other.x) < COORD_TOLERANCE and
                math.fabs(self.y - other.y) < COORD_TOLERANCE)

    def __add__(self, other) -> Self:
        """ component-wise addition with another vector """
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> Self:
        """ component-wise subtraction with another vector """
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> Self:
        """ scalar multiplication with an integer or float value """
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Vector(other * self.x, other * self.y)

    def __rmul__(self, other) -> Self:
        """ (see __mul__)"""
        return self.__mul__(other=other)

    def __truediv__(self, other) -> Self:
        """ (see __mul__)"""
        factor = 1/other
        return self.__mul__(other=factor)

    def __rtruediv__(self, other) -> Self:
        """ dividing a value by a vector is not possible """
        return NotImplemented

    @property
    def mag(self) -> float:
        """ the vector magnitude (length) according to the euclidian norm """
        norm = math.sqrt(self.x**2 + self.y**2)
        return norm

    def normalized(self) -> Self:
        """ return a normalized version of the vector
        the initial_point will be the origin (0, 0) and the magnitude will be 1
        :raises ZeroDivisionError if the vector has magnitude zero
        """
        if self.mag == 0:
            raise ZeroDivisionError("Can not normalize a vector of magnitude 0")
        return self / self.mag

    def orthogonal(self, ccw: bool = False) -> Self:
        """ return a normalized vector that points in the (counter)clockwise
        orthogonal direction from this vector
        :argument ccw if True rotate counterclockwise, otherwise clockwise
        :raises ZeroDivisionError if the vector has magnitude zero
        """
        if self.mag == 0:
            raise ZeroDivisionError("Can not normalize a vector of magnitude 0")
        norm = self.normalized()
        if ccw:
            return Vector(norm.y, -norm.x)
        return Vector(-norm.y, norm.x)


ORIGIN = Vector(0, 0)
