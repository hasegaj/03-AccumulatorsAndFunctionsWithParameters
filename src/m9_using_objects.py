"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Josiah Hasegawa.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    point = rg.Point(93, 76)
    circle = rg.Circle(point, 67)
    circle.fill_color = 'green'

    pointl = rg.Point(100, 70)
    circle2 = rg.Circle(pointl, 55)

    circle.attach_to(window)
    circle2.attach_to(window)

    window.render()

    return
    # -------------------------------------------------------------------------
    # DO: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow()



    point_1 = rg.Point(100, 100)
    point_2 = rg.Point(40,40)
    point_3 = rg.Point(200,200)

    circle = rg.Circle(point_1, 50)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    rect = rg.Rectangle(point_2, point_3)
    rect.attach_to(window)
    merp = point_3.x - point_2.x
    derp = point_3.y - point_2.y
    dah = rg.Point(merp, derp)

    print(1)
    print(circle.fill_color)
    print(point_1)
    print(point_1.x)
    print(point_1.y)
    print(1)
    print('none')
    print(dah)
    print(merp)
    print(derp)


    window.render()
    return
    # -------------------------------------------------------------------------
    # DO: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow()

    p1 = rg.Point(200, 13)
    p2 = rg.Point(15, 40)
    p3 = rg.Point(194, 68)
    p4 = rg.Point(11, 91)
    line_1 = rg.Line(p1, p2)
    thicc_boy = rg.Line(p3, p4)
    thicc_boy.thickness = 10

    line_1.attach_to(window)
    thicc_boy.attach_to(window)

    print('midpoint of thicc boi')
    print(thicc_boy.get_midpoint())

    window.render()
    window.close_on_mouse_click()
    return
    # DO: 4. Implement and test this function.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
