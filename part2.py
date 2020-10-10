import math
def Gaussian_model(sigma,point):
    x, y = point
    ratio = 1/(2*math.pi*sigma**2)
    e_part = math.exp(-(x**2+y**2)/(2*sigma**2))
    return ratio * e_part
    
def Gaussian_Blur(sigma,kernel_size):
    half_kernel = (kernel-1) // 2
    matrix = []
    Gaussian_matrix = []
    
    for i in range(kernel_size):
        matrix.append([])
        Gaussian_matrix.append([])
        for j in range(kernel_size):
            matrix[i].append((j-half_kernel,half_kernel-i))
            Gaussian_matrix[i].append(Gaussian_model(sigma,matrix[i][j]))
            
    return Gaussian_matrix
    
print(Gaussian_Blur(1.5,3),'\n')
print(Gaussian_Blur(0.5,7))
    
    

