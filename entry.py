from tkinter import *
from tkinter import messagebox
import datetime
from functions import clear, forget, get_values, Search
import pandas
from auxillary_sec import StockCheck

BACKGROUND_COLOR = "#949494"

domain = ["Masonry", "Plumbing", "Electrical", "Tiling", "Ceiling", "Painting", "Equipments", "Water Proofing", "Others", "Scaffolding"]

class EntryTab():

    def __init__(self, frame:Frame, search:Search, update:StockCheck):
        
        self.find = search
        self.frame = frame
        self.update = update

        self.entry_label = Label(master=self.frame, text="ENTRY", font=("Century Gothic", 20, "bold"), bg=BACKGROUND_COLOR)
        self.entry_label.place(x=300, y=0)

        self.domain_label = Label(master=self.frame, text="Domain", font=("Century Gothic", 18, "bold"), bg=BACKGROUND_COLOR)
        self.domain_label.place(x=5, y=70)

        
        self.item_label= Label(master=self.frame, text="Material", font=("Century Gothic", 12, "bold"), bg=BACKGROUND_COLOR)
        self.item_label.place(x=138, y=175)

        self.item_entry = Entry(master=self.frame, width=40)
        self.item_entry.place(x=138, y=200)

        self.units_label = Label(master=self.frame, text="Unit", font=("Century Gothic", 12, "bold"), bg=BACKGROUND_COLOR)
        self.units_label.place(x=135, y=235)

        self.units_entry = Entry(master=self.frame, width=12)
        self.units_entry.place(x=135, y=260)

        self.qty_label = Label(master=self.frame, text="Qty", font=("Century Gothic", 12, "bold"), bg=BACKGROUND_COLOR)
        self.qty_label.place(x=135, y=290)

        self.qty_entry = Entry(master=self.frame, width=10)
        self.qty_entry.place(x=135, y=315)

        self.search_item_btn= Button(master=self.frame, text="click here to select material if already in stock", font=("Century Gothic", 8, "bold"), width=35, command=self.stock_search, fg="green")
        self.search_item_btn.place(x=380, y=450)

        self.entry_cancel_btn = Button(master=self.frame, text="Cancel transaction",  font=("Century Gothic", 8, "bold"), width=35, command=self.entry_cancel_tran, fg="white", bg="green")
        self.entry_cancel_btn.place(x=380, y=490)

        self.validate_entry_btn= Button(master=self.frame, text="Validate Entry", font=("Century Gothic", 12, "bold"), width=27, command=self.validate_entry, fg="white", bg="green")
        self.validate_entry_btn.place(x=380, y=530)

        self.select_btn = Button(master=self.frame, text="Select item", font=("Century Gothic", 8, "bold"), command=self.selected)
        self.cancel_btn = Button(master=self.frame, text="Cancel", font=("Century Gothic", 8, "bold"), command=self.cancel_item_selection)


        self.radio_state = IntVar(master=self.frame)
        self.radiobutton1 = Radiobutton(master=self.frame, text="Ceiling", value=1, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton2 = Radiobutton(master=self.frame, text="Equipments", value=2, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton3 = Radiobutton(master=self.frame, text="Electricity", value=3, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton4 = Radiobutton(master=self.frame, text="Masonry", value=4, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton5 = Radiobutton(master=self.frame, text="Plumbing", value=5, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton6 = Radiobutton(master=self.frame, text="Painting", value=6, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton7 = Radiobutton(master=self.frame, text="Scaffolding", value=7, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton8 = Radiobutton(master=self.frame, text="Tiling", value=8, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton9 = Radiobutton(master=self.frame, text="Waterproofing", value=9, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton10 = Radiobutton(master=self.frame, text="Others", value=10, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.radiobutton1.place(x=15, y=110)
        self.radiobutton2.place(x=15, y=150)
        self.radiobutton3.place(x=15, y=190)
        self.radiobutton4.place(x=15, y=230)
        self.radiobutton5.place(x=15, y=270)
        self.radiobutton6.place(x=15, y=310)
        self.radiobutton7.place(x=15, y=350)
        self.radiobutton8.place(x=15, y=390)
        self.radiobutton9.place(x=15, y=430)
        self.radiobutton10.place(x=15, y=470)



    
    def stock_search(self):
        """
        - Clears any entry on the Material ENTRY section using the clear() function if there is any.
        - Disables the Search item button and displayes the Entry section listbox alongside the Select and Cancel Button
        - 
        """

        clear(self.item_entry, self.units_entry, self.qty_entry)

        try:
            stock_data = pandas.read_csv("./data/Stock_level.csv")
        except FileNotFoundError:
            messagebox.showinfo(
            title="Error",
            message="You do not have any inventory"
            )
        else:
            self.radio_state.set(None)
            
            self.find.listboxdis(x_cor=450, y_cor=70)

            self.select_btn.place(x=450, y=400)

            self.cancel_btn.place(x=550, y=400)

            self.search_item_btn.config(state="disabled")



    def entry_cancel_tran(self):
        """Clears all text in the ENTRY entry boxes if the transaction is to be canceled (When the 'Cancel transaction' is clicked)"""
        clear(self.item_entry, self.units_entry, self.qty_entry)
        self.radio_state.set(None)


    def selected(self):
        """Automatically inserts the material name, domain and unit to their respective entries"""

        material, mat_domain, mat_unit, mat_qty = self.find.get_details()

        self.item_entry.insert(END, material[:-5])
        self.units_entry.insert(END, mat_unit)

        self.search_item_btn.config(state="active")

        for i in range(len(domain)):
            if domain[i] == mat_domain:
                self.radio_state.set(i+1)

        forget(self.find.listbox, self.cancel_btn, self.select_btn)



    def cancel_item_selection(self):
        """Uses the forget() function to hide the listbox, listbox select button and listbox cancel button when the cancel button is clicked"""
        forget(self.find.listbox, self.cancel_btn, self.select_btn)
        self.search_item_btn.config(state="active")


    def validate_entry(self):
        """
        - Gets all material details and the date, checks for conditions like if a domain was chosen, ensure a descriptive material name, ensures that only integers are entered as quantity
        - Appends the transaction data to the Entries, General ledger and Stock level csv files if all conditions have been fulfilled and the file exits otherwise, it creates the files and appends the data
        - If the material is already in stock and the material to be stored has the same domain as the material in stock, it deletes the previous material data and inserts a new data with an updated quantity 
        (adds current quantity to new quantity)
        - Uses the Inventory_check function to update the quantity displayed in the Stock Check section
        """

        current_time = datetime.datetime.now()
        date = current_time.strftime("%d-%b-%Y")

        qty, item_cat = get_values(self.qty_entry, self.radio_state)
        category = domain[item_cat - 1]
        item_name = self.item_entry.get().title()
        stock_name = f"{item_name}[{category[0:3]}]"
        unit = self.units_entry.get().lower()

        
        if item_cat < 1:
            messagebox.showinfo(
                title="Domain error",
                message="No domain was selected for this material"
            )
        elif len(item_name) < 10:
            messagebox.showinfo(
                title="Modify Item name",
                message="Please enter a descriptive and simple item name that will distinguish it from similar materials and make it easy to remember"
            )
        elif len(unit) < 1 or not unit.isalpha():
            messagebox.showinfo(
                title="Modify Unit box",
                message="Please enter a more descriptive Units to distinguish it from similar materials\nOnly use alphabetic characters"
            )
        elif not qty.isdecimal() or int(qty) < 1 :
            messagebox.showinfo(
                title="Invalid quantity",
                message="Quantities must be numerical and cannot be less than 1"
            )
        else:

            tran_validate = messagebox.askokcancel(
                title="Confirm Entry",
                message=f"Material: {item_name}\nDomain: {category}\nUnit: {unit}\nQuantity: {qty}"
                )

            if tran_validate == True:
            
                new_data = {
                    "Date" : [date],
                    "Time" : [f"{current_time.strftime('%H:%M:%S')}"],
                    "Domain": [category],
                    "Material" : [item_name],
                    "Unit" : [unit],
                    "Quantity" : [qty]
                }
                df = pandas.DataFrame(new_data)

                stk_data = {
                    "Domain": [category],
                    "Material" : [f"{item_name}[{category[0:3]}]"],
                    "Unit" : [unit],
                    "Quantity" : [qty]
                }
                new_stk_df = pandas.DataFrame(stk_data)

                try:
                    entry_data = pandas.read_csv("./data/Entries.csv")
                    general_led_data = pandas.read_csv("./data/General_ledger.csv")
                    stock_data = pandas.read_csv("./data/Stock_level.csv")
                except FileNotFoundError:
                    df.to_csv("./data/Entries.csv", mode='a', index=False)
                    df.to_csv("./data/General_ledger.csv", mode='a', index=False)
                    new_stk_df.to_csv("./data/Stock_level.csv", mode='a', index=False)
                else:
                    stk_df = pandas.DataFrame(stock_data)
                    df.to_csv("./data/Entries.csv", mode='a', index=False, header=False)
                    df.to_csv("./data/General_ledger.csv", mode='a', index=False, header=False)

                    stock_lenght = len(stock_data.Material.to_list())

                    for (i, row) in stk_df.iterrows():

                        if row.Material == stock_name and row.Domain == category:

                            stk_df = stk_df.drop(stk_df.index[i], axis=0)
                            stk_df.to_csv("./data/Stock_level.csv", index=False)

                            updated_data = {
                                "Domain": [category],
                                "Material" : [stock_name],
                                "Unit" : [unit],
                                "Quantity" : [int(qty) + row.Quantity]
                            }
                            updated_stk_df = pandas.DataFrame(updated_data)
                            updated_stk_df.to_csv("./data/Stock_level.csv", mode='a', index=False, header=False)
                            stock_lenght -= 1

                    #This line of code checks to see if a new record was created to avoid duplicating entries
                    if stock_lenght == len(stock_data.Material.to_list()):
                        new_stk_df.to_csv("./data/Stock_level.csv", mode='a', index=False, header=False)

                clear(self.item_entry, self.units_entry, self.qty_entry)
                self.radio_state.set(None)
                self.update.inventory_check()
