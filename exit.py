from tkinter import Frame, Label, Entry, Button, END
from tkinter import messagebox
import datetime
from functions import clear, forget, get_values, Search
import pandas
from auxillary_sec import StockCheck

BACKGROUND_COLOR = "#949494"

domain = ["Masonry", "Plumbing", "Electrical", "Tiling", "Ceiling", "Painting", "Equipments", "Water Proofing", "Others", "Scaffolding"]

FONT1 = ("Century Gothic", 20, "bold")
FONT2 = ("Century Gothic", 12, "bold")
FONT3 = ("Century Gothic", 10, "bold")
FONT4 = ("Century Gothic", 8, "bold")

class ExitTab():
    """This class is responsible for the entire EXIT section"""
    def __init__(self, frame:Frame, search:Search, update:StockCheck):

        self.exit_find = search
        self.frame = frame
        self.update = update

        self.exit_label = Label(master=self.frame, text="EXIT", font=FONT1, bg=BACKGROUND_COLOR)
        self.exit_label.place(x=300, y=0)

        self.exit_material_label = Label(master=self.frame, text="Material: ", font=FONT3, bg=BACKGROUND_COLOR)
        self.exit_material_label.place(x=5, y=70)

        self.material_name_entry = Entry(master=self.frame, width=35)
        self.material_name_entry.place(x=110, y=70)

        self.exit_mat_cat_label = Label(master=self.frame, text="Domain: ", font=FONT3, bg=BACKGROUND_COLOR)
        self.exit_mat_cat_label.place(x=5, y=130)

        self.material_cat = Entry(master=self.frame, width=35)
        self.material_cat.place(x=110, y=130)

        self.material_unit_label = Label(master=self.frame, text="Unit:", font=FONT3, bg=BACKGROUND_COLOR)
        self.material_unit_label.place(x=5, y=190)

        self.material_unit = Entry(master=self.frame)
        self.material_unit.place(x=110, y=190)

        self.exit_current_qty_label = Label(master=self.frame, text="Current Qty:", font=FONT3, bg=BACKGROUND_COLOR)
        self.exit_current_qty_label.place(x=5, y=250)

        self.material_current_qty = Entry(master=self.frame)
        self.material_current_qty.place(x=110, y=250)

        self.exit_qty_label = Label(master=self.frame, text="Exit Qty:", font=FONT3, bg=BACKGROUND_COLOR, fg="red")
        self.exit_qty_label.place(x=5, y=310)

        self.material_exit_qty = Entry(master=self.frame, )
        self.material_exit_qty.place(x=110, y=310)

        self.material_exit_description= Label(master=self.frame, text="Enter a concise description of the work to be done with this material:", font=FONT4, bg=BACKGROUND_COLOR)
        self.material_exit_description.place(x=5, y=370)

        self.material_description_entry = Entry(master=self.frame, width=60)
        self.material_description_entry.place(x=5, y=390)

        self.exit_search_item_btn = Button(master=self.frame, text="click here to select material from stock", font=FONT4, fg="red", width=35, command=self.stock_search)
        self.exit_search_item_btn.place(x=5, y=450)

        self.exit_cancel_btn = Button(master=self.frame, text="Cancel transaction", font=FONT4, fg="white", bg="red", width=35, command=self.exit_cancel_tran)
        self.exit_cancel_btn.place(x=5, y=490)

        self.validate_exit_btn = Button(master=self.frame, text="Validate Exit", font=FONT2, fg="white", bg="red", width=27, command=self.validate_exit)
        self.validate_exit_btn.place(x=5, y=530)

        self.select_btn = Button(master=self.frame, text="Select item", font=FONT4, command=self.selected)
        self.cancel_btn = Button(master=self.frame, text="Cancel", font=FONT4, command=self.cancel_item_selection)


    def stock_search(self):
        """
        - Clears any entry on the Material EXIT section using the clear() function if there is any.
        - Loops through the stock csv file and automatically inserts all the data related to the material including the current quantity in stock to their corresponding entry widgets
        """
        
        clear(self.material_name_entry, self.material_cat, self.material_unit, self.material_current_qty)

        try:
            pandas.read_csv("./data/Stock_level.csv")
        except FileNotFoundError:
            messagebox.showinfo(
            title="Error",
            message="You do not have any inventory"
            )
        else:
        
            self.exit_find.listboxdis(x_cor=450, y_cor=70)

            self.select_btn.place(x=450, y=400)

            self.cancel_btn.place(x=550, y=400)

            self.exit_search_item_btn.config(state="disabled")



    def selected(self):
        """Automatically inserts the material name, domain, unit and quantity to their respective entries"""

        material, mat_domain, mat_unit, mat_qty = self.exit_find.get_details()

        self.material_name_entry.insert(END, material)
        self.material_cat.insert(END, mat_domain)
        self.material_unit.insert(END, mat_unit)
        self.material_current_qty.insert(END, mat_qty)

        forget(self.exit_find.listbox, self.cancel_btn, self.select_btn)
        self.exit_search_item_btn.config(state="active")


    def cancel_item_selection(self):
        """Uses the forget() function hide the Listbox, Select and Cancel buttons and then reactivates the Search item Button"""
        forget(self.exit_find.listbox, self.cancel_btn, self.select_btn)
        self.exit_search_item_btn.config(state="active")


    def exit_cancel_tran(self):
        """Clears all text in the EXIT entry boxes if the transaction is to be canceled (When the 'Cancel transaction' ic clicked)"""
        clear(self.material_name_entry,  self.material_cat, self.material_unit, self.material_current_qty, self.material_exit_qty, self.material_description_entry)

    def validate_exit(self):

        """
        - Gets all material details and ensures that the name, domain and unit of the outbound material is an exact match to any material in stock for the exit to be accepted
        - Appends the transaction data to the Exit, General ledger and Stock level csv files if all conditions have been fulfilled and the file exits (for the Exit file) otherwise, it creates the file and appends the data
        - For the Stock file, it deletes any data relating to the specific material (material for a specific domain) and inserts a new data with an updated quantity (subtracts exit quantity from quantity in stock)
        - For the General Ledger, it registers the quantity with a minus(-) sign to indicate an exit.
        - Uses the Inventory_check function to update the quantity displayed in the Stock Check section
        """

        item_name, item_cat, unit, qty, exit_qty, description, *_ = get_values( self.material_name_entry, self.material_cat, self.material_unit, self.material_current_qty, self.material_exit_qty, self.material_description_entry)

        current_time = datetime.datetime.now()
        date = current_time.strftime("%d-%b-%Y")
        qty_left = int(qty) - int(exit_qty)
        real_name = item_name[:-5]

        
        try:
            stock_data = pandas.read_csv("./data/Stock_level.csv")
        except FileNotFoundError:
            messagebox.showinfo(
                title="Error",
                message="You do not have any inventory"
                )
        else:
            stk_df = pandas.DataFrame(stock_data)
            chosen_material = stock_data[stock_data.Material == item_name]
            material_dict = chosen_material.to_dict(orient="records")

            if item_cat != material_dict[0]["Domain"] or item_name != material_dict[0]["Material"] or unit != material_dict[0]["Unit"] or int(qty) != material_dict[0]["Quantity"]:
                messagebox.showinfo(
                title="Error",
                message="Do not change any data concerning the material for the transaction to be successfull"
            )
            
            elif  not exit_qty.isdecimal() or int(exit_qty) < 1:
                messagebox.showinfo(
                    title="Invalid quantity",
                    message="Quantities must be numerical and cannot be less than 1"
                )
            
            elif qty_left < 0:
                messagebox.showinfo(
                    title="Error",
                    message="Insufficient stock"
                )

            elif len(description) < 20:
                messagebox.showinfo(
                    title="Error",
                    message="Enter a comprehensive description of the work to be done with this material and do not use symbols"
                )
            else:

                tran_validate = messagebox.askokcancel(
                    title="Confirm Exit",
                    message=f"Material: {real_name}\nDomain: {item_cat}\nUnit: {unit}\nQuantity: {exit_qty}"
                )

                if tran_validate is True:

                    exit_data = {
                        "Date" : [date],
                        "Time" : [f"{current_time.strftime('%H:%M:%S')}"],
                        "Domain": [item_cat],
                        "Material" : [real_name],
                        "Unit" : [unit],
                        "Quantity" : [exit_qty],
                        "Description" : [description]
                    }
                    exit_df = pandas.DataFrame(exit_data)

                    gl_data = {
                        "Date" : [date],
                        "Time" : [f"{current_time.strftime('%H:%M:%S')}"],
                        "Domain": [item_cat],
                        "Material" : [real_name],
                        "Unit" : [unit],
                        "Quantity" : [-int(exit_qty)]                
                    }
                    gl_df = pandas.DataFrame(gl_data)

                    new_stk_data = {
                        "Domain": [item_cat],
                        "Material" : [item_name],
                        "Unit" : [unit],
                        "Quantity" : [qty_left] 
                    }
                    new_stk_df = pandas.DataFrame(new_stk_data)

                    try:
                        pandas.read_csv("./data/Exit.csv")
                    except FileNotFoundError:
                        exit_df.to_csv("./data/Exit.csv", mode='a', index=False)
                    else:
                        exit_df.to_csv("./data/Exit.csv", mode='a', index=False, header=False)

                    finally:
                        gl_df.to_csv("./data/General_ledger.csv", mode='a', index=False, header=False)

                        for (i, row) in stk_df.iterrows():
                            if row.Material == item_name:
                                stk_df = stk_df.drop(stk_df.index[i], axis=0)
                                stk_df.to_csv("./data/Stock_level.csv", index=False)
                                new_stk_df.to_csv("./data/Stock_level.csv", mode='a', index=False, header=False)
                    clear(self.material_name_entry,  self.material_cat, self.material_unit, self.material_current_qty, self.material_exit_qty, self.material_description_entry)
                    self.update.inventory_check()