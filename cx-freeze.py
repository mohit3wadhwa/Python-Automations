import sys
from cx_Freeze import setup, executable
base=none
setup(name='hello',
	version='1.0',
	executables=[Executable('hello',base=base)])
