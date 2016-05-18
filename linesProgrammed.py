import os
import datetime

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
f = open("/home/bryce/Documents/Projects/bryceandress.github.io/_data/lines.yml", "w")
f.write("- name: ")
f.write(str(programmed))
f.write(" lines of code committed as of " + str(datetime.date.today()))
f.close()

