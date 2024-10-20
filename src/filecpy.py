import os
import shutil
def Cpy_Directory(source, destination):
    if not os.path.exists(source):
        raise Exception("path to source directory does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    items = os.listdir(source)
    for item in items:
        pth = os.path.join(source, item)
        if os.path.isfile(pth):
            #print(f"Copying {pth}...")
            shutil.copy(pth, destination)
        else:
            Cpy_Directory(pth, destination+ f"/{item}")