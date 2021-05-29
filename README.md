<!--Open Preview (Ctrl+Shift+V)-->
# Image Kernals:


## Table of Contents
* [Description](#description-)
* [Dependencies](#dependencies-)
* [Operations](#operations)
* [Usage Example](#usage-example-)
* [References](#references-)

## Description :
implementation of different image filters using a wide variety of kernals under convolution process

## Dependencies :
* [Numpy](http://www.numpy.org/)
* [Matplotlib](https://matplotlib.org/)

## Operations :

*All Figures renderd using* `Plot_Kernals`

### Identity
--------------------------
<img src='Images/Figure_1.png' width = 500/>

### embossing
--------------------------

<img src='Images/Figure_2.png' width = 500/>

### sharpening
--------------------------

<img src='Images/Figure_3.png' width = 500/>

--------------------------

### Gaussian blur (aka. Gaussian smoothing)


<img src='Images/Figure_6.png' width = 500/>
<img src='Images/Figure_7.png' width = 500/>
<img src='Images/Figure_8.png' width = 500/>

-------------------------------------

### Edge detection

<img src='Images/Figure_9.png' width = 500/>
<img src='Images/Figure_10.png' width = 500/>
<img src='Images/Figure_11.png' width = 500/>
<img src='Images/Figure_12.png' width = 500/>
<img src='Images/Figure_13.png' width = 500/>
<img src='Images/Figure_14.png' width = 500/>
<img src='Images/Figure_15.png' width = 500/>
<img src='Images/Figure_16.png' width = 500/>
<img src='Images/Figure_4.png' width = 500/>
<img src='Images/Figure_5.png' width = 500/>


## Usage Example :
```python
import os
from plot_assest import Plot_Kernals

dir_path = os.path.dirname(os.path.realpath(__file__))

Plot_Kernals(dir_path + '/Images/monarch.jpg')
```


## References :
- **[wikipedia](https://en.wikipedia.org/wiki/Kernel_(image_processing))**
