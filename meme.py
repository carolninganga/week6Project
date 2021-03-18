# Bruce Maxwell
# CS 5001 Spring 2021
# Warhol style panels
#
# create a multi-panel window with a panel for each specified effect

import sys
import graphicsPlus as gr
import image  # contains the filters
import time

# should create a graphWin window, insert an image for each effect (left to right)
# should return the window
def warhol( filename, listOfEffects ):

    # read the image from the file
    original = gr.Image( gr.Point(0, 0), filename )

    rows = original.getHeight()
    cols = original.getWidth()
    panels = len(listOfEffects)

    # create a window based on the image and how many copies
    win = gr.GraphWin( 'Warhol', cols*panels, rows )
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
        sometext = gr.Text( gr.Point( cols/2, rows/2+30 ), "Aaaaargh" )
        sometext.setFill('red')
        sometext.setSize( 20 )
        sometext.draw(win)

        # create an eye patch
        patch = gr.Circle( gr.Point( cols/2-15, rows/2-30 ), 8 )
        patch.setFill( 'black' )
        patch.draw(win)

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

        time.sleep(0.05)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main( sys.argv )











