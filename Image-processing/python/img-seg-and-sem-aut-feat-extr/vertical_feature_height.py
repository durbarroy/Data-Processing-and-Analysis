import numpy as np
from skimage import io
from matplotlib import pyplot as plt
from skimage.filters import threshold_local
from skimage.filters.rank import median
from skimage.morphology import disk


def read(img_in):
    img_read=io.imread(img_in)
    return(img_read)

def show(img):
    plt.imshow(img,cmap='gray')
    plt.show()


def adaptive_thresholding(image):
    block_size = 35
    adaptive_thresh = threshold_local(image, block_size, offset=10)
    binary_adaptive = image > adaptive_thresh
    return binary_adaptive


def remove_noise(im):
    return median(im, disk(6))

def central_height(im,yStart,yEnd,xCentral):
    for i in range(yStart,yEnd+1):
        if abs(float(im[i+1,xCentral])-float(im[i,xCentral]))==255:
            return (yEnd-i)



def process(startImage,endImage):
    central_heights=[]
    for i in range(startImage,endImage):    


        img_in='./'+str(i)+'.tiff'
        print('processing image:',i)
        img=read(img_in)
        bin_ada=adaptive_thresholding(img)
        noise_removed=remove_noise(bin_ada)
        ch=central_height(noise_removed,190,290,264)
        central_heights.append(ch)
        #show(noise_removed)


    print(central_heights)
    f=open("centralHeight_16mm_1.csv","w")
    f.write("#time[ms],height[pixels]\n")
    for i in range(len(central_heights)):
        f.write("%3.2f,%i\n" %(i*0.1,central_heights[i]))
    f.close()

process(65,300)


