import cv2
import numpy

img=cv2.imread('Lena.tiff',1)
img2=cv2.imread('F16.tiff',1)
cv2.imshow('Before steganography',img)

def binary(a):
    binary_of_image_pixel=[]
    
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for k in range(a.shape[2]):
                binary_of_image_pixel.append(list(numpy.binary_repr(a[i][j][k])))
    return binary_of_image_pixel

bin_img=binary(img)
bin_img2=binary(img2)

binarylist=[]

for i in range(len(bin_img2)):
    for j in range(len(bin_img2[i])):
        binarylist.append(bin_img2[i][j])

for i in range(len(binarylist)):
    bin_img[i][-1]=binarylist[i]
decimal=[]
new=[]
for i in range(len(bin_img)):
    ds=""
    for each_alphabet in bin_img[i]:
        ds=ds+str(each_alphabet)
    new.append(ds)

for a in new:
    decimal.append(int(a,2))

final=[]
final=numpy.reshape(decimal,(512,512,3))

finali=numpy.array(final,dtype=numpy.uint8)
cv2.imshow('After steganography',finali)
for i in range(5):
    for j in range(5):
        for k in range(3):
            print(img[i][j][k],"\t",finali[i][j][k])
