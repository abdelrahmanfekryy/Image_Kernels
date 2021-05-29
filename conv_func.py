import numpy as np


def pad(img,p_x = 0, p_y =0):
    padded = np.zeros((img.shape[0] + 2*p_x,img.shape[1] + 2*p_y))
    padded[p_x:img.shape[0] + p_x,p_y:img.shape[1] + p_y] = img
    return padded


def convolution(img, kernel , stride =(1,1),dilation =(1,1),mode='valid'):
    if not (mode in ['valid','same','full']):
        raise ValueError('mode must be either "valid", "same" or "full"')

    if mode == 'full':
        p = [((img.shape[0] + kernel.shape[0] - 1)//stride[0] * stride[0] + kernel.shape[0] - img.shape[0])//2,
            ((img.shape[1] + kernel.shape[1] - 1)//stride[1] * stride[1] + kernel.shape[1] - img.shape[1])//2]   
        img = pad(img,p_x=p[0],p_y=p[1])

    elif mode == 'same':
        p = [((img.shape[0]//stride[0])* stride[0] + kernel.shape[0] - img.shape[0])//2,
            ((img.shape[1]//stride[0])* stride[1] + kernel.shape[1] - img.shape[1])//2]
        img = pad(img,p_x=p[0],p_y=p[1])

    output_shape = [(img.shape[0] - dilation[0]*(kernel.shape[0] - 1) - 1)//stride[0] + 1
                    ,(img.shape[1] - dilation[1]*(kernel.shape[1] - 1) - 1)//stride[1] + 1]
                    
    output = np.zeros(output_shape)
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i,j] = np.sum(img[i*stride[0]:i*stride[0] + kernel.shape[0],j*stride[1]:j*stride[1] + kernel.shape[1]] * kernel)

    return output




