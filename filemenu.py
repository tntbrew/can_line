import tkinter as tk
from constants import *
class FileMenu:
    def __init__(self, master):
        self.master = master

    def create_file_menu(self):
        menubar = tk.Menu(self.master, background='blue', foreground='red', activebackground='blue',
                          activeforeground='black')
        file = tk.Menu(menubar)

        file.add_command(label='Exit', font=FONT_SIZE, underline=1, accelerator='Ctrl+Q', command=lambda: quit())

        menubar.add_cascade(label="File", menu=file)

        self.master.bind_all("<Control-q>",
                             lambda event: quit())

        self.master.config(menu=menubar)