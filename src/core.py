# PYTHON VERSION: 3.12.0

from difflib import HtmlDiff
from tkinter import Tk
from tkinter import filedialog
import os

# Asks user to choose a file
def select_file():
    root = Tk()
    root.withdraw()
    
    file = filedialog.askopenfilename(title="Select a file")
    
    root.destroy()

    return file

# Read lines from both files and compares them
def read_files(path_01, path_02):

    d = HtmlDiff()

    with open(path_01, "r", encoding="utf-8") as f1, \
        open(path_02, "r", encoding="utf-8") as f2:
        
            try:
                lines_file01 = f1.readlines()
                lines_file02 = f2.readlines()
            
                html_diff = d.make_file(
                    lines_file01,
                    lines_file02,
                    fromdesc = "file01",
                    todesc = "file02")
            except (UnicodeDecodeError, OSError):
                return None

    return html_diff

# Asks user where to save a diff file
def set_output_file():
    root = Tk()
    root.withdraw()

    output_file = filedialog.asksaveasfilename(title="Save as...", initialfile="diff.html", 
                                                 defaultextension=".html", filetypes=[("HTML Files", "*.html")])

    root.destroy()

    return output_file

# Default save location if user doesn't provide one
def create_output_folder():
    directory = "output"
    parent_dir = os.path.abspath(os.path.join(directory, os.pardir))
    path = os.path.join(parent_dir, directory)

    try:
        os.mkdir(path)
        filename = os.path.join(path, "diff.html")
        return filename
    except OSError:
        print(f"Folder {directory} already exists in {path}")

# Saves diff file
def save_file(html_diff, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_diff)
