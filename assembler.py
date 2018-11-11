# Assembler For PVM Language
# Assembles PYVM language to hdd binary
#
# By: Ari Stehney
#

import sys
import os
import optomizer
import crayons

filename1 = sys.argv[1]
filename2 = sys.argv[2]

if os.path.isfile(filename1):
    with open(filename1,mode="r") as fn1:
        codeIn = fn1.read()

    print(crayons.magenta("assembling..."))
    outCode = optomizer.OptomizerCreate(codeIn)

    print(crayons.magenta("encoding binary..."))
    with open(filename2,mode="w") as fn2:
        fn2.write(outCode)
else:
    print(crayons.red("assembler: input file not found!"))
