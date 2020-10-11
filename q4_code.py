import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def Gaussian_Model(sigma,point):
    x, y = point
    ratio = 1/(2*math.pi*sigma**2)
    e_part = math.exp(-(x**2+y**2)/(2*sigma**2))
    return ratio * e_part
    
def Gaussian_Blur(sigma,kernel_size):
    half_kernel = (kernel_size-1) // 2
    matrix = []
    Gaussian_matrix = []
    for i in range(kernel_size):
        matrix.append([])
        Gaussian_matrix.append([])
        for j in range(kernel_size):
            matrix[i].append((j-half_kernel,half_kernel-i))
            Gaussian_matrix[i].append(Gaussian_Model(sigma,matrix[i][j]))
    print(Gaussian_matrix)
    return Gaussian_matrix
    
def convolution(matrix,x,y,src):
    x_length, y_length = src.shape
    kernel_size = len(matrix)
    count_u = 0
    res = 0
    start = int(-(kernel_size-1)/2)
    end = int((kernel_size-1)/2 + 1)
    for u in range(start,end):
        count_v = 0
        for v in range(start,end):
            if(x-u<0 or y-v<0 or x-u>=x_length or y-v>=y_length): res += 0
            else: res += src[x-u][y-v] * matrix[count_u][count_v]
            count_v += 1
        count_u += 1
    return res
    
def Sobel_Operation(src):
    sobel_x = [[-1,0,1],[-2,0,2],[-1,0,1]]
    sobel_y = [[-1,-2,-1],[0,0,0],[1,2,1]]
    x_length, y_length = src.shape
    res = np.empty((x_length,y_length), dtype=float)
    for i in range(x_length):
        for j in range(y_length):
            res[i][j] = math.sqrt(convolution(sobel_x,i,j,src)**2+convolution(sobel_y,i,j,src)**2)
    return res
    
def Threshold_Algorithm(gradients):
    tau = 0
    h, w = gradients.shape
    for i in range(h):
        for j in range(w):
            tau += gradients[i][j]
    tau = tau / (h*w)
    tau_0 = tau
    tau_1 = -1
    while 1:
        lower_bound = []
        upper_bound = []
        for i in range(h):
            for j in range(w):
                if gradients[i][j]<tau_0: lower_bound.append(gradients[i][j])
                else: upper_bound.append(gradients[i][j])
        M_L = sum(lower_bound) / len(lower_bound)
        M_H = sum(upper_bound) / len(upper_bound)
        tau_1 = (M_L+M_H) / 2
        if(abs(tau_0-tau_1)<=0.0000001): break
        tau_0 = tau_1
    edge_map = np.empty((h,w), dtype=float)
    for i in range(h):
        for j in range(w):
            if(gradients[i][j]>=tau_1): edge_map[i][j] = 255
            else: edge_map[i][j] = 0
    return edge_map
    
def getGreyImge(img):
    rgb_weights = [0.2989, 0.5870, 0.1140]
    return np.dot(img[...,:3], rgb_weights)
    
def getEdgeImage(img,Gaussian_Matrix):
    x, y = img.shape
    Gaussian_image = np.empty((x,y), dtype=float)
    for i in range(x):
        for j in range(y):
            Gaussian_image[i][j] = convolution(Gaussian_Matrix,i,j,img)
    gradients = Sobel_Operation(Gaussian_image)
    return Threshold_Algorithm(gradients)
    
if __name__ == '__main__':
    Gaussian_Matrix = Gaussian_Blur(1.5,5)
    img = plt.imread("./Q4_image_1.jpg")
    grayscale_image = getGreyImge(img)
    edge_map = getEdgeImage(grayscale_image,Gaussian_Matrix)
    img_g = Image.fromarray(edge_map)
    img_g.show()
    

