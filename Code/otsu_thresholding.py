import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../DataInput/coins.jpg',0)
blur = cv2.GaussianBlur(img,(5,5),0)

plt.imshow(blur, 'gray')
plt.title('Input')
plt.show()

# find normalized_histogram, and its cumulative distribution function
# Returns 256*1 numpy matrix, each having the number of pixels with that value of intensity
hist = cv2.calcHist([blur],[0],None,[256],[0,256])

# Plot the normalized histogram
plt.hist(hist, np.arange(256))
img = plt.gcf()
plt.show()
img.savefig('../Result/coin_hist.png', dpi=100)

# print hist.shape
# print hist.max()

# Normalize this hostogram from 0 to 1
hist_norm = hist.ravel()/hist.max()

# print hist_norm.shape

# Find the cumulative distribution of the pixels wrt intensity
Q = hist_norm.cumsum()
# print Q.shape

bins = np.arange(256)
fn_min = np.inf
thresh = -1
for i in xrange(1,256):
    # probabilities
    p1,p2 = np.hsplit(hist_norm,[i])

    # cumulative sum of classes
    q1,q2 = Q[i],Q[255]-Q[i]

    # weights
    b1,b2 = np.hsplit(bins,[i])

    # finding means and variances
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2

    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# find otsu's threshold value with OpenCV function
ret, otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.imshow(otsu, 'gray')
plt.title('Output')
plt.show()

print "Threshold gotten by native implementation:",thresh
print "Threshold gotten by the OpenCV implementation:",ret

print "Percentage error in calculation is",abs(thresh-ret)/ret*100.0,"%"
