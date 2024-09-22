# PYTHON VERSION: 3.11.9

import os.path
import tkinter as tk
from tkinter.messagebox import askyesno
import json

import backend as bkd
import utils.utiles as util


class App:

    logger = ""

    path_dict = os.path.join("texts", "strings.json")
    with open(path_dict, "r", encoding="utf-8") as file:
            strings = json.load(file)

    text_logger = strings["text"]


    def __init__(self):

        self.first_directory = None
        self.second_directory = None

        self.main_window = tk.Tk()
        self.main_window.geometry("1024x400")
        self.main_window.title(self.text_logger["title"])
        self.main_window.configure(bg="#1a242b")
        self.main_window.resizable(False, False)

        self.first_main_window = util.get_button(self.main_window, self.text_logger["first_path"], "green", self.first_path_button)
        self.first_main_window.place(x=860, y=35)

        self.second_main_window = util.get_button(self.main_window, self.text_logger["second_path"], "green", self.second_path_button)
        self.second_main_window.place(x=860, y=80)

        self.execute_main_window = util.get_button(self.main_window, self.text_logger["run"], "red", self.execute_button)
        self.execute_main_window.config(state=tk.DISABLED)
        self.execute_main_window.place(x=860, y=125)

        self.label_border = tk.Frame(self.main_window, bg="#f0f0f0", relief="sunken", bd=2)
        self.label_text = tk.Label(self.label_border, font=("Consolas", 10), justify="left", anchor="nw", width=115, height=35, bg="#131313", fg="#f0f0f0")
        self.label_text.pack(fill="both", expand=True, padx=1, pady=1)
        self.label_border.pack(anchor="nw", padx=15, pady=15)
        self.output()


    def first_path_button(self):
        self.first_directory = bkd.select_file()
        self.switch_state()

        self.logger += self.text_logger["selected_first_message"].format(first_directory=self.first_directory)+"\n"


    def second_path_button(self):
        self.second_directory = bkd.select_file()
        self.switch_state()

        self.logger += self.text_logger["selected_second_message"].format(second_directory=self.second_directory)+"\n"


    def execute_button(self):
        answer_execute = askyesno(self.text_logger["run"], self.text_logger["checking_message"])

        if answer_execute:
            self.logger += self.text_logger["start_message"]+"\n"
            html_diff = bkd.read_files(self.first_directory, self.second_directory)
            self.logger += self.text_logger["comparison_message"]+"\n"
            output_directory = bkd.create_output_folder()
            bkd.save_file(output_directory, html_diff)
            self.logger += self.text_logger["html_message"]+"\n"
        else:
            pass


    def switch_state(self):
        if self.first_directory == None or self.second_directory == None:
            self.execute_main_window.config(state=tk.DISABLED)
        else:
            self.execute_main_window.config(state=tk.NORMAL)


    def output(self):
        self.label_text.config(text=self.logger)
        self.main_window.after(1000, self.output)


    def exit_button(self):
        answer_exit = askyesno(self.text_logger["exit"], self.text_logger["checking_message"])

        if answer_exit:
            self.main_window.destroy()
        else:
            pass


    def start(self):
        self.main_window.protocol("WM_DELETE_WINDOW", self.exit_button)
        self.main_window.mainloop()
