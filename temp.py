import datetime
import time

dt1 = datetime.datetime.now()
delta  = datetime.timedelta(hours=1)

dt2 = dt1+delta

print "in an hour, the time will be", dt2
