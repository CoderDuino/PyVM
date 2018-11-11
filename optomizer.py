# Code Transpiler for VVGA-PVM
# turns hdd-bytecode to pvm interpreted language
#
#
# BY: Ari Stehney
#

import array
import crayons
import os
import sys

opcodes = [
    "%",
    "*",
    "+",
    "-",
    "/",
    "==",
    "cast_int",
    "cast_str",
    "drop",
    "dup",
    "exit",
    "if",
    "jmp",
    "over",
    "print",
    "println",
    "read",
    "stack",
    "swap"
]

c_op = dict()

# Reverse Opcodes
c_op["%"] = "00"
c_op["*"] = "01"
c_op["+"] = "02"
c_op["-"] = "03"
c_op["/"] = "04"
c_op["=="] = "05"
c_op["cast_int"] = "06"
c_op["cast_str"] = "07"
c_op["drop"] = "08"
c_op["dup"] = "09"
c_op["exit"] = "10"
c_op["if"] = "11"
c_op["jmp"] = "12"
c_op["over"] = "13"
c_op["print"] = "14"
c_op["println"] = "15"
c_op["read"] = "16"
c_op["stack"] = "17"
c_op["swap"] = "18"

def OptomizerTrans(coderaw):
    lcbits = coderaw.split(" ")
    bufferout=[]
    for idx, word in enumerate(lcbits):
        #print("Ins:"+str(word)+"                      Index:"+str(idx))
        if "{" and "}" in word:
            bufferout.append(int(str(str(word.split("{")[1]).split("}")[0])))
        elif "[" and "]" in word:
            bufferout.append('"'+str(str(word.split("[")[1]).split("]")[0]).replace("_"," ")+'"')
        else:
            opcode = int(word)
            bufferout.append(opcodes[opcode])

    return bufferout


def OptomizerCreate(codestring, outStr = ""):
    lcode = codestring.split("\n")
    for word in lcode:
        if "{" and "}" in word:
            outStr = outStr + "{"+str(str(word.split("{")[1]).split("}")[0])+"}"+" "
        elif "[" and "]" in word:
            outStr = outStr + "["+str(str(word.split("[")[1]).split("]")[0])+"]"+" "
        else:
            if not word in opcodes:
                print(crayons.red("assembler: invalid opcode!"))
                sys.exit()
            outStr = outStr + c_op[word] + " "
    outStr = outStr[:-1]
    return outStr
            
		
        
