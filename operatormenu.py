import tkinter as tk


class OperatorMenu:
    def __init__(self, master):
        self.master = master

    def _close(self):
        self.destroy()

    def create_operator_menu(self):
        menubar = tk.Menu(self.master, background='#ff8000', foreground='black', activebackground='white',
                          activeforeground='black')

        file = tk.Menu(menubar)

        file.add_command(label='Exit', underline=1, accelerator='Ctrl+Q', command=quit)

        menubar.add_cascade(label="File", menu=file)

        self.master.bind_all("<Control-q>", lambda event: quit())

        self.master.config(menu=menubar)
        rollchange = tk.Menu(menubar)

        rollchange.add_command(label='Line 1', command=None)

        menubar.add_cascade(label="Welding Roll Change", menu=rollchange)

        self.master.config(menu=menubar)
        return
