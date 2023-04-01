import tkinter as tk
from productionlines import ProductionLine


class AdminMenu:

    def __init__(self, master, username):
        self.master = master
        self.username = username

    def create_admin_menu(self):
        self.menubar = tk.Menu(self.master, background='#ff8000', foreground='black', activebackground='white',
                               activeforeground='black')

        file = tk.Menu(self.menubar)

        file.add_command(label='Exit', underline=1, accelerator='Ctrl+Q', command=quit)

        self.menubar.add_cascade(label="File", menu=file)

        self.master.bind_all("<Control-q>", lambda event: quit())

        self.master.config(menu=self.menubar)

        rollchange = tk.Menu(self.menubar)

        rollchange.add_command(label='New', command=lambda: WeldingRollChange(self.master).create_roll_change_form())

        self.menubar.add_cascade(label="Welding Roll Change", menu=rollchange)

        self.master.config(menu=self.menubar)

        canmaker = tk.Menu(self.menubar)
        canmaker.add_command(label='Welding Roll Specs', command=lambda: WeldingRollSpecifications(self.master,
                                                                                                   self.username).create_welding_roll_specs_form)

        self.menubar.add_cascade(label="Specifications", menu=canmaker)

        tools = tk.Menu(self.menubar)

        tools.add_command(label='Add User', command=lambda: UserManager(self.master).create_new_user_form)

        tools.add_command(label='Add City', command=None)

        tools.add_command(label='New Code Change tk.Labels', command=None)

        tools.add_command(label='Add Country', command=None)

        tools.add_command(label='Add Branch', command=None)

        tools.add_command(label='Add Line', command=lambda: ProductionLine(self.master).add_line_form())

        self.menubar.add_cascade(label="Tools", menu=tools)
