# Higher Class Language compiler for PYVM
# transpiles a tiny language to ppvm for assembler
#
# By: Ari Stehney
#

import sys
import os
import time
import crayons

at_compiler_tags = dict()
at_stack = dict()
at_functions = dict()
at_includes = dict()

def CompileCode(inputcode):
    if not inputcode.count(';')>=(inputcode.count('\n')+1):
        print(crayons.red("compiler: end line charactor not found!"))
        sys.exit()
    ic = inputcode
    inputcode = inputcode.replace("\n", "")
    inputcode = inputcode[:-1].split(";")
    outFile = ""
    for word in inputcode:
        if word.startswith("function "):
            at_functions[word.split(' ')[1].split('{')[0].split('(')[0]] = word.split(' ')[1].split('{')[1].split('}')[0].replace("<","{").replace(">","}")

        if word.startswith("#comperror"):
            print(crayons.red("error: "+word.split(' ')[1]))
            sys.exit()
        if word.startswith("#include"):
            includeFileName = word.split(' ')[1]
            at_includes[os.path.splitext(includeFileName)[0]] = os.path.dirname(__file__)+"/modules/"+os.path.splitext(includeFileName)[0]+"/"+os.path.splitext(includeFileName)[0]
            if not os.path.exists(os.path.dirname(__file__)+"/modules/"+os.path.splitext(includeFileName)[0]+"/"+includeFileName):
                print(crayons.red("file error: include file not found!"))
                sys.exit()
            with open(os.path.dirname(__file__)+"/modules/"+os.path.splitext(includeFileName)[0]+"/"+includeFileName,mode="r") as fInclude:
                codeLib = fInclude.read()
            oc_n = codeLib+"\n"+ic.replace(word+";\n","")
            return CompileCode(oc_n)
            
        if not (word.startswith("#include") or word.startswith("#comperror") or word.startswith("function")):
            if word.startswith("//"):
                print("",end="")
            else:
                wcode = word.split("(")
                arg = wcode[1].split(")")[0]
                command = wcode[0]
                insfound=False
                # Process Code
                if command=="callmacro":
                    if not arg in at_functions:
                        print(crayons.red("macro error: callmacro: function name '" + arg + "' not defined!"))
                        sys.exit()
                    outFile = outFile+str(at_functions[arg].replace("&","\n"))+"\n"
                    insfound = True

                # Include Dynamic Compiler extensions
                for key in at_includes:
                    try:
                        with open(at_includes[key]+".py", mode="r") as d_lib:
                            dlibfile = d_lib.read()
                        exec(dlibfile)

                    except FileNotFoundError:
                        print(crayons.red("dynamic includes error!"))
                        sys.exit()
                    
                if command=="print":
                    outFile = outFile+"["+str(arg.split('"')[1].split('"')[0]).replace(' ','_')+"]\n"
                    outFile = outFile+"println"+"\n"
                    insfound = True

                if command=="printstk":
                    outFile = outFile+"println"+"\n"
                    insfound = True

                if command=="input":
                    outFile = outFile+"["+str(arg.split('"')[1].split('"')[0]).replace(' ','_')+"]\n"
                    outFile = outFile+"println"+"\n"
                    outFile = outFile+"read"+"\n"
                    insfound = True

                if command=="math":
                    if "*" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("*")[0]+"}\n"
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("*")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True
                    if "/" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("/")[0]+"}\n"
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("/")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True
                    if "-" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("-")[0]+"}\n"
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("-")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True
                    if "+" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("+")[0]+"}\n"
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("+")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True
                    if "%" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("%")[0]+"}\n"
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("%")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True

                if command=="mathstk":
                    if "*" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("*")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True
                    if "/" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("/")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True
                    if "-" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("-")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True
                    if "+" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("+")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True
                    if "%" in str(arg.split(",")[0]):
                        outFile = outFile+"{"+str(arg.split(",")[0]).split("%")[1]+"}\n"
                        outFile = outFile+"*\n"
                        insfound = True

                if command=="__raw__":
                        outFile = outFile+arg
                        print(crayons.yellow("warning: ")+crayons.yellow("assembler code 'raw' misuse can cause errors!"))
                        insfound = True

                if insfound==False:
                    print(crayons.red("compiler: function error! (Keyword Not Found)"))
    return outFile[:-1]


filename1 = sys.argv[1]
filename2 = sys.argv[2]

print(crayons.cyan("opening..."))
#os.getcwd()+"/"
if os.path.isfile(filename1):
    with open(filename1,mode="r") as fn1:
        codeIn = fn1.read()

    print(crayons.cyan("compiling..."))
    outCode = CompileCode(codeIn)

    print(crayons.cyan("making output..."))
    with open(filename2,mode="w") as fn2:
        fn2.write(outCode)

else:
    print(crayons.red("tc-pvm: Input file not found: "+filename1))
