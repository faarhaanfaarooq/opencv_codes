import cv2 as cv
print("Pacakage Imported")

img = cv.imread("/home/farhan/Pictures/wd.png") #the path of your picture you want to display
cv.imshow("weed", img)
cv.waitKey(0)