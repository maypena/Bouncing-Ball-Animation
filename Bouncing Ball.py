# May Pena
# This program creates a red moving ball that bounces
# frm the corners of the screen.

from graphics import *
from random import *

def main():
    win = GraphWin( "Lab 7 Moving ball", 600, 400 )

    # create and draw a red circle
    center = Point( 100, 100 )
    circ = Circle( center, 30 )
    circ.setFill( 'red' )
    circ.draw( win )

    # define the direction the circle will start moving in.
    # .10 pixels to the right every move, and .10 pixels down
    # every move.
    dx = .10
    dy = .10

    # as long as the mouse hasn't been clicked on the window
    # keep on looping.
    while win.checkMouse() == None:

        # move the circle in the current direction.
        circ.move( dx, dy )

        # get the x and y of the center of the circle.
        x = circ.getCenter().getX()
        y = circ.getCenter().getY()

        # if the center is outside the right or left boundary,
        # reverse the x direction of movement.
        if  x > 600:
            dx = -dx
        if  x < 0:
            dx = -dx
        if  y > 400:
            dy = -dy
        if  y < 0:
            dy = -dy

    
    # if we're here, it's because the the user clicked on the graphic window.
    # we can close everything and quit.
    win.close()

main()

