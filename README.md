# PyVM
Python Compiler and Assembler demo.
This is very simple and buggy but is a good demo
on how code complimation works.

--> THIS ONLY WORKS ON UNIX-LIKE OSES <--
Installing the path system will fail and
not correctly run! Please do not report windows
compatibility in issues!

# Installing
First, Make sure you have python3 installed.
Second, install all of the modules.
```
pip3 install crayons
```
Then inside the root directory,run the path installer,
```
chmod +x install.sh
./install.sh
```
# Running
Commands:
1. atcc <source file>- at C compiler.
2. atmake <makefile>- makefile automater.
3. atsdk - sdk manager (updater/installer/version).
4. atrun <filename>- output runtime.
