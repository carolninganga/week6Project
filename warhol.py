# Caroline Ninganga
# CS 5001
# Week6 Project
# 03/15/2021

import graphicsPlus as gr
import sys

#function named something like swapRedBlue that takes in one argument, which will be an Image object
def swapRedBlue( src ):
    rows = src.getHeight() # provides the number of rows in the image
    cols = src.getWidth() # provides the number of columns in the image 
    # loop through the rows of the image
    for row in range( rows ):
        # loop through the cols of the image
        for col in range( cols):
            r, g, b = src.getPixel( col, row ) #this line gets the value of the pixel at (cols, rows) returning 3 values
            src.setPixel( cols, rows, gr.color_rgb( b, g, r)) # set the value of the pixel at (cols, rows) to (b, g, r)

            #it is best to loop through the row in the outer loop because that is how the image is stored in the computers memory. It 

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
    swapRedBlue(clonedImage)


    # move the image so it is centered in the window
    image.move( cols/2, rows/2 )
    image.draw(win)

    # the move method centers the cloned image in the window and draw method draws to the window
    clonedImage.move( cols/2 + cols, rows/2 )
    clonedImage.draw(win)



 
    # reduceRed( image )


    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)