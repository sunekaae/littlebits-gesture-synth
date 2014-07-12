#only does this sometimes

import myrequest
import time
import cloudmessage

class Sometimes:
	def __init__(self):
		self.start_time = time.time() * 1000
		self.previous_cm = cloudmessage.CloudMessage()

	def something(self):
		print 'some'

	def ping_values(self, percent, duration_ms):
		cm = cloudmessage.CloudMessage()
		cm.percent = percent
		cm.duration_ms = duration_ms
		self.ping(cm)

	def ping(self, cloudmessage):
#		print 'do it'
#		print self.start_time
#		print time.time() * 1000
		diff = (time.time() * 1000) - self.start_time
		if (1):
#			print 'more than a sec'
			if ((self.previous_cm.percent != cloudmessage.percent) or (self.previous_cm.duration_ms != cloudmessage.duration_ms)):
				self.doIt(cloudmessage)
			else:
				print "same value as last http request. skipping"
				time.sleep (200.0 / 1000.0)
			self.previous_cm = cloudmessage
			self.start_time = time.time() * 1000
	
	def doIt(self, cloudmessage):
#		print 'do the request'
		myrequest.makeHttpCall(cloudmessage)
		

	

