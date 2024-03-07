import os
#relative
# used to read and write files by the name alone


#absolute
# spell out the exact location of the file-drive name, then directory, then file name

os.path.exists("text.txt")

os.rename("text.txt", "new_text.txt")


os.path.getsize("spider.txt")
#This code will provide the file size
os.path.getmtime("spider.txt")
#This code will provide a timestamp for the file
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
#This code will provide the date and time for the file in an easy too understand format
os.path.abspath("spider.txt")
#This code takes the file name and turns it into an absolute path


print(os.getcwd())
#This code snippet returns the current working directory.


os.mkdir("new_dir")
#The os.mkdir("new_dir") function creates a new directory called new_dir

os.chdir("new_dir")
os.getcwd()
#This code snippet changes the current working directory to new_dir. The second line prints the current working directory.

os.mkdir("newer_dir")
os.rmdir("newer_dir")
#This code snippet creates a new directory called newer_dir. The second line deletes the newer_dir directory.



os.listdir("website")
#This code snippet returns a list of all the files and sub-directories in the website directory.

dir = "website"
 for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
          print("{} is a directory".format(fullname))
     else:
          print("{} is a file".format(fullname))
          
          
          
          
          
 Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
 os.mkdir(dest_dir)


# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")


# Move the file from its original location to the destination:
os.rename(src_file, dest_file)



# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
  dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)


The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.


import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open (filename, "w") as file:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  date = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(date.strftime("%Y-%m-%d")))


print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

