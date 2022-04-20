# Imports PIL module

import os
import itertools
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image

#File location naming
class ing:
    def __init__(self):
        self.pen = ""
    def select_file(self):
        self.pen = (fd.askdirectory(title='Choose a file'))
        print(os.listdir(self.pen))

#ends program without printing
def end():
    exit(1)


#The file locations of the three parts to an NFT: background, base image, components
#Background
blap = ing()
#Base
blap2 = ing()
#Components
blap3 = ing()

#Create and format the GUI
root = Tk()
root.title("Nft Printer")
frm = ttk.Frame(root, padding=10)
frm.grid()

#Button implementation

#Sets Background
ttk.Button(frm, text="Background", command = blap.select_file).grid(column=1, row=0)
#Sets Base
ttk.Button(frm, text="Base", command = blap2.select_file).grid(column=2, row=0)
#Sets Components
ttk.Button(frm, text="Components", command = blap3.select_file).grid(column=3, row=0)
#Ends program and does not print
ttk.Button(frm, text="Quit", command = end).grid(column=2, row=2)
#Ends the GUI and prints
ttk.Button(frm, text="Execute", command = root.destroy).grid(column=2, row=1)
#Gives a preview of what the images will look like


#Loops until the GUI is executed
root.mainloop()


componentList =[]
for x in os.listdir(blap3.pen):
    newlist = []
    for y in os.listdir(blap3.pen + chr(92) + x):
      newlist.append(blap3.pen +chr(92)+ x +chr(92) + y)
    componentList.append(newlist)

#Create the list for background images and base images
baseList = os.listdir(blap2.pen)
backgroundList = os.listdir(blap.pen)

#Contains a list of lists each with the directory for each of the combinations of components
ImgList = list(itertools.product(backgroundList, baseList, *componentList))
for q in ImgList:
    print(q)


#prints The NFTs
for i in list(ImgList):

  background = Image.open((blap.pen+chr(92) + i[0]), mode='r')
  base = Image.open((blap2.pen+chr(92) + i[1]), mode='r')
  background.paste(base, base)
  for x in range(2,(len(i))):
    comp = Image.open((i[x]), mode='r')
    background.paste(comp,comp)
  background.show()

exit(1)
