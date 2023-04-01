import tkinter as tk
from filemenu import FileMenu
from login import Login
from welderlabel import WelderLabel


class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Can Line Assistant')
        self.master.geometry('325x150')
        self.master.resizable(0, 0)
        self.master.configure(bg='deep sky blue')

        # maximize window
        self.master.state('zoomed')
        FileMenu(self.master).create_file_menu()
        # Login(self.master).create_login_window()
        WelderLabel("1234", '987544', 'PP12345', '0.21 05/WHITE2/05 CLEAR', 'fz086456', '0.18 BLUE MOON',
                    'TDA200/004-1', 'LINE 3')


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
