# List all the files in all the directories and subdirectories of the given path.

import os
print ("Os Walk Performance")
for (root,files,direc) in  os.walk("others", topdown = False):
  print(root, files, direc)
  
import os, time, glob

