"""Recursive graphics generation system based on Context Free principles.

This module provides classes for generating recursive graphics using Processing.
It allows for the creation of fractal-like patterns by defining rules and elements
that can be combined and transformed.
"""

import types, colorsys
from mekanigame.graphics.processing.processing import Processing
from mekanigame.utilities import radians
import random

# Element type constants
ADJUST = 0
CIRCLE = 1
SQUARE = 2
TRIANGLE = 3
RULE = 4

class Rule(object):
    """A rule that can be applied recursively to generate graphics.

    A Rule contains elements that can be other Rules, Elements, or dictionaries
    of transformation parameters that modify the rendering context.

    Args:
        parent (Rekurjon): The parent Rekurjon instance.
        elements (list): List of elements to apply when this rule is executed.
        x (float, optional): X-position offset. Defaults to 0.
        y (float, optional): Y-position offset. Defaults to 0.
        r (float, optional): Rotation in degrees. Defaults to 0.
        sx (float, optional): X-scale factor. Defaults to 1.
        sy (float, optional): Y-scale factor. Defaults to 1.
        h (float, optional): Hue adjustment. Defaults to 0.
        sat (float, optional): Saturation adjustment. Defaults to 0.
        b (float, optional): Brightness adjustment. Defaults to 0.
        a (float, optional): Alpha/transparency adjustment. Defaults to 0.
        n (int, optional): Number of iterations. Defaults to 100.
    """
    def __init__(self, parent, elements, x=0, y=0, r=0, sx=1, sy=1, h=0, sat=0, b=0, a=0, n=100):
        self.parent = parent
        self.elements = elements
        self.parent.elements.append(self)
        self.parameters = (x, y, r, sx, sy, h, sat, b, a)
        self.n = n
        self.type = RULE
        self.iter=0
        self.multi = len([x for x in elements if type(x) == types.DictionaryType]) > 1

    def apply(self, dict=None):
        """Apply this rule by executing all its elements.

        This method applies transformations and renders elements recursively.

        Args:
            dict (dict, optional): Dictionary of transformation parameters.
                Used for internal recursion. Defaults to None.

        Returns:
            None
        """
        if not self.parent.withinLimits():
            return

        for element in self.elements:
            if type(element) == types.DictionaryType :
                if self.multi:
                    if dict != element:
                        self.parent.p.pushMatrix()
                        self.parent.adjustState(**element)
                        self.apply(element)
                        self.parent.p.popMatrix()
                else:
                    self.parent.p.pushMatrix()
                    self.parent.adjustState(**element)
                    self.apply(element)
                    self.parent.p.popMatrix()


            elif type(element) == types.ListType:
                element = random.choice(element)
                self.parent.p.pushMatrix()
                element.apply()
                self.parent.p.popMatrix()
            else:
                element.apply()

        self.parent.p.popMatrix()

class Element(object):
    """A basic graphical element like a circle, square, or triangle.

    Elements are the basic building blocks for the recursive graphics system.

    Args:
        parent (Rekurjon): The parent Rekurjon instance.
        type (int): Element type constant (CIRCLE, SQUARE, etc.).
        x (float, optional): X-position offset. Defaults to 0.
        y (float, optional): Y-position offset. Defaults to 0.
        r (float, optional): Rotation in degrees. Defaults to 0.
        sx (float, optional): X-scale factor. Defaults to 1.
        sy (float, optional): Y-scale factor. Defaults to 1.
        h (float, optional): Hue adjustment. Defaults to 0.
        sat (float, optional): Saturation adjustment. Defaults to 0.
        b (float, optional): Brightness adjustment. Defaults to 0.
        a (float, optional): Alpha/transparency adjustment. Defaults to 0.
        n (int, optional): Number of repetitions. Defaults to 1.
    """
    def __init__(self, parent, type, x=0, y=0, r=0, sx=1, sy=1, h=0, sat=0, b=0, a=0, n=1):
        self.parent = parent
        self.type = type
        self.parameters = (x, y, r, sx, sy, h, sat, b, a)
        self.n = n
        self.dictDraw = {CIRCLE: self.parent.drawCircle, SQUARE: self.parent.drawSquare,
                      TRIANGLE: self.parent.drawTriangle, ADJUST: self.adjust}


    def __repr__(self):
        """Return string representation of the Element.

        Returns:
            str: String representation showing type and parameters.
        """
        print '%i, %s' %(self.type, str(self.parameters))

    def apply(self):
        """Apply this element by drawing it with the current transformation state.

        Returns:
            None
        """
        for i in range(self.n):
            if not self.parent.withinLimits():
                return
            self.parent.adjustState(*self.parameters)
            self.dictDraw[self.type]()

    def adjust(self):
        """Apply only state adjustments without drawing anything.

        Returns:
            None
        """
        pass

