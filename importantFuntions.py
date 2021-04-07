import cv2 as cv
print("Package Imported")

im = cv.imread("/home/farhan/Pictures/wd.png")
#to resize the frame
img = cv.resize(im, (350,250))
#grayscale
imgGray = cv.cvtColor(img,cv.COLOR_BGRA2GRAY)
#blur
imgBlur = cv.GaussianBlur(img,(11,11),0)
#Edge Detection
imgEdge = cv.Canny(img,100,100)
cv.imshow("Normal",img)
cv.imshow("Gray",imgGray)
cv.imshow("Blur",imgBlur)
cv.imshow("Edge",imgEdge)
cv.waitKey(0)