import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def Gaussian_Model(sigma,point):
    x, y = point
    ratio = 1/(2*math.pi*sigma**2)
# Slightly different for the expression from the lecture. #
    e_part = math.exp(-(x**2+y**2)/(2*sigma**2))
    return ratio * e_part
    
def Gaussian_Blur(sigma,kernel_size):
# This can use array to boost access speed. #
    half_kernel = (kernel_size-1) // 2
    Gaussian_matrix = []
    for i in range(kernel_size):
        Gaussian_matrix.append([])
        for j in range(kernel_size):
            Gaussian_matrix[i].append(Gaussian_Model(sigma,(j-half_kernel,half_kernel-i)))
# Visualize the Matrix. #
    for i in range(len(Gaussian_matrix)): print(Gaussian_matrix[i],'\n')
    print("\n")
    return Gaussian_matrix
    
def convolution(matrix,x,y,src):
# This function is only for grey scale image. #
# Please use getGreyImge first, if input is a RGB image. #
# Can be optimized by the product of two vectors. #
    x_boundary, y_boundary = src.shape
    kernel_size = len(matrix)
# Help to track the row in Matrix. #
    index_i = 0
    res = 0
# Get the start and end of k. #
    start = int(-(kernel_size-1)/2)
    end = int((kernel_size-1)/2 + 1)
    for u in range(start,end):
# Help to track the coloum in Matrix. #
        index_j = 0
        for v in range(start,end):
# Boundary check. Smarter than padding the image. #
            if(x-u<0 or y-v<0 or x-u>=x_boundary or y-v>=y_boundary): res += 0
            else: res += src[x-u][y-v] * matrix[index_i][index_j]
            index_j += 1
        index_i += 1
    return res
    
def Sobel_Operation(src):
# This function is only for grey scale image. #
# Please use getGreyImge first, if input is a RGB image. #
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
# Set epsilon to 0.0000001 (enough small)#
        if(abs(tau_0-tau_1)<=0.0000001): break
        tau_0 = tau_1
    edge_map = np.empty((h,w), dtype=float)
    for i in range(h):
        for j in range(w):
            if(gradients[i][j]>=tau_1): edge_map[i][j] = 255
            else: edge_map[i][j] = 0
    return edge_map
    
def getGreyImge(img):
# Change the rgb value to grey. #
    rgb_weights = [0.2989, 0.5870, 0.1140]
    return np.dot(img[...,:3], rgb_weights)
    
def getEdgeImage(img,Gaussian_Matrix):
# This function is only for grey scale image. #
# Please use getGreyImge first, if input is a RGB image. #
    x, y = img.shape
# Do the filter first to decrease the noise. #
    Gaussian_image = np.empty((x,y), dtype=float)
    for i in range(x):
        for j in range(y):
            Gaussian_image[i][j] = convolution(Gaussian_Matrix,i,j,img)
# Get the gradient image (array). #
    gradients = Sobel_Operation(Gaussian_image)
    return Threshold_Algorithm(gradients)
    
if __name__ == '__main__':
# Get two Gaussian_Matrix. #
    Gaussian_Matrix = Gaussian_Blur(1.5,3)
    Gaussian_Matrix_2 = Gaussian_Blur(0.5,5)
# Get image array. #
    img_1 = plt.imread("./Q4_image_1.jpg")
    img_2 = plt.imread("./Q4_image_2.jpg")
    img_3 = plt.imread("./my_image.jpg")
# Change to grey scale.#
# If the image is grey, skip this step. #
    grayscale_image_1 = getGreyImge(img_1)
    edge_map_1 = getEdgeImage(grayscale_image_1,Gaussian_Matrix)
    img_g_1 = Image.fromarray(edge_map_1)
    img_g_1.show()
    
    grayscale_image_2 = getGreyImge(img_2)
    edge_map_2 = getEdgeImage(grayscale_image_2,Gaussian_Matrix_2)
    img_g_2 = Image.fromarray(edge_map_2)
    img_g_2.show()
    
    grayscale_image_3 = getGreyImge(img_3)
    edge_map_3 = getEdgeImage(grayscale_image_3,Gaussian_Matrix)
    img_g_3 = Image.fromarray(edge_map_3)
    img_g_3.show()
    
    
    
    
    
    
