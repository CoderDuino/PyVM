#!/usr/local/bin/python3

#  ____  _  _  __ __ ___  ___    __ __  __  __  ______  ___  __    __     ____ ____ 
# || \\ \\//  || || ||\\//||    || ||\ || (( \ | || | // \\ ||    ||    ||    || \\
# ||_//  )/   \\ // || \/ ||    || ||\\||  \\    ||   ||=|| ||    ||    ||==  ||_//
# ||    //     \V/  ||    ||    || || \|| \_))   ||   || || ||__| ||__| ||___ || \\                                                                                
# Installer for pyvm
# By: Ari Stehney

import os
import sys
import crayons
import time

print("-==Installing PYVM==-")

print(crayons.yellow("This will require restart after install to activate"))
yn1 = input(crayons.yellow("Continue [Y/n]: "))

if yn1.lower()=="y":
	print("adding to system path...")
	nhome = input(crayons.yellow("Path to Home dir: "))
	outF = open(nhome+"/.bash_profile", "a")
	outF.write("""
# PYVM Install
export PATH=~/pyvm/bin:$PATH
export PATH=~/pyvm:$PATH
export PVMHOME=~/pyvm
export PVMBIN=~/pyvm/bin
""")
	print("installing extensions...")
	print("")
	print("")
	print("")
	print("")
	print("PYVM Is now installed!")
	print("use:")
	print("	atcc - at C compiler")
	print("	atmake - makefile automater")
	print("	atsdk - sdk manager (updater/installer/version)")
	print("	atrun - output runner")
	print("")
	print(crayons.green("reboot to activate!",bold=True))

	