import cv2 as cv
print("Package Imported")

img = cv.imread("/home/farhan/Pictures/lambo.jpg")
#to know the size of current pic
print(img.shape)
#to resize the pic
imgResize = cv.resize(img,(400,190))
#to crop the pic
imgCrop = img[0:400,400:600]
cv.imshow("Car",img)
cv.imshow("resized",imgResize)
cv.imshow("Crop",imgCrop)
cv.waitKey(0)