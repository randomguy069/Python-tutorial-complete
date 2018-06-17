import datetime
import time
lst = []
for i  in range (5):
    lst.append(datetime.datetime.now())
    time.sleep(1)
for i in lst:
    print (i)
