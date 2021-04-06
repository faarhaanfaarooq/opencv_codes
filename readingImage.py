import cv2 as cv
print("Pacakage Imported")

img = cv.imread("/home/farhan/Pictures/weed.png") #the path of your picture you want to display
cv.imshow("weed", img)
cv.waitKey(0)