#! python2
#Woradorn K.
import game
import matplotlib.animation as mpa
import matplotlib.pyplot as plt
import numpy as np
def animate(g, moveArr, fName):
    #Input: 
    #   g: Game state initialized the same way as on the recorded run
    #   moveArr: List of moves for the whole game
    #   fName: Output file name
    
    Writer = mpa.writers['ffmpeg']
    writer = Writer(fps=15)
    fig = plt.figure()
    plt.axis([0, g._gridSize[0], 0, g._gridSize[1]])
    im = []
    normSnek = np.vectorize(lambda v: (v/max(g.score,1) + 0.1) if v>0 else v)
    grid = normSnek(g.gameGrid)
    im.append([plt.imshow(grid, 
        interpolation='none', 
        origin='upper',
        extent = [0, g._gridSize[0], 0, g._gridSize[1]],
        cmap = 'seismic',
        vmin=-4, vmax=4)])
    #plt.show()
    for m in moveArr:
        #print('move: {}'.format(m))
        try:
            g.run(m)
        except Exception as e:
            break
        #plt.grid(True)
        normSnek = np.vectorize(lambda v: (v/max(g.score,1) + 0.1) if v>0 else v)
        grid = normSnek(g.gameGrid)
        im.append([plt.imshow(grid, 
            interpolation='none', 
            origin='upper',
            extent = [0, g._gridSize[0], 0, g._gridSize[1]],
            cmap = 'seismic',
            vmin=-4, vmax=4)])
        #plt.show()
    im_ani = mpa.ArtistAnimation(fig, im, interval=500, blit=True)
    #plt.grid(True)
    im_ani.save(fName)
    #plt.show()
    
