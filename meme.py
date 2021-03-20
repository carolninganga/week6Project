#Caroline Ninganga
# CS 5001 Spring 2021
# Warhol style panels
#
# create a multi-panel window with a panel for each specified effect

import sys
import graphicsPlus as gr
import time

# this function takes in a list as a parameter and return a GraphWin window object
def memeGenerator( filename, listOfEffects ):

    # read the image from the file
    original = gr.Image( gr.Point(0, 0), filename )

    rows = original.getHeight()
    cols = original.getWidth()
    panels = len(listOfEffects)

    # create a window based on the image and how many copies
    win = gr.GraphWin( 'memeGenerator', cols*panels, rows )
    allimages = []

    # for each effect
    for i in range(panels):
        # clone the original image
        clone = original.clone() # duplicates the Image object
        # apply the filter to the clone, which filter to apply?
        if listOfEffects[i] == 'swaprg': 
            image.swaprg( clone )
        elif listOfEffects[i] == 'reduceRed':
            image.reduceRed( clone )
        # implied else don't do anything
        
        # move the image to the right location
        clone.move( cols/2 + i*cols , rows/2 )
        # draw the image into the window
        clone.draw(win)
        allimages.append( clone )

        # create some text
        sometext = gr.Text( gr.Point( cols/2, rows/2+30 ), "flowers" ) #The Text constructor takes a Point object as the first argument and the string to draw as the second argument. For example: gr.Text( gr.Point( x, y ), 'some text' ).  
        sometext.setFill('red') # Color using its setFill method. 
        sometext.setSize( 20 ) # Control the size of the text using its setSize method
        sometext.draw(win) # Draw the text into the window in order to see it. 
        # Centered the text on the specified point

    # return the window
    return win, allimages

def main( argv ):

    if len(argv) < 3:
        print('usage: python3 warhol.py <image filename> <effect: swaprg | reduceRed | org>')
        return

    filename = argv[1]
    listOfEffects = argv[2:] # the remaining strings
    win, allimages = warhol( filename, listOfEffects )

    frame = 0
    while True:
        if frame % 20 == 0:
            allimages[0].move( 0, -5 )
        elif frame % 20 == 10:
            allimages[0].move( 0, 5 )
        frame += 1

        if win.checkMouse() != None: 
            break

        time.sleep(0.05) # use the imported time to control when it sleeps 

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main( sys.argv )











