import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from adminmenu import AdminMenu
from constants import *
from canmakermenu import CanMakerMenu
from operatormenu import OperatorMenu
from usermanager import UserManager
import bcrypt


def close_window(root, main):
    root.withdraw()
    main.focus_force()


class Login:
    def __init__(self, master):
        self.user_password_textbox = None
        self.username_combo = None
        self.master = master
        self.root = tk.Toplevel(self.master)

    def disable_event(self):
        self.root.withdraw()
        self.master.focus_force()

    def validate_login(self, root):

        username = self.username_combo.get()
        temp_password = self.user_password_textbox.get()

        # Hash the encoded password and generate a salt:
        temp_password = temp_password.encode('utf-8')

        DbConnection = sqlite3.connect('canlinedb.mdf')
        DbCursor = DbConnection.cursor()
        DbCursor.execute("SELECT * FROM user where user_name = ?", (username,))

        user_record = DbCursor.fetchall()
        logged_on_user_name = self.username_combo.get()

        DbConnection.close()

        for user_login in user_record:

            if bcrypt.checkpw(temp_password, user_login[1]):

                # admin
                if user_login[2] == USER_ACCESS_CODES[2]:
                    AdminMenu(self.master, logged_on_user_name).create_admin_menu()

                    close_window(root, self.master)
                    return True

                # can maker
                if user_login[2] == USER_ACCESS_CODES[1]:
                    CanMakerMenu(self.master).create_can_maker_menu()
                    close_window(root, self.master)
                    return True

                # operator
                if user_login[2] == USER_ACCESS_CODES[0]:
                    OperatorMenu(self.master).create_operator_menu()
                    self.root.destroy()
                    # self.close_window()
                    return True

                return True

            else:
                messagebox.showerror('Error', 'login failed.Try again', parent=self.root)
                self.user_password_textbox.delete(0, tk.END)
                return

    def create_login_window(self):

        self.root.config(bg='#D9D8D7')
        self.root.title('Login')
        self.root.attributes('-topmost', True)
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.disable_event())
        self.root.geometry('350x150')
        self.root.resizable(0, 0)
        self.root.update_idletasks()

        # self.root.configure(bg='grey')
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 1)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.deiconify()

        users_name_list = list()

        # get usernames from database table
        usernames = UserManager(self.master).get_user_names()

        # loop through usernames and append them to the users_names list
        for user in usernames:
            users_name_list.append(user[0])

        # create labels for form
        username_label = tk.Label(self.root, text='User Name:', bg='#D9D8D7', font=FONT_SIZE)  # bg='grey',
        username_label.grid(row=0, column=0, padx=10, pady=10)

        user_password_label = tk.Label(self.root, text='Password:', bg='#D9D8D7', font=FONT_SIZE)  # ,bg='grey')
        user_password_label.grid(row=1, column=0, padx=10, pady=10)

        # create text boxes for form
        self.username_combo = ttk.Combobox(self.root, width=18, font=FONT_SIZE)
        self.username_combo['values'] = users_name_list
        self.username_combo.current(0)
        self.username_combo.grid(row=0, column=1)

        self.user_password_textbox = tk.Entry(self.root, show='*', font=FONT_SIZE)
        self.user_password_textbox.grid(row=1, column=1)

        # create log on button
        submit_button = tk.Button(self.root, text="Login", font=FONT_SIZE,
                                  command=lambda: self.validate_login(self.root))
        submit_button.grid(row=2, column=0, columnspan=2, pady=10, padx=20, ipadx=60)
        self.root.bind('<Return>', lambda event: self.validate_login(self.root))
        self.user_password_textbox.focus()
