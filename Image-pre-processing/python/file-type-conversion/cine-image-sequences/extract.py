#extraction of tiff images from cine files
#-------------------------------------------#
#import essential libraries
import imageio
import pims
#-------------------------------------------#
#extraction function
def extract():
    T=[2,3]
    H=[13.5,15,17.5,20,22.5,25]
    for h in H:
        for t in T:
            im=pims.open('./'+str(t)+'_'+str(h)+'cm.cine')
            for i in range(len(im)):
                imageio.imwrite('./rose_'+str(t)+'_'+str(h)+'cm/'+str(i)+'.tiff',im[i])
                if (i==2001):
                    break
                print('extracting '+'height:'+str(h)+', take:'+str(t)+' image_no:'+str(i))

#-------------------------------------------#
#calling extraction
extract()

