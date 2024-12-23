import sys 
import os
if len(sys.argv)==2:
    infile_name=sys.argv[1]
else:
    print ("Oops! Incorrect number of arguments.")
    sys.exit(2)
#checks if the file exists
if not os.path.isfile(infile_name):
    print("File doesn't exist.")
    sys.exit(3)
