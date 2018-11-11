#!/usr/local/bin/python3

# PVM Runtime
# VM with assembler and compiler
# By: Ari Stehney

from tkinter import *
import os
import time
import sys
import crayons
import vm
import optomizer

def runpvm(rpvmFile="vmdisk.hdd"):
    master = Tk()

    w = Canvas(master, width=800, height=600)
    w.pack()

    w.create_rectangle(0,0,800,600,fill='black',width=0)

    # Define VM Screen Object
    linetx = str(30)
    linetxc = str(0)
    screen = w

    def drawPixel(x,y,c):
        w.create_rectangle(x,y,1,1,fill=c)

    def drawText(x,y,t,c, style_s=""):
        w.create_text(x,y,text=t,fill=c,stipple=style_s)

    def drawRect(x,y,x2,y2,c):
        w.create_rectangle(x,y,x2,y2,fill=c)

    def drawCircle(x,y,c):
        w.create_rectangle(x,y,1,1,fill=c)
        
    def fillBackground(c):
        w.create_rectangle(0,0,800,600,fill=c,width=0)

    def drawImages(x,y,im):
        img = PhotoImage(file=im)
        canvas.create_image(x,y,anchor=NW,image=img)

    def appendVGA(tx):
        drawText(40,300, tx, "grey")
        
    print(crayons.green("reformatting temporary disk...",bold=True))
    with open("vmtemp.mem", mode="w") as vmwtemp:
        vmwtemp.write("")
    with open(rpvmFile, mode="r") as vmwbtemp:
        hdd_disk0 = vmwbtemp.read()

    vmtempread = open("vmtemp.mem", mode="r")
    vmtempwrite = open("vmtemp.mem", mode="w")

    print(crayons.green("reformatted temporary disk",bold=True))
    print(crayons.green("reading hard disk...",bold=True))

    time.sleep(2)
    print(crayons.green("v-vga started",bold=True))
    print(crayons.magenta("system image loaded",bold=True))

    # Drawing commands Here #
    """def paint( event ):
       python_green = "#476042"
       x1, y1 = ( event.x - 1 ), ( event.y - 1 )
       x2, y2 = ( event.x + 1 ), ( event.y + 1 )
       w.create_oval( x1, y1, x2, y2, fill = python_green )
    w.bind( "<B1-Motion>", paint )"""

    optcode = optomizer.OptomizerTrans(hdd_disk0)
    c = vm.Machine(optcode)
    c.run()
    c.dump_stack()

    appendVGA(c.log)
    vmtempwrite.write(str(c.data_stack))

    # End Drawing commands Here #
    print(crayons.magenta("setup image done",bold=True))
    mainloop()
    print(crayons.red("pvm exit",bold=True))
    vmtempread.close()
    vmtempwrite.close()

if __name__=="__main__":
    runpvm(sys.argv[1])
