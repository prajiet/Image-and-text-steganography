import cv2
import numpy

#numpy.set_printoptions(threshold=numpy.nan)
img=cv2.imread('Lena.tiff',1)
cv2.imshow('Original',img)


#print(img)
txt=open('Text.txt',"rt")
binary_of_text=' '.join(format(ord(a),'b')for a in txt.read())
#print(b)
binary_of_image_pixe=[]
for i in range(512):
    for j in range(512):
        for k in range(3):
            binary_of_image_pixe.append(list(numpy.binary_repr(img[i][j][k])))


for i in range(5):
    print(binary_of_image_pixe[i][-1])
binary_of_t=[]
p=0
binary_of_image_pixel=list(binary_of_image_pixe)
print(type(binary_of_image_pixel[0]))
binary_of_t=binary_of_text.split(' ')

for q in range(5):
    print(binary_of_image_pixel[q],'pehle')
for num in binary_of_t:
    for index in num:
        binary_of_image_pixel[p][-1]=index
        p=p+1
new=[]
for q in range(5):
    pass

for ne in binary_of_image_pixel:
    ds=""
    for each_albhabet in ne:
        ds=ds+str(each_albhabet)
    
    new.append(ds)
for q in range(5):
    pass
new_decimal=[]        
for a in new:
    new_decimal.append(int(a,2))

for q in range(5):
    print(new_decimal[q],'new_decimal')
final=[]
final=numpy.reshape(new_decimal,(512,512,3))
final.astype('uint8')
#print(final[0][0][0])

finali=numpy.array(final,dtype=numpy.uint8)

#print(finali.dtype)
#print(finali)
cv2.imshow('After steganography',finali)
cv2.waitKey(200) 
