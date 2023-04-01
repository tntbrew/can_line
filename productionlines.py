import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter as tk
from constants import *


class ProductionLine:
    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(self.master)

    def get_all_production_lines(self):
        try:
            DbConnection = sqlite3.connect('canlinedb.mdf')
            DbCursor = DbConnection.cursor()
            DbCursor.execute("SELECT rowid,* FROM production_lines order by line_name")

            records = DbCursor.fetchall()

            return records
        except sqlite3.Error as error:
            print("No line records in sqlite table", error)

        finally:
            DbConnection.commit()
            DbConnection.close()

            return records

    def save_new_line(self):

        conn = sqlite3.connect('canlinedb.mdf')
        c = conn.cursor()
        # data=line
        # sql1='insert into production_lines values (line_name)',self.line_name_textbox.get()
        # sql=("INSERT INTO production_lines(line_name) VALUES (?)")
        c.execute("INSERT INTO production_lines VALUES (:name)",
                  {

                      'name': self.line_name_textbox.get(),

                  })

        conn.commit()
        conn.close()
        self.line_name_textbox.delete(0, tk.END)
        self.display_production_lines()

    def delete_production_line_record(self):
        try:
            DbConnection = sqlite3.connect('canlinedb.mdf')
            DbCursor = DbConnection.cursor()

            DbCursor.execute("DELETE FROM production_lines WHERE oid=" +
                             self.delete_textbox.get())

            DbConnection.commit()
            DbConnection.close()
            self.delete_textbox.delete(0, tk.END)
            self.display_production_lines()
            return True
        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
            return False

    def display_production_lines(self):

        self.tree = ttk.Treeview(self.root, column=("c1", "c2"), show='headings')

        DbConnection = sqlite3.connect('canlinedb.mdf')
        DbCursor = DbConnection.cursor()

        DbCursor.execute("SELECT *,oid FROM production_lines")

        records = DbCursor.fetchall()

        for record in records:
            self.tree.insert("", tk.END, values=record)

        self.tree.column("#1", anchor=tk.CENTER, width=70)
        self.tree.heading("#1", text="Line Name")

        self.tree.column("#2", anchor=tk.CENTER, width=50)
        self.tree.heading("#2", text="Id")

        # attach a Horizontal (x) scrollbar to the frame
        treeXScroll = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        treeXScroll.configure(command=self.tree.xview)
        self.tree.configure(xscrollcommand=treeXScroll.set)

        self.tree.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

        # DbConnection = sqlite3.connect('canlinedb.mdf')
        # DbCursor = DbConnection.cursor()

        # DbCursor.execute("SELECT *,oid FROM production_lines")
        # records = DbCursor.fetchall()

        # print_record = ''
        # for record in records:

        #     print_record += str(record[0])+"\t" + str(record[1])+ "\n"
        # query_label.config(text=print_record)
        # DbConnection.commit()
        # DbConnection.close()

    def edit(self):
        editor = tk.Toplevel(self.master)
        editor.title('Update A Record')

        editor.geometry('250x300')

        editor.update_idletasks()
        width = editor.winfo_width()
        height = editor.winfo_height()
        x = (editor.winfo_screenwidth() // 2) - (width // 2)
        y = (editor.winfo_screenheight() // 2) - (height // 2)
        editor.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        editor.attributes("-topmost", True)

        DbConnection = sqlite3.connect('canlinedb.mdf')
        DbCursor = DbConnection.cursor()
        record_id = self.delete_textbox.get()

        DbCursor.execute("DELETE FROM production_lines WHERE oid=" + record_id)

        records = DbCursor.fetchall()

        for record in records:
            self.line_name_editor_textbox.insert(0, record(0))

        DbConnection.commit()
        DbConnection.close()

        # Create textboxes for form
        self.line_name_editor_textbox = tk.Entry(editor)
        self.line_name_editor_textbox.grid(row=0, column=1)

        # Create labels for form
        line_name_label = tk.Label(editor, text='Line Name:')
        line_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.save_button = tk.Button(editor, text='UpdateRecord', command=None)
        self.save_button.grid(row=2, column=1, columnspan=2, pady=10, ipadx=50)

    def add_line_form(self):

        self.root.title('Production Line Editor')

        self.root.geometry('350x600')

        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.root.attributes("-topmost", True)

        # Create textboxes for form
        self.line_name_textbox = tk.Entry(self.root, font=FONT_SIZE)
        self.line_name_textbox.grid(row=0, column=1)

        # Create labels for form
        line_name_label = tk.Label(self.root, text='Line Name:', font=FONT_SIZE)
        line_name_label.grid(row=0, column=0, pady=5)

        # Create buttons
        submit_button = tk.Button(self.root, text="Add Record", command=lambda: self.save_new_line(), font=FONT_SIZE)
        submit_button.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=105)

        query_button = tk.Button(self.root, text="Show Records", command=lambda: self.display_production_lines(),
                                 font=FONT_SIZE)
        query_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

        delete_label = tk.Label(self.root, text='Record Id:', font=FONT_SIZE)
        delete_label.grid(row=3, column=0, pady=10)

        self.delete_textbox = tk.Entry(self.root, font=FONT_SIZE)
        self.delete_textbox.grid(row=3, column=1)

        delete_button = tk.Button(self.root, text='Delete Record', command=lambda: self.delete_production_line_record(),
                                  font=FONT_SIZE)
        delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

        edit_button = tk.Button(self.root, text='Edit Record', command=lambda: self.edit(), font=FONT_SIZE)
        edit_button.grid(row=5, column=0, columnspan=2, pady=10, ipadx=110)

        # self.query_label = tk.Label(self.root, text='###')
        # self.query_label.grid(row=7, column=0, columnspan=2)
        self.display_production_lines()
