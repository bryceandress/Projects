import os

programmed = 0

#Get all the files that have been committed
for root, dirs, files in os.walk("/home/bryce/Documents/Projects/python_projects/completedprojects/", topdown=False):
	for name in files:
		if name.endswith('.py'):
			with open(name) as f:
				for i, l in enumerate(f):
					programmed += 1
#TODO
#WRITE PROGRAMMED TO HIDDEN FILE
f = open("/home/bryce/.lines", "w")
f.write(str(programmed)+"\n")
f.close()

