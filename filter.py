# Caroline Ninganga
# CS 5001
# Week6 Project
# 03/15/2021

import graphicsPlus as gr
import sys

def swapRedBlue( src ):
    rows = src.getHeight()
    cols = src.getWidth()
    # loop through the rows of the image
    for i in range( rows ):
        # loop through the rows of the image
        for j in range( cols):
            r, g, b = src.getPixel( cols, rows ) #this libe gets the value of the pixel at (cols, rows) returning 3 values
            src.setPixel( cols, rows, gr.color_rgb( b, g, r)) # set the value of the pixel at (cols, rows) to (b, g, r)
