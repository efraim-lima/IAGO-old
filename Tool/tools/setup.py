import sys
from cx_Freeze import setup, Executable

import pandas as pd
import numpy as np
import os.path
import re, sys
from selenium import webdriver
import os.path
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import PySimpleGUI as sg
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
icon = "ASTRO-Group.png"


if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "IA5",
        version = "1.4",
        description = "Video Content Artificial Inteligence",
        options = {"build_exe": build_exe_options},
        executables = [Executable("yt_full.py", base=base, icon=icon)])


# cd C:\Users\efrai\Desktop\YT\__YT__\__API__\
# python setup.py build