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
    for i in range( rows ):
        # loop through the rows of the image
        for j in range( cols):
            r, g, b = src.getPixel( cols, rows ) #this libe gets the value of the pixel at (cols, rows) returning 3 values
            src.setPixel( cols, rows, gr.color_rgb( b, g, r)) # set the value of the pixel at (cols, rows) to (b, g, r)

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
    # reduceRed( image )

    image.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)