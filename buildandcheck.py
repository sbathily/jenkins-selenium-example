#!/usr/bin/python
import time
from autojenkins import Jenkins
 
j = Jenkins('http://192.168.1.216:8080/')

# Build new job.
print "Building Job"
j.build('my-new-job')

while  j.job_info('my-new-job')['color'] == 'notbuilt' or j.job_info('my-new-job')['color'] == 'notbuilt_anime':
	#print j.job_info('my-new-job')['color']
	time.sleep(1)
	if j.job_info('my-new-job')['color'] == 'blue' or j.job_info('my-new-job')['color'] == 'yellow' or j.job_info('my-new-job')['color'] == 'red':
		#print j.job_info('my-new-job')['color']
		print 'Build Completed'
		break

if j.last_result('my-new-job')['result'] == 'SUCCESS':
	print 'Job was built successfully'
else:
	print 'Build failed'	
