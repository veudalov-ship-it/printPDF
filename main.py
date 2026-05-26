import re
import sys
import os
import win32api
from time import sleep


path = sys.argv[1]
currentprinter = sys.argv[2]

r = re.search('БланкВозвратаРеалициалицияТоваров', path)
if not r is None:
    orientation = '-portrait'
else:
    orientation = '-landscape'


if getattr(sys, 'frozen', False):
    GHOSTSCRIPT_PATH = os.path.join(sys._MEIPASS, "gs/gs10.02.1/bin/gswin32.exe")
    GSPRINT_PATH = os.path.join(sys._MEIPASS, "GSPRINT/gsprint.exe")

else:
    GHOSTSCRIPT_PATH = os.path.abspath(r"gs/gs10.02.1/bin/gswin32.exe")
    GSPRINT_PATH = os.path.abspath(r"GSPRINT/gsprint.exe")



win32api.ShellExecute(0, 'open', GSPRINT_PATH,
                      '-ghostscript "' + GHOSTSCRIPT_PATH + '" -printer "' + currentprinter + '" "' + orientation + '" "' + path,
                      '.', 0)
sleep(3)


