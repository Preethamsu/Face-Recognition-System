import cv2

image=cv2.imread("image.jpeg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv2.waitKey(0)
cv2.destroyAllWindows()