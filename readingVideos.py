import cv2 as cv
print("Package imported")

cap = cv.VideoCapture("/media/farhan/New Volume/Game recording/Ace.mp4") #Here you can put integers according to your numbers of webcam 
#sets the frame
cap.set(3,400) 
cap.set(4,480)
#this loop will read the frames of your video and show it until you press q on keyboard
while True:
    success, img = cap.read()
    cv.imshow("Ace",img)
    if cv.waitKey(1) & 0xFF==ord("q"):
        break