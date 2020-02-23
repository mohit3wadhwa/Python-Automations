import shutil
import os


source = os.listdir("/Users/mohitwadhwa/Desktop/<source folder>")
folder = "/Users/mohitwadhwa/Desktop/<source folder>"
destination = "/Users/mohitwadhwa/Desktop/<destination folder>"

# Enable this and required folder will be created automatically
# NOTE:- ADMIN ACCESS SHOULD BE HERE...
# if not os.path.exists(destination):
#    os.mkdir(destination)

for files in source:
    #OPTIONAL - Use only when any condition required.
    if files.endswith('.JPG'):
        # CUT & PASTE; NOTE:- Please make sure destination folder should be created.
        shutil.move(folder + '/' + files, destination)
        # Copy & PASTE; NOTE:- Please make sure destination folder should be created.
        shutil.copy(folder + '/' + files, destination)
