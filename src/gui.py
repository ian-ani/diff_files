# PYTHON VERSION: 3.12.0

import os.path
import tkinter as tk
from tkinter.messagebox import askyesno
import json

import core
import utils.utiles as util
import constants as c

class App:

    # Logger
    log = ""
    lines = 0

    # UI texts
    path_dict = os.path.join("texts", "strings.json")
    with open(path_dict, "r", encoding="utf-8") as f:
        strings = json.load(f)
    ui_text = strings["text"]

    def __init__(self):
        # Files
        self.first_file = None
        self.second_file = None
        self.output_file = None

        # Main window
        self.main_window = tk.Tk()
        self.main_window.geometry(c.WINDOW_GEOMETRY)
        self.main_window.title(self.ui_text["title"])
        self.main_window.configure(bg=c.WINDOW_BG_COLOR)
        self.main_window.resizable(False, False)

        # Buttons
        self.first_main_window = util.get_button(self.main_window, self.ui_text["first_file"], c.BUTTON_COLOR[0], 
                                                lambda: self.get_file_button("selected_first_message", "first_file"))
        self.first_main_window.place(x=c.START_X, y=c.START_Y)

        self.second_main_window = util.get_button(self.main_window, self.ui_text["second_file"], c.BUTTON_COLOR[0], 
                                                lambda: self.get_file_button("selected_second_message", "second_file"))
        self.second_main_window.place(x=c.START_X, y=c.START_Y + c.STEP_Y)

        self.output_main_window = util.get_button(self.main_window, self.ui_text["save"], c.BUTTON_COLOR[0], self.output_button)
        self.output_main_window.place(x=c.START_X, y=c.START_Y + c.STEP_Y * 2)

        self.run_main_window = util.get_button(self.main_window, self.ui_text["run"], c.BUTTON_COLOR[1], self.run_button)
        self.run_main_window.config(state=tk.DISABLED)
        self.run_main_window.place(x=c.START_X, y=c.START_Y + c.STEP_Y * 3)

        # Logger
        self.label_border = tk.Frame(self.main_window, bg=c.LOGGER_BORDER_COLOR, relief="sunken", bd=2)
        self.label_text = tk.Label(self.label_border, font=(c.FONT_FAMILY, c.FONT_SIZE), justify="left", anchor="nw", width=c.LOGGER_WIDTH, 
                                   height=c.LOGGER_HEIGHT, bg=c.FONT_BG_COLOR, fg=c.FONT_COLOR)
        self.label_text.pack(fill="both", expand=True, padx=1, pady=1)
        self.label_border.pack(anchor="nw", padx=c.PADDING, pady=c.PADDING)
        self.create_log()

    # Asks user which file to compare
    def get_file_button(self, key, number):
        self.directory = core.select_file()

        setattr(self, number, self.directory)
        self.write_log(key, directory=getattr(self, number))

        self.switch_state()

    # Asks user where to save a diff file
    def output_button(self):
        self.output_file = core.set_output_file()
        self.write_log("selected_output_file", output_file=self.output_file)

    # Compares both files
    def run_button(self):
        answer = askyesno(self.ui_text["run"], self.ui_text["checking"])

        if answer:
            self.write_log("start_checking")
            html_diff = core.read_files(self.first_file, self.second_file)
            
            if html_diff:
                self.write_log("end_checking")
            else:
                self.write_log("wrong_format")
                return

        if not self.output_file:
            filename = core.create_output_folder()
            core.save_file(html_diff, filename)
        else:
            core.save_file(html_diff, self.output_file)

        self.write_log("generated_report")

    # Blocked until both files have been selected
    def switch_state(self):
        if not self.first_file or not self.second_file:
            self.run_main_window.config(state=tk.DISABLED)
        else:
            self.run_main_window.config(state=tk.NORMAL)

    # Logger
    def create_log(self):
        self.label_text.config(text=self.log)
        self.main_window.after(1000, self.create_log)

    def write_log(self, message, **kwargs):
        if self.lines == c.MAX_NUM_LINES:
            self.clean_log()
            self.lines = 0

        self.log += self.ui_text[message].format(**kwargs)+"\n"
        self.lines += 1
        
    def clean_log(self):
        self.log = ""

    # Closes program
    def exit_button(self):
        answer = askyesno(self.ui_text["exit"], self.ui_text["checking"])

        if answer:
            self.main_window.destroy()

    # Starts program
    def start(self):
        self.main_window.protocol("WM_DELETE_WINDOW", self.exit_button)
        self.main_window.mainloop()
