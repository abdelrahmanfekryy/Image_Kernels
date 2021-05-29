import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from kernels import *
from conv_func import * 

color = '#0066cc'
weight = 'bold'
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.facecolor'] = '#22222200'
plt.rcParams['axes.edgecolor'] = color
plt.rcParams['axes.labelcolor'] = color
plt.rcParams['axes.titlecolor'] = color
plt.rcParams['xtick.color'] = color
plt.rcParams['ytick.color'] = color
plt.rcParams['font.weight'] = weight
plt.rcParams['axes.labelweight'] = weight
plt.rcParams['axes.titleweight'] = weight


def Plot_Kernals(URL):
    image = plt.imread(URL)
    grayscale = np.mean(image,axis=-1)
   
    imgs_stack = []
    for k in kernel:
        img2 = np.clip(convolution(grayscale,k,stride=(1,1),mode = 'same'),0,255)
        img2 = np.repeat(np.expand_dims(img2,axis=-1),3,axis=-1).astype(int)
        imgs_stack.append(img2)

    fig = plt.figure()
    ax = plt.subplot2grid((15,15),(0,1), colspan=14, rowspan=15)
    ax.imshow(imgs_stack[0])
    ax.set_title('original')
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)


    dataSlider_ax = plt.subplot2grid((15,15),(0,0), colspan=1, rowspan=15,facecolor='lightgray')
    dataSlider = Slider(ax=dataSlider_ax,label='',valmin=0,valmax=len(kernel) - 1, valinit=0,valstep=1,orientation='vertical',visible = False)
    dataSlider.valtext.set_visible(False)
    dataSlider_ax.set_title('kernel')
    dataSlider_ax.set_yticks(range(len(kernel)))
    dataSlider_ax.set_yticklabels(kernelname)
    dataSlider_ax.yaxis.set_visible(True)
    idx = [dataSlider_ax.plot([0,20],[0,0],linewidth = 10,color=color)]


    def update(val):
        ax.clear()
        ax.imshow(imgs_stack[dataSlider.val])
        ax.set_title(kernelname[dataSlider.val])
        idx[0][0].remove()
        idx[0] = dataSlider_ax.plot([0,20],[dataSlider.val,dataSlider.val],linewidth = 10,color=color)
        fig.canvas.draw_idle()
        

    dataSlider.on_changed(update)

    fig.tight_layout()
    plt.show()