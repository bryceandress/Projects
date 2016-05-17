import sys

#Open to-do.list
fptr=open('/home/bryce/.to-do.list', 'w+')

#Check which flag was supplied, do correct thing.
if sys.argv[1] == "-a":
    addTodo()

elif sys.argv[1] == "-td":
    #COMPLETE FUNCTION

elif sys.argv[1] == "-d":
    #COMPLETE FUNCTION

elif sys.argv[1] == "-h":
    print("Flags:\n-a:  Add to to-do list\n-td: Show list of to-dos\n-d:  Completed to-do\n")

else:
    incorrectFlag()

fptr.close()

#Functions
def addTodo():
    fptr.write(sys.argv[2])
    print("To-do list updated")

def printTodo():
    #Print list of todos

def incorrectFlag():
    sys.stderr.write("Incorrect flag, type -h for list of flags")

def doneTodo():
    #Remove done
