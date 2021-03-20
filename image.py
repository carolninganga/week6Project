
# Caroline Ninganga
# CS 5001 Spring 2021
# Project 6 
# First Image example

import sys
import graphicsPlus as gr

# the function swaprg switches the red and green values at every pixel
def swaprg( src ):
    rows = src.getHeight()
    cols = src.getWidth()
    for row in range(rows):
        for col in range(cols):
            # get the value of the pixel at (col, row)
            r, g, b = src.getPixel( col, row ) # this function returns 3 values
            # option1: rgb = red value is rgb[0], green value is rgb[1], blue value is rgb[2]
            # option2: r is red value, g is green value, b is the blue value
            # set the value of the pixel at (col, row) to (g, r, b)
            src.setPixel( col, row, gr.color_rgb( g, r, b ) )

def reduceRed( src ):
    rows = src.getHeight()
    cols = src.getWidth()
    for row in range(rows):
        for col in range(cols):
            # get the value of the pixel at (col, row)
            r, g, b = src.getPixel( col, row ) # this function returns 3 values
            # option1: rgb = red value is rgb[0], green value is rgb[1], blue value is rgb[2]
            # option2: r is red value, g is green value, b is the blue value
            # set the value of the pixel at (col, row) to halve the red value (integer division)
            src.setPixel( col, row, gr.color_rgb( r//2, g, b ) )

# read in an image and display in a window
def main( argv ):

    if len(argv) < 2:
        print("usage: python3 image.py <image filename>")
        return

    # read in the image from the filename specified on the command
    filename = argv[1]
    image = gr.Image( gr.Point(0, 0), filename )

    # create a window that is the same size as the image
    rows = image.getHeight()
    cols = image.getWidth()
    win = gr.GraphWin( filename, cols, rows )

    # move the image so it is centered in the window
    image.move( cols/2, rows/2 )

    # call the filter function before the image is drawn into a window
    reduceRed( image )

    image.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)



















