import datetime
print(datetime.datetime.now())
yes = datetime.datetime(2017,3,24,11,2,27,0)
now1= datetime.datetime.now()
print(yes," ",now1)
sub = now1 - yes
print(sub.days) #prints the number of days between two dates
