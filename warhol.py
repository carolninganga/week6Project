# Caroline Ninganga
# CS 5001
# Week6 Project
# 03/15/2021

import graphicsPlus as gr
import filter   
import sys

def main( argv ):

    # check if the user input is correct in the command line
    if len(argv) < 2:
        print("usage: python3 image.py <image filename>")
        return

    # read in the image from the filename specified on the command
    filename = argv[1]
    image = gr.Image( gr.Point(0, 0), filename )

    # create a window that is the same size as the image
    rows = image.getHeight()
    cols = image.getWidth()
    win = gr.GraphWin( filename, cols*2, rows )
    clonedImage = image.clone()
    # call the filter function before the image is drawn into a window
    filter.swapRedBlue(clonedImage)


    # move the image so it is centered in the window
    image.move( cols/2, rows/2 )
    image.draw(win)

    # the move method centers the cloned image in the window and draw method draws to the window
    clonedImage.move( cols/2 + cols, rows/2 )
    clonedImage.draw(win)

    filter.reduceGreen( image )


    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)