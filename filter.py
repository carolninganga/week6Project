# Caroline Ninganga
# CS 5001
# Week6 Project
# 03/15/2021

import graphicsPlus as gr
import sys

#function named something like swapRedBlue that takes in one argument, which will be an Image object
def swapRedBlue( src ):
    rows = src.getHeight()
    cols = src.getWidth()
    # loop through the rows of the image
    for row in range( rows ):
        # loop through the rows of the image
        for col in range( cols):
            r, g, b = src.getPixel( col, row ) #this libe gets the value of the pixel at (cols, rows) returning 3 values
            src.setPixel( cols, rows, gr.color_rgb( b, g, r)) # set the value of the pixel at (cols, rows) to (b, g, r)

def reduceGreen( src ):
    rows = src.getHeight()
    cols = src.getWidth()
    for row in range(rows):
        for col in range(cols):
            # get the value of the pixel at (col, row)
            r, g, b = src.getPixel( col, row ) # this function returns 3 values
            # option1: rgb = red value is rgb[0], green value is rgb[1], blue value is rgb[2]
            # option2: r is red value, g is green value, b is the blue value
            # set the value of the pixel at (col, row) to halve the red value (integer division)
            src.setPixel( col, row, gr.color_rgb( r, g//2, b) )

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
    swapRedBlue(image)
    reduceGreen( image )

    image.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)