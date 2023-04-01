import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from productionlines import ProductionLine


class WeldingRollChange:
    def __init__(self, master):
        self.tree = None
        self.top_roll_position_text = None
        self.zbarsetting_text = None
        self.top_roll_jig_text = None
        self.trpos_edit_textbox = None
        self.viewrecords_button = None
        self.save_button = None
        self.bottom_probechanged_checkbox = None
        self.bottom_roll_profile_depth_textbox = None
        self.bottom_roll_diameter_textbox = None
        self.bottom_roll_number_textbox = None
        self.top_probe_changed_checkbox = None
        self.top_roll_offset_textbox = None
        self.top_roll_profile_depth_textbox = None
        self.top_roll_diameter_textbox = None
        self.top_roll_number_textbox = None
        self.line_number_combobox = None
        self.master = master
        self.root = tk.Toplevel(self.master)

    def check_string_is_float(self, result):
        try:
            integer_result = int(result)
        except ValueError:
            return tk.FALSE
        else:
            return tk.TRUE

    def create_roll_change_form(self):

        self.root.title('Roll Change Form')
        self.root.geometry('1050x600')
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

        # Define empty variables for checkboxes
        var_top_probe_changed = tk.IntVar()
        var_bottom_probe_changed = tk.IntVar()

        # Create labels for form
        line_number_label = tk.Label(self.root, text='Line Number', width=25, anchor='e')
        line_number_label.grid(row=0, column=0, pady=10)

        top_roll_number_label = tk.Label(self.root, text='Top Welding Roll Number:', width=25, anchor='e')
        top_roll_number_label.grid(row=1, column=0, padx=10, pady=10)

        top_roll_diameter_label = tk.Label(self.root, text='Top Welding Roll Diameter:', width=25, anchor='e')
        top_roll_diameter_label.grid(row=2, column=0, pady=10)

        top_roll_profile_depth_label = tk.Label(self.root, text='Top Welding Roll Profile Depth:', width=25, anchor='e')
        top_roll_profile_depth_label.grid(row=3, column=0, pady=10)

        top_roll_offset_label = tk.Label(self.root, width=25, text='Top Welding Roll Offset', anchor='e')
        top_roll_offset_label.grid(row=4, column=0, pady=10)

        bottom_roll_number_label = tk.Label(self.root, text='Bottom Roll Number:', width=25, anchor='e')
        bottom_roll_number_label.grid(row=1, column=3, padx=10, pady=20)

        bottom_roll_diameter_label = tk.Label(self.root, text='Bottom Welding Roll Diameter:', width=25, anchor='e')
        bottom_roll_diameter_label.grid(row=2, column=3, pady=10)

        bottom_roll_profile_depth_label = tk.Label(self.root, text='Bottom Welding Roll Profile Depth:', width=25,
                                                   anchor='e')
        bottom_roll_profile_depth_label.grid(row=3, column=3, pady=10)

        trpos_label = tk.Label(self.root, text='Top Roll Position:',
                               anchor='e')  # , bg=BG_COLOR,font=("Arial 11 bold "))
        trpos_label.grid(row=8, column=0, pady=10, sticky='e')

        top_roll_jig_label = tk.Label(self.root, text='Jig To Roll Measurement:',
                                      anchor='e')  # ,bg=BG_COLOR,font=("Arial 11 bold "))
        top_roll_jig_label.grid(row=9, column=0, pady=10, sticky='e')

        zbar_setting_label = tk.Label(self.root, text='Z-Bar Setting:')  # ,bg=BG_COLOR,font=("Arial 11 bold "))
        zbar_setting_label.grid(row=10, column=0, pady=10, sticky='e')

        top_roll_position_label = tk.Label(self.root,
                                           text='Top Roll Position:')  # ,bg=BG_COLOR,font=("Arial 11 bold "))
        top_roll_position_label.grid(row=11, column=0, pady=10, sticky='e')

        # Create data tk.Entry boxes

        self.line_number_combobox = ttk.Combobox(self.root)
        self.line_number_combobox['values'] = production_line
        self.line_number_combobox.grid(row=0, column=1)

        self.top_roll_number_textbox = tk.Entry(self.root, width=23)
        self.top_roll_number_textbox.grid(row=1, column=1)

        self.top_roll_diameter_textbox = tk.Entry(self.root, width=23)
        self.top_roll_diameter_textbox.grid(row=2, column=1)

        self.top_roll_profile_depth_textbox = tk.Entry(self.root, width=23)
        self.top_roll_profile_depth_textbox.grid(row=3, column=1)

        self.top_roll_offset_textbox = tk.Entry(self.root, width=23)
        self.top_roll_offset_textbox.grid(row=4, column=1)

        self.top_probe_changed_checkbox = tk.Checkbutton(self.root, text='Top Probe Changed?',
                                                         variable=var_top_probe_changed, onvalue=1,
                                                         offvalue=0)  # ,bg=BG_COLOR, font=(LABEL_FONT))
        self.top_probe_changed_checkbox.grid(row=5, column=1, pady=10)

        self.bottom_roll_number_textbox = tk.Entry(self.root, width=23)
        self.bottom_roll_number_textbox.grid(row=1, column=4)

        self.bottom_roll_diameter_textbox = tk.Entry(self.root, width=23)
        self.bottom_roll_diameter_textbox.grid(row=2, column=4)

        self.bottom_roll_profile_depth_textbox = tk.Entry(self.root, width=23)
        self.bottom_roll_profile_depth_textbox.grid(row=3, column=4)

        self.bottom_probechanged_checkbox = tk.Checkbutton(self.root, text='Bottom Probe Changed?',
                                                           variable=var_bottom_probe_changed, onvalue=1,
                                                           offvalue=0)  # ,bg=BG_COLOR,font=(LABEL_FONT),anchor="w")
        self.bottom_probechanged_checkbox.grid(row=4, column=4, pady=10)

        # Create Buttons
        self.save_button = tk.Button(self.root, text="Save Record",
                                     command=None)  # lambda:validate_roll_change_data_entry(self.root))
        self.save_button.grid(row=6, column=1, columnspan=2)

        self.viewrecords_button = tk.Button(self.root, text='view all records',
                                            command=lambda: self.display_all_records)
        self.viewrecords_button.grid(row=12, column=1, columnspan=2)

        separator = ttk.Separator(self.root, orient='horizontal')
        separator.grid(row=7, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

        self.trpos_edit_textbox = tk.Entry(self.root, width=25, state=tk.DISABLED)
        self.trpos_edit_textbox.grid(row=8, column=1)

        self.top_roll_jig_text = tk.Entry(self.root, width=25, state=tk.DISABLED)
        self.top_roll_jig_text.grid(row=9, column=1)

        self.zbarsetting_text = tk.Entry(self.root, width=25, state=tk.DISABLED)
        self.zbarsetting_text.grid(row=10, column=1)

        self.top_roll_position_text = tk.Entry(self.root, width=25, state=tk.DISABLED)
        self.top_roll_position_text.grid(row=11, column=1)

    def convert_to_float(string):
        return float(string)

    def display_all_records(self):

        self.tree = ttk.Treeview(self.root, column=("c1", "c2", "c3", "C4", "c5", "c6", "c7", "c8", "c9", "c10"),
                                 show='headings')

        DbConnection = sqlite3.connect('canlinedb.mdf')
        DbCursor = DbConnection.cursor()

        DbCursor.execute("SELECT *,oid FROM user")

        records = DbCursor.fetchall()

        for record in records:
            self.tree.insert("", tk.END, values=record)

        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Date")

        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Name")

        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Top Roll Id")

        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Top Roll Dia.")

        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Top Roll Dia.")

        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="Top Roll Profile.")

        self.tree.column("#6", anchor=tk.CENTER)
        self.tree.heading("#6", text="Top Roll Pos.")

        self.tree.column("#7", anchor=tk.CENTER)
        self.tree.heading("#7", text="Bottom Roll Id.")

        self.tree.column("#8", anchor=tk.CENTER)
        self.tree.heading("#8", text="Bottom Roll Dia.")

        self.tree.column("#9", anchor=tk.CENTER)
        self.tree.heading("#9", text="Top Probe.")

        self.tree.column("#10", anchor=tk.CENTER)
        self.tree.heading("#10", text="Bottom Probe.")

        # attach a Horizontal (x) scrollbar to the frame
        treeXScroll = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        treeXScroll.configure(command=self.tree.xview)
        self.tree.configure(xscrollcommand=treeXScroll.set)

        self.tree.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    def get_radius(self, diameter):

        result = diameter / 2
        radius = round(result, 2)

        return radius

    def validate_dataself(self):

        # Check top roll diameter data entry
        if self.check_string_is_float(self.top_roll_diameter_textbox.get()):

            top_roll_diameter = self.convert_to_float(self.top_roll_diameter_textbox.get())

            top_roll_radius = self.get_radius(top_roll_diameter)

        else:
            tk.messagebox.showerror('Value Error',
                                    self.top_roll_diameter_textbox.get() + ' is not a valid value! \n Please try again')

            # Check top roll profile data entry
        if self.check_string_is_float(self.top_roll_profile_depth_textbox.get()):

            top_roll_profile = self.convert_to_float(self.top_roll_profile_depth_textbox.get())

        else:
            tk.messagebox.showerror('Value Error',
                                    self.top_roll_profile_depth_textbox.get() + ' is not a valid value! \n Please try again')

            # Check bottom roll diameter  entry
        if self.check_string_is_float(self.bottom_roll_diameter_textbox.get()):

            bottom_roll_diameter = self.convert_to_float(self.bottom_roll_diameter_textbox.get())

        else:
            tk.messagebox.showerror('Value Error',
                                    self.bottom_roll_diameter_textbox.get() + ' is not a valid value! \n Please try again')

            # Check bottom roll profile data entry
        if self.check_string_is_float(self.bottom_roll_profile_depth_textbox.get()):

            bottom_roll_profile = self.convert_to_float(self.bottom_roll_profile_depth_textbox.get())

        else:
            tk.messagebox.showerror('Value Error',
                                    self.bottom_roll_profile_depth_textbox.get() + ' is not a valid value! \n Please try again')

        self.display_settings_to_user()
