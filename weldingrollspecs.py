import tkinter as tk
import sqlite3
from tkinter import ttk
import datetime

class WeldingRollSpecifications:
    def __init__(self, master, username):

        self.master = master
        self.username = username
        self.root = tk.Toplevel(self.master)

    def create_welding_roll_specs_form(self):

        self.root.title('Welding Roll Specs Form')
        self.root.geometry('1200x600')
        self.root.update_idletasks()  # Add this line
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.root.attributes("-topmost", True)

        production_line = list()

        production_lines = ProductionLine(self.master).get_all_production_lines()

        for line in production_lines:
            production_line.append(line[1])

        fnt = ("Comic Sans MS", 11)

        lw = 35

        # Create labels for form
        line_number_label = tk.Label(self.root, text='Line Number', width=lw, anchor='e', font=fnt)
        line_number_label.grid(row=0, column=0, pady=10)

        top_roll_maximum_diameter_label = tk.Label(self.root, text='Top Welding Roll Maximum Diameter:', width=lw,
                                                   anchor='e', font=fnt)
        top_roll_maximum_diameter_label.grid(row=1, column=0, pady=10)

        top_roll_minimum_diameter_label = tk.Label(self.root, text='Top Welding Roll Maximum Diameter:', width=lw,
                                                   anchor='e', font=fnt)
        top_roll_minimum_diameter_label.grid(row=2, column=0, pady=10)

        top_roll_profile_maximum_depth_label = tk.Label(self.root, text='Top Welding Roll Maximum Profile Depth:',
                                                        width=lw, anchor='e', font=fnt)
        top_roll_profile_maximum_depth_label.grid(row=3, column=0, pady=10)

        top_roll_profile_minimum_depth_label = tk.Label(self.root, text='Top Welding Roll Minimum Profile Depth:',
                                                        width=lw, anchor='e', font=fnt)
        top_roll_profile_minimum_depth_label.grid(row=4, column=0, pady=10)

        top_roll_offset_label = tk.Label(self.root, text='Top Welding Roll Offset:', width=lw, anchor='e', font=fnt)
        top_roll_offset_label.grid(row=5, column=0, pady=10)

        bottom_roll_maximum_diameter_label = tk.Label(self.root, text='Bottom Welding Roll Maximum Diameter:', width=45,
                                                      anchor='e', font=fnt)
        bottom_roll_maximum_diameter_label.grid(row=1, column=3, pady=10)

        bottom_roll_minimum_diameter_label = tk.Label(self.root, text='Bottom Welding Roll Minimum Diameter:', width=45,
                                                      anchor='e', font=fnt)
        bottom_roll_minimum_diameter_label.grid(row=2, column=3, pady=10)

        bottom_roll_maximum_profile_depth_label = tk.Label(self.root, text='Bottom Welding Maximum Roll Profile Depth:',
                                                           width=45, anchor='e', font=fnt)
        bottom_roll_maximum_profile_depth_label.grid(row=3, column=3, pady=10)

        bottom_roll_minimum_profile_depth_label = tk.Label(self.root, text='Bottom Welding Minimum Roll Profile Depth:',
                                                           width=45, anchor='e', font=fnt)
        bottom_roll_minimum_profile_depth_label.grid(row=4, column=3, pady=10)

        top_roll_offset_label = tk.Label(self.root, text='Top Welding Roll Offset:', width=lw, anchor='e', font=fnt)
        top_roll_offset_label.grid(row=5, column=3, pady=10)

        # Create data entry boxes for form

        self.line_number_combobox = ttk.Combobox(self.root)
        self.line_number_combobox['values'] = production_line
        self.line_number_combobox.grid(row=0, column=1)

        self.top_roll_maximum_diameter_textbox = tk.Entry(self.root, width=23)
        self.top_roll_maximum_diameter_textbox.grid(row=1, column=1)

        self.top_roll_minimum_diameter_textbox = tk.Entry(self.root, width=23)
        self.top_roll_minimum_diameter_textbox.grid(row=2, column=1)

        self.top_roll_profile_maximum_depth_textbox = tk.Entry(self.root, width=23)
        self.top_roll_profile_maximum_depth_textbox.grid(row=3, column=1)

        self.top_roll_profile_minimum_depth_textbox = tk.Entry(self.root, width=23)
        self.top_roll_profile_minimum_depth_textbox.grid(row=4, column=1)

        self.top_roll_offset_textbox = tk.Entry(self.root, width=23)
        self.top_roll_offset_textbox.grid(row=5, column=1)

        self.bottom_roll_maximum_diameter_textbox = tk.Entry(self.root, width=23)
        self.bottom_roll_maximum_diameter_textbox.grid(row=1, column=4)

        self.bottom_roll_minimum_diameter_textbox = tk.Entry(self.root, width=23)
        self.bottom_roll_minimum_diameter_textbox.grid(row=2, column=4)

        self.bottom_roll_maximum_profile_depth_textbox = tk.Entry(self.root, width=23)
        self.bottom_roll_maximum_profile_depth_textbox.grid(row=3, column=4)

        self.bottom_roll_minimum_profile_depth_textbox = tk.Entry(self.root, width=23)
        self.bottom_roll_minimum_profile_depth_textbox.grid(row=4, column=4)

        self.jig_textbox = tk.Entry(self.root, width=23)
        self.jig_textbox.grid(row=5, column=4)

        # Create tk.Buttons
        self.save_button = tk.Button(self.root, text="Save Record", font=fnt,
                                     command=None)  # lambda:validate_roll_change_data_entry(self.root))
        self.save_button.grid(row=6, column=2, columnspan=2, ipadx=200)

        self.viewrecords_button = tk.Button(self.root, text='View All Records', font=fnt,
                                            command=None)  # lambda:display_records())
        self.viewrecords_button.grid(row=7, column=2, columnspan=2, pady=10, ipadx=190)

    def get_bottom_roll_maximum_diameter(self, line_id):
        try:
            DbConnection = sqlite3.connect('canlinedb.mdf')

            DbCursor = DbConnection.cursor()

            DbCursor.execute(
                "SELECT bottom_roll_maximum_diameter FROM welding_roll_specifications where line_name=" + line_id)

            bottom_roll_maximum_diameter = DbCursor.fetchall()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)


        finally:
            if DbConnection:
                DbConnection.commit()
                DbConnection.close()
                print("The SQLite connection is closed")

        DbConnection.commit()
        DbConnection.close()
        return bottom_roll_maximum_diameter

    def get_jig_measurement(self, line_id):
        try:
            DbConnection = sqlite3.connect('canlinedb.mdf')

            DbCursor = DbConnection.cursor()

            DbCursor.execute("SELECT jig_setting FROM welding_roll_specifications where line_name=" + line_id)

            jig_measurement = DbCursor.fetchall()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)


        finally:
            if DbConnection:
                DbConnection.commit()
                DbConnection.close()
                print("The SQLite connection is closed")
                return jig_measurement

    def get_roll_offset(self, line_id):
        try:
            DbConnection = sqlite3.connect('canlinedb.mdf')

            DbCursor = DbConnection.cursor()

            DbCursor.execute("SELECT top_roll_offset FROM welding_roll_specifications where line_name=" + line_id)

            offset = DbCursor.fetchall()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)


        finally:
            if DbConnection:
                DbConnection.commit()
                DbConnection.close()
                print("The SQLite connection is closed")
                DbConnection.commit()
                DbConnection.close()
                return offset

    def save_record(self):
        DbConnection = sqlite3.connect('canlinedb.mdf')
        DbCursor = DbConnection.cursor()
        # data=line

        # sql=("INSERT INTO production_lines(line_name) VALUES (?)")
        DbCursor.execute(
            'insert into welding_roll_specifications values (:date,:line,:user,:trmaxd,:trmind,:trmaxp,:trminp,:jig,:offset,:brmaxd,:brmind,:brmaxp,:brminp)',
            {
                'date': datetime('now'),
                'line': self.line_number_combobox.get(),
                'user': self.username,
                'trmaxd': float(self.top_roll_maximum_diameter_textbox.get()),
                'trmind': float(self.top_roll_minimum_diameter_textbox.get()),
                'trmaxp': float(self.top_roll_profile_maximum_depth_textbox.get()),
                'trminp': float(self.top_roll_profile_minimum_depth_textbox.get()),
                'jig': float(self.jig_textbox.get()),
                'offset': float(self.top_roll_offset_textbox.get()),
                'brmaxd': float(self.bottom_roll_maximum_diameter_textbox.get()),
                'brmind': float(self.bottom_roll_minimum_diameter_textbox.get()),
                'brmaxp': float(self.bottom_roll_maximum_profile_depth_textbox.get()),
                'brminp': float(self.bottom_roll_minimum_profile_depth_textbox.get())

            })

        DbConnection.commit()
        DbConnection.close()