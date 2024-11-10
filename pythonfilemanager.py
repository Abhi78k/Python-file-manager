import os
import glob
import shutil
from os import path
filename = glob.glob(r"C:\Users\ABHIJITH\Desktop\Abhijith\Downloads\*")
pdf = ['.pdf']
notepad = ['.txt']
media = ['.jpg','.jpeg','.PNG','.png','.mp4','.ico']
pdfloc = r"C:\Users\ABHIJITH\Desktop\Abhijith\Downloads\pdf files"
notepadloc = r"C:\Users\ABHIJITH\Desktop\Abhijith\Downloads\notepad files"
medialoc = r"C:\Users\ABHIJITH\Desktop\Abhijith\Downloads\media or image files"
for file in filename:
    if os.path.splitext(file)[1] in pdf:
        if (path.exists(pdfloc)):
            shutil.move(file,pdfloc)
        else:
            os.mkdir(pdfloc)
            shutil.move(file,pdfloc)
    elif os.path.splitext(file)[1] in notepad:
        if (path.exists(notepadloc)):
            shutil.move(file,notepadloc)
        else:
            os.mkdir(notepadloc)
            shutil.move(file,notepadloc)
    elif os.path.splitext(file)[1] in media:
        if (path.exists(medialoc)):
            shutil.move(file,medialoc)
        else:
            os.mkdir(medialoc)
            shutil.move(file,medialoc)
            