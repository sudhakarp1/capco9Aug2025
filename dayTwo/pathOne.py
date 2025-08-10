from pathlib import Path 
import os 
pth = Path('.')
print(pth)
print(pth.absolute())
print(os.path.isdir(pth))
print(os.path.isfile(pth))
print(os.path.islink(pth))
print(os.path.basename('/usr/bin/bash'))
print(os.path.join(pth.absolute(),'someFile.txt'))
print(os.listdir(pth))
#os.mkdir() --> mkdir
#os.makedirs() --> mkdir -p 
