"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Raymond Becerra.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
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

    p1 = rg.Point(200, 50)
    c = rg.Circle(p1,25)
    c.fill_color = 'blue'
    c.outline_color = 'red'
    c.attach_to(window)

    p2 = rg.Point(100,75)
    d = rg.Circle(p2,30)
    d.outline_color = 'purple'
    d.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
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

    x = 200
    y = 100
    p3 = rg.Point(x,y)
    f = rg.Circle(p3,20)
    f.outline_thickness = '15'
    t = f.outline_thickness
    f.fill_color = 'blue'
    a = f.fill_color
    print(t)
    print(a)
    print(p3)
    print(x)
    print(y)
    f.attach_to(window)

    w = rg.Point(50,50)
    p = rg.Point(100,100)
    g = rg.Rectangle(w,p)
    g.outline_thickness = 10
    h = g.outline_thickness
    print(h)
    print(w,p)
    print(w)
    print(p)
    g.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
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

    p4 = rg.Point(20,100)
    p5 = rg.Point(100, 20)
    L = rg.Line(p4,p5)
    L.color = 'red'
    o = L.get_midpoint()
    print(o)
    print(o.x)
    print(o.y)
    L.attach_to(window)

    p6 = rg.Point(50,150)
    p7 = rg.Point(150,50)
    j = rg.Line(p6, p7)
    j.color = 'blue'
    j.thickness = 15
    q = j.get_midpoint()
    print(q)
    print(q.x)
    print(q.y)
    j.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
