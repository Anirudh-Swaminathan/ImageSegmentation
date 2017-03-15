**Project** : Image Segmentation into foreground and background using Python

----------
**Language used:** Python

**Algorithm:**
1. Compute the histogram of pixel intensities vs the number of pixels
2. Loop through the grayscale intensities from 0 to 255, setting each as a threshold
3. Compute the weighted mean, and the variance from the function
4. Compute the function value at that point
5. Update minimum variance and then update the threshold
