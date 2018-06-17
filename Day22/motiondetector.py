import cv2,time,datetime, pandas

first_frame = None #none is a python datatype
status_list =[None,None]
times =[]
df = pandas.DataFrame(columns=["Start","End"])
video = cv2.VideoCapture(0)



while True:

    check, frame = video.read() #check is boolean, frame is a numpy array
    status=0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0) #read on GaussianBlur

    if first_frame is None:
        first_frame = gray #will store first frame
        continue

    delta_frame = cv2.absdiff(first_frame,gray) #comparing two gray scale images

    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] #read about threshold
    thresh_frame = cv2.dilate(thresh_frame,None,iterations =1) #read about dilate. Iterations smoothens the image

    (_,cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #whats a contour, use of cnts needed

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.datetime.now())

    cv2.imshow("Capturing",gray)
    cv2.imshow("Capturi",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key = cv2.waitKey(1)

    print(gray)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.datetime.now())
        break

    datetime.datetime.now()


print(status_list)
print(times)

for i in range(0,len(times),2):
    df= df.append({"Start":times[i], "End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows
