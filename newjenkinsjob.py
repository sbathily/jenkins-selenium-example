#!/usr/bin/python
import time
from autojenkins import Jenkins
 
j = Jenkins('http://192.168.1.216:8080/')
 
# Create a new job.
j.create_copy('my-new-job', 'Selenium-Test', repo='my-repo', branch='my-branch')
newjob = j.job_info('my-new-job')

while newjob != 'null':
	print 'Job Created Successfully'
	break
else:
	time.sleep(1)
