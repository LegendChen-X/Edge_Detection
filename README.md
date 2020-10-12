# CSC420_A1
> **Note for Linux users:** if you're using Ubuntu, make sure you've installed the following packages if
> you haven't done so already:
>
>     sudo apt-get install -y libfuse-dev
>     sudo apt-get install -y fuse
>     sudo apt-get install -y pkg-config


## Summary
In this assignment, I have implement funtions `Gaussian_Model`, `Gaussian_Blur`, `convolution`, `Sobel_Operation`, `Threshold_Algorithm`, `getGreyImge`, `getEdgeImage`, `neighbor_check`, `CC_label`.


## Tests Procedures
First `cd` into A1b and run `runit.sh`. (May need `chmod 700 runit.sh` to change the permission.) 
It will create baseic tests for our system including, `mkdir` `rmdir` `mv` `touch` `cd` `ls` `read` `write` `unlink` .
After these operations, `runit.sh` will exit the `mnt` and `mount` it again to test the storage persistence ability of our file system.

## Academic Honest
All members, Xiang Chen, Keyi Zhang, promise all codes are written by ourselves and both of us understand code well.
