import numpy as np

identical = np.array([[ 0, 0, 0],  
                    [ 0, 1, 0],  
                    [ 0, 0, 0]])

gaussian3x3 = 1/16 * np.array([[1, 2, 1],
                                [2, 4, 2],
                                [1, 2, 1]])


gaussian5x5 = 1/256 * np.array([[1, 4 ,  6,  4, 1],
                                [4, 16, 24, 16, 4],
                                [6, 24, 36, 24, 6],
                                [4, 16, 24, 16, 4],
                                [1, 4 ,  6,  4, 1]])

gaussian5x5T2 = 1/115 * np.array([[2, 4, 5, 4, 2],
                                  [4, 9,12, 9, 4],
                                  [5,12,15,12, 5],
                                  [4, 9,12, 9, 4],
                                  [2, 4, 5, 4, 2]])

laplacian3x3 = np.array([[ -1, -1, -1],  
                        [ -1,  8, -1],  
                        [ -1, -1, -1]])

laplacian5x5 = np.array([[ -1, -1, -1, -1, -1 ],  
                        [ -1, -1, -1, -1, -1 ],  
                        [ -1, -1, 24, -1, -1 ],  
                        [ -1, -1, -1, -1, -1 ],  
                        [ -1, -1, -1, -1, -1 ]])

emboss = np.array([[ -2, -1, 0],  
                    [ -1,  1, 1],  
                    [ 0, 1, 2]])

sharpen = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

laplacian = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]])


prewitt3x3H = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]])

prewitt3x3V = prewitt3x3H.T

kirsch3x3H = np.array([[ 5, 5, 5],
                        [-3, 0,-3],
                        [-3,-3,-3]])

kirsch3x3V = kirsch3x3H.T

sobel3x3R = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel3x3L = np.array([[ 1, 0, -1],
                    [ 2, 0, -2],
                    [ 1, 0, -1]])

sobel3x3T = np.array([[ 1, 2, 1],
                    [ 0, 0, 0],
                    [ -1, -2, -1]])

sobel3x3B = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])



kernel = [identical,emboss,sharpen,prewitt3x3V,prewitt3x3H,gaussian3x3,gaussian5x5,gaussian5x5T2,laplacian3x3,laplacian5x5,kirsch3x3H,kirsch3x3V,sobel3x3R,sobel3x3L,sobel3x3T,sobel3x3B]
kernelname = ['original','emboss','sharpen','prewitt3x3V','prewitt3x3H','gaussian3x3','gaussian5x5','gaussian5x5T2','laplacian3x3','laplacian5x5','kirsch3x3H','kirsch3x3V','sobel3x3R','sobel3x3L','sobel3x3T','sobel3x3B']