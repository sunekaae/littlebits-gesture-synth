import myrequest
import sometimes
import cloudmessage
import time

s = sometimes.Sometimes()
cm = cloudmessage.CloudMessage()
cm.duration_ms = 500
cm.percent = 99
while 1==1:
	s.ping(cm)
	print 'iteration'
	time.sleep (100.0 / 1000.0)

