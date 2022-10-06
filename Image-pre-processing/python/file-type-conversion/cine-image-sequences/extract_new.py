#extraction of tiff images from cine files
#-------------------------------------------#
#import essential libraries
import imageio
import pims
#-------------------------------------------#
#extraction function
def extract(file_name):
    im = pims.open('./'+file_name+'.cine')
    for i in range(len(im)):
        imageio.imwrite('./'+file_name+str('/')+str(i)+'.tiff',im[i])
        if (i==2001):
            break
        print('extracting image slice:'+str(i))

#-------------------------------------------#
#calling extraction

def main():
    file_name = input('Enter the file name:\n')
    extract(file_name)

if __name__=='__main__':
    main()

