# PYTHON VERSION: 3.11.9

from difflib import HtmlDiff
from tkinter import Tk
from tkinter import filedialog
import os


def select_file():
    root = Tk()
    root.withdraw()
    
    selected_file = filedialog.askopenfilename(title="Select a file") 
    print(selected_file)
    
    root.destroy()

    return selected_file


def read_files(path_01, path_02):

    d = HtmlDiff()

    with open(path_01, "r", encoding="utf-8") as file01:
        with open(path_02, "r", encoding="utf-8") as file02:
        
            lines_from_file01 = file01.readlines()
            lines_from_file02 = file02.readlines()
        
            html_diff = d.make_file(
                lines_from_file01,
                lines_from_file02,
                fromdesc = "file01",
                todesc = "file02")

    return html_diff


def create_output_folder():
    directory = "output"
    parent_dir = os.path.abspath(os.path.join(directory, os.pardir))
    path = os.path.join(parent_dir, directory)

    try:
        os.mkdir(path)
        print(f"Created {directory} folder in {path}")
    except OSError:
        print(f"Folder {directory} already exists in {path}")

    return path

def save_file(path, html_diff):
    file_name = "diff.html"
    html_file_path = os.path.join(path, file_name)

    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(html_diff)
