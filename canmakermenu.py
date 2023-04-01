import tkinter as tk


class CanMakerMenu:
    def __init__(self, master):
        self.master = master

    def create_can_maker_menu(self):
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

        canmaker = tk.Menu(menubar)

        canmaker.add_command(label='Welding Roll Specs', command=None)

        menubar.add_cascade(label="Specifications", menu=canmaker)
        return
