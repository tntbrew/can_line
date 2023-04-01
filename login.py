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


class Login:
    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)

    def disable_event(self):
        self.root.withdraw()
        self.master.focus_force()

    def validate_login(self, root):

        username = self.username_combo.get()
        temp_password = self.userpassword_textbox.get()

        # Hash the encoded password and generate a salt:
        temp_password = temp_password.encode('utf-8')

        DbConnection = sqlite3.connect('canlinedb.mdf')
        DbCursor = DbConnection.cursor()
        DbCursor.execute("SELECT * FROM user where user_name = ?", (username,))

        user_record = DbCursor.fetchall()
        logged_on_user_name = self.username_combo.get()

        DbConnection.close()

        for userlogin in user_record:

            if bcrypt.checkpw(temp_password, userlogin[1]):

                # admin
                if userlogin[2] == USER_ACCESS_CODES[2]:
                    AdminMenu(self.master, logged_on_user_name).create_admin_menu()

                    self.close_window(root, self.master)
                    return True

                # can maker
                if userlogin[2] == USER_ACCESS_CODES[1]:
                    CanMakerMenu(self.master).create_can_maker_menu()
                    self.close_window()
                    return True

                # operator
                if userlogin[2] == USER_ACCESS_CODES[0]:
                    OperatorMenu(self.master).create_operator_menu()
                    self.root.destroy()
                    # self.close_window()
                    return True

                return True

            else:
                messagebox.showerror('Error', 'login failed.Try again', parent=self.root)
                self.userpassword_textbox.delete(0, tk.END)
                return

    def close_window(self, root, main):
        root.withdraw()
        main.focus_force()

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

        usersname_list = list()
        usernames = list()

        # get user names from database table
        usernames = UserManager(self.master).get_user_names()
        # UserManager.destroy()

        # loop thru user names and append them to the users_names list

        for user in usernames:
            usersname_list.append(user[0])

        # create labels for form
        username_label = tk.Label(self.root, text='User Name:', bg='#D9D8D7', font=FONT_SIZE)  # bg='grey',
        username_label.grid(row=0, column=0, padx=10, pady=10)

        userpassword_label = tk.Label(self.root, text='Password:', bg='#D9D8D7', font=FONT_SIZE)  # ,bg='grey')
        userpassword_label.grid(row=1, column=0, padx=10, pady=10)

        # create textboxes for form
        self.username_combo = ttk.Combobox(self.root, width=18, font=FONT_SIZE)
        self.username_combo['values'] = usersname_list
        self.username_combo.current(0)
        self.username_combo.grid(row=0, column=1)

        self.userpassword_textbox = tk.Entry(self.root, show='*', font=FONT_SIZE)
        self.userpassword_textbox.grid(row=1, column=1)

        # create log on button
        submit_button = tk.Button(self.root, text="Login", font=FONT_SIZE,
                                  command=lambda: self.validate_login(self.root))
        submit_button.grid(row=2, column=0, columnspan=2, pady=10, padx=20, ipadx=60)
        self.root.bind('<Return>', lambda event: self.validate_login(self.root))
        self.userpassword_textbox.focus()
