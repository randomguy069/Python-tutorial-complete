import cv2

img = cv2.imread("galaxy.jpg",0) #reading the image file. Reading image in blackscale is 0 and image in color is 1, -1 is transparency

print(img) #will return list of matrices
print (type(img))
print(img.shape) #shows the image resolution
print(img.ndim) #shows dimensions

resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resizing the image
cv2.imshow("Galaxy",resized_image) #opens a window
cv2.imwrite("Resized_Galaxy.jpg",resized_image)
cv2.waitKey(0) #window waits for 2000 seconds. if you put 0 waits till button is clicked
cv2.destroyAllWindows()
