#!/usr/bin/python
import time
from autojenkins import Jenkins
 
j = Jenkins('http://192.168.1.216:8080/')

#Build new job.
print "Building Job"
j.build('my-new-job')
 
#check result...Currently does not work.
while j.last_result('my-new-job')['result'] != '':
	result = j.last_result('my-new-job')['result']
	#print result
	if result == 'SUCCESS':
		print 'Job Built Successfully'
		break   
else:
	time.sleep(1)	