class Rekurjon(object):
    """Combines Python, Processing, and Context Free concepts for recursive graphics.

    This class serves as the main entry point for creating recursive graphics.
    It manages the drawing state, element creation, and rule application.

    Args:
        x (float, optional): Initial X position. Defaults to 1.
        y (float, optional): Initial Y position. Defaults to 1.
        r (float, optional): Initial rotation in degrees. Defaults to 0.
        sx (float, optional): Initial X-scale factor. Defaults to 1.
        sy (float, optional): Initial Y-scale factor. Defaults to 1.
        h (float, optional): Initial hue. Defaults to 0.
        sat (float, optional): Initial saturation. Defaults to 0.
        b (float, optional): Initial brightness. Defaults to 0.
        a (float, optional): Initial alpha/transparency. Defaults to 255.
        size (float, optional): Base size for elements. Defaults to 100.
        iterLimit (int, optional): Maximum iteration limit. Defaults to 900000.
        sizeLimit (float, optional): Minimum size limit before stopping recursion. Defaults to .00001.
    """
    def __init__(self, x=1, y=1, r=0, sx=1, sy=1, h=0, sat=0, b=0, a=255, size=100, iterLimit=900000, sizeLimit= .00001):
        self.sx = sx
        self.sy = sy
        self.h = h
        self.sat = sat
        self.b = b
        self.a = a
        self.angle = r
        self.p = Processing()
        self.parameters = (x, y, r, sx, sy, h, sat, b, a)
        self.gc = self.p.gc
        self.iter = 0
        self.allIter = 0
        self.size = size
        self.elements = [ ]
        self.iterFlag = True
        self.iterLimit = iterLimit
        self.sizeLimit = sizeLimit
        self.adjustState(*self.parameters)

    def withinLimits(self):
        """Check if the current transformation is within size limits.

        Returns:
            bool: True if within limits, False otherwise.
        """
        tm = self.gc.GetTransform().Get()
        return not(abs(tm[0]) < self.sizeLimit or abs(tm[3]) < self.sizeLimit)

    def containValue(self, attrib, tresh):
        """Constrain an attribute value between 0 and the threshold.

        Args:
            attrib (str): The attribute name to constrain.
            tresh (float): The maximum allowed value.

        Returns:
            None
        """
        val = getattr(self, attrib)
        if val > tresh:
            setattr(self, attrib, tresh)
        elif val < 0:
            setattr(self, attrib, 0)

    def adjustState(self, x=0, y=0, r=0, sx=1, sy=None, h=0, sat=0, b=0, a=0):
        """Adjust the current transformation and color state.

        Args:
            x (float, optional): X-position offset. Defaults to 0.
            y (float, optional): Y-position offset. Defaults to 0.
            r (float or list, optional): Rotation in degrees. Defaults to 0.
                If given as a list, a random value will be chosen.
            sx (float, optional): X-scale factor. Defaults to 1.
            sy (float, optional): Y-scale factor. Defaults to sy or sx if None.
            h (float, optional): Hue adjustment. Defaults to 0.
            sat (float, optional): Saturation adjustment. Defaults to 0.
            b (float, optional): Brightness adjustment. Defaults to 0.
            a (float, optional): Alpha/transparency adjustment. Defaults to 0.

        Returns:
            None
        """
        if type(r) == types.ListType:
            r = random.choice(r)
        self.p.translate(x*self.size, y*self.size)
        self.p.rotate(radians(r))
        self.p.scale(sx, sy)
        if h or sat or b or a:
            self.h += h
            self.sat += sat
            self.b += b
            self.a += a
            for x in [('h', 360), ('sat', 1), ('b', 1), ('a', 255)]:
                self.containValue(*x)
            r, g, b = [int(x*255) for x in colorsys.hsv_to_rgb(self.h, self.sat, self.b)]
            self.p.fill(r, g, b, 255)

    def run(self):
        """Execute all elements in the Rekurjon instance.

        This method runs through all elements three times for better randomization.

        Returns:
            None
        """
        for i in range(3):
            for elem in self.elements:
                if type(elem) == types.ListType:
                    elem = random.choice(elem)
                if elem.type == ADJUST:
                    elem.apply()
                elif elem.type == RULE:
                    self.p.pushMatrix()
                    elem.apply()
                    self.p.popMatrix()
                else:
                    self.p.pushMatrix()
                    elem.apply()
                    self.p.popMatrix()

    def adjust(self, x=0, y=0, r=0, sx=1, sy=1, h=0, sat=0, b=0, a=1, n=1):
        """Create an adjustment element.

        Args:
            x (float, optional): X-position offset. Defaults to 0.
            y (float, optional): Y-position offset. Defaults to 0.
            r (float, optional): Rotation in degrees. Defaults to 0.
            sx (float, optional): X-scale factor. Defaults to 1.
            sy (float, optional): Y-scale factor. Defaults to 1.
            h (float, optional): Hue adjustment. Defaults to 0.
            sat (float, optional): Saturation adjustment. Defaults to 0.
            b (float, optional): Brightness adjustment. Defaults to 0.
            a (float, optional): Alpha/transparency adjustment. Defaults to 1.
            n (int, optional): Number of repetitions. Defaults to 1.

        Returns:
            Element: An adjustment element.
        """
        return Element(self, ADJUST, x, y, r, sx, sy, h, sat, b, a, n)

    def circle(self, x=0, y=0, r=0, sx=1, sy=1, h=0, sat=0, b=0, a=1, n=1):
        """Create a circle element.

        Args:
            x (float, optional): X-position offset. Defaults to 0.
            y (float, optional): Y-position offset. Defaults to 0.
            r (float, optional): Rotation in degrees. Defaults to 0.
            sx (float, optional): X-scale factor. Defaults to 1.
            sy (float, optional): Y-scale factor. Defaults to 1.
            h (float, optional): Hue adjustment. Defaults to 0.
            sat (float, optional): Saturation adjustment. Defaults to 0.
            b (float, optional): Brightness adjustment. Defaults to 0.
            a (float, optional): Alpha/transparency adjustment. Defaults to 1.
            n (int, optional): Number of repetitions. Defaults to 1.

        Returns:
            Element: A circle element.
        """
        return Element(self, CIRCLE, x, y, r, sx, sy, h, sat, b, a, n)

    def square(self, x=0, y=0, r=0, sx=1, sy=1, h=0, sat=0, b=0, a=1, n=1):
        """Create a square element.

        Args:
            x (float, optional): X-position offset. Defaults to 0.
            y (float, optional): Y-position offset. Defaults to 0.
            r (float, optional): Rotation in degrees. Defaults to 0.
            sx (float, optional): X-scale factor. Defaults to 1.
            sy (float, optional): Y-scale factor. Defaults to 1.
            h (float, optional): Hue adjustment. Defaults to 0.
            sat (float, optional): Saturation adjustment. Defaults to 0.
            b (float, optional): Brightness adjustment. Defaults to 0.
            a (float, optional): Alpha/transparency adjustment. Defaults to 1.
            n (int, optional): Number of repetitions. Defaults to 1.

        Returns:
            Element: A square element.
        """
        return Element(self, SQUARE, x, y, r, sx, sy, h, sat, b, a, n)

    def triangle(self, x=0, y=0, r=0, sx=1, sy=1, h=0, sat=0, b=0, a=1, n=1):
        """Create a triangle element.

        Args:
            x (float, optional): X-position offset. Defaults to 0.
            y (float, optional): Y-position offset. Defaults to 0.
            r (float, optional): Rotation in degrees. Defaults to 0.
            sx (float, optional): X-scale factor. Defaults to 1.
            sy (float, optional): Y-scale factor. Defaults to 1.
            h (float, optional): Hue adjustment. Defaults to 0.
            sat (float, optional): Saturation adjustment. Defaults to 0.
            b (float, optional): Brightness adjustment. Defaults to 0.
            a (float, optional): Alpha/transparency adjustment. Defaults to 1.
            n (int, optional): Number of repetitions. Defaults to 1.

        Returns:
            Element: A triangle element.
        """
        return Element(self, TRIANGLE, x, y, r, sx, sy, h, sat, b, a, n)

    def drawCircle(self):
        """Draw a circle with the current transformation and color.

        Returns:
            None
        """
        self.iter += 1
        self.allIter += 1
        self.p.ellipse(-self.size/2, -self.size/2, self.size, self.size)

    def drawSquare(self):
        """Draw a square with the current transformation and color.

        Returns:
            None
        """
        self.iter += 1
        self.allIter += 1
        self.p.rect(-self.size/2, -self.size/2, self.size, self.size)

    def drawTriangle(self):
        """Draw a triangle with the current transformation and color.

        Returns:
            None
        """
        pass
