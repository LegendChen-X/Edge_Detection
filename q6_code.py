import matplotlib.image as mpimg
import q4_code
import q5_code
from q4_code import *
from q5_code import *
# Gaussian_Matrix with small kernel size#
Gaussian_Matrix = Gaussian_Blur(3,3)
img = mpimg.imread("./Q6.png")
# Transfer to edge map. #
edge_map = getEdgeImage(img,Gaussian_Matrix)
img_g = Image.fromarray(edge_map)
img_g.show()
labels, counter = CC_label(edge_map)
print("The number of cells in the image is",counter)

