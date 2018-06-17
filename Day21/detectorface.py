import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #learn on haarcascade

img = cv2.imread("news.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #changing the original image to grayscale

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.11, minNeighbors=5) #searching scale is scalerfactor. smaller the scalefactor better the accuracy. minNeighbors to tell how many neighbors

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3) #first parameter is highest point, second lowest point, third is color an RGB

print(type(faces))
print(faces) #returns dimensions of faces

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
