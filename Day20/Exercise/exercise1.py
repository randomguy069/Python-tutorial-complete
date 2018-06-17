import glob,cv2



for filex in glob.glob('*.jpg'):
    img = cv2.imread(filex,0)
    resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    img_new_name = "newbob"+filex
    cv2.imwrite(img_new_name,resized_image)
