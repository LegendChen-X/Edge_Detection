# CSC420_A1
> **Note for Linux users:** if you're using Ubuntu, make sure you've installed the following packages if
> you haven't done so already:
>
>     sudo apt-get update
>     sudo apt install software-properties-common
>     sudo add-apt-repository ppa:deadsnakes/ppa
>     sudo apt install python3.8


## Summary
In this assignment, I have implement funtions `Gaussian_Model`, `Gaussian_Blur`, `convolution`, `Sobel_Operation`, `Threshold_Algorithm`, `getGreyImge`, `getEdgeImage`, `neighbor_check`, `CC_label`.

`Gaussian_Model`: Implement Gaussian distribution.
`Gaussian_Blur`: Use Gaussian_Model to blur the image.
`convolution`: Convolution between one kernel and image.
`Sobel_Operation`: Image Gradient.
`Threshold_Algorithm`: Get binary image.
`getGreyImge`: Transfer RGB to one channel.
`getEdgeImage`: Get binary image.
`neighbor_check`: Check eight neighbours when doing labels.
`CC_label`: Label the graph.

You can find details in the report and `q4_code.py`, `q5_code.py`, and `q6_code.py`.

## Tests Procedures

### Use `python3 q4_code` to get three binary images (two are given and one is mine). It may take slightly long time to get my binary picture due to the fact that I use a 4K image.

### Use `python3 q6_code.py` to count number of cells. It includes test for `q5_code.py`.

## Academic Honest
I, Xiang Chen,  promise all codes are written by myself.
