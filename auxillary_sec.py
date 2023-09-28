from functions import clear
import pandas
from tkinter import *
from tkinter import messagebox
import os


selected = "" 
BACKGROUND_COLOR = "#D3D3D3"

report_type = [("Entry Records", 1), ("Exit Records", 2), ("Ledger Records", 3), ("Current Stock Level", 4)]

class StockCheck():
    """This class is responsible for displaying the Stock Check sections and verifying the current quantity for each material"""

    def __init__(self, frame:Frame):
        self.frame = frame
        self.inventory_check()

        self.check_label = Label(master=self.frame, text="Stock Check", font=("Century Gothic", 12, "bold"), bg=BACKGROUND_COLOR)
        self.check_label.place(x=10, y=50)

        self.check_domain = Label(master=self.frame, text="Domain:", font=("Century Gothic", 10, "bold"), bg=BACKGROUND_COLOR)
        self.check_domain.place(x=15, y=80)

        self.check_domain_entry = Entry(master=self.frame, width=22)
        self.check_domain_entry.place(x=100, y=80)

        self.check_qty = Label(master=self.frame, text="Quantity in stock:", font=("Century Gothic", 10, "bold"), bg=BACKGROUND_COLOR)
        self.check_qty.place(x=15, y=120)

        self.check_qty_entry = Entry(master=self.frame, width=10)
        self.check_qty_entry.place(x=150, y=120)


    def inventory_check(self):
        """
        - Deletes any old Listbox(if any) and recreates another(to ensure that inventory data is updated)
        - Also responsible for displaying the SELECT and CLEAR button
        """

        self.listbox3 = Listbox(master=self.frame, height=10, width=30)
        self.listbox3.place(x=450, y=20)

        try:
            self.stock_data = pandas.read_csv("./data/Stock_level.csv")    
        except FileNotFoundError:
            print("Nofile")
        else:
            material_list = self.stock_data.Material.to_list()

            self.listbox3.delete(0, END)

            for item in material_list:
                self.listbox3.insert(material_list.index(item), item)

            self.select_btn3 = Button(master=self.frame, text="Select", font=("Century Gothic", 8, "bold"), command=self.check)
            self.select_btn3.place(x=400, y=50)

            self.select_btn4 = Button(master=self.frame, text="Clear", font=("Century Gothic", 8, "bold"), command=self.wipe)
            self.select_btn4.place(x=400, y=100)



    def wipe(self):
        """Clears the domain and quantity entry"""
        clear(self.check_domain_entry, self.check_qty_entry)



    def check(self):
        """
        - Loops through the stock data to update the quantity and inserts the domain and quantity of the selected material in their entries so that the current stock quantity can be known
        """

        global selected

        clear(self.check_domain_entry, self.check_qty_entry)

        for _ in self.listbox3.curselection():
            selected = (self.listbox3.get(self.listbox3.curselection()))

        for (index, row) in self.stock_data.iterrows():

            if row.Material == selected:

                self.check_domain_entry.insert(END, row.Domain)
                self.check_qty_entry.insert(END, row.Quantity)




class Report():

    """
    - This class generates any REPORT chosen 
    """

    def __init__(self, frame:Frame):

        self.radio_state = IntVar()

        self.rb_list = []

        x_cor = 10
        y_cor = 50

        for i in range(len(report_type)):
            gen_radiobutton = Radiobutton(master=frame, text=report_type[i][0], value=report_type[i][1], variable=self.radio_state, font=("Century Gothic", 10, "bold"), bg=BACKGROUND_COLOR)
            gen_radiobutton.place(x=x_cor, y=y_cor)
            x_cor += 150

            self.rb_list.append(gen_radiobutton)

        self.gen_excel_btn = Button(master=frame, text="EXPORT RECORDS TO MICROSOFT EXCEL",  font=("Century Gothic", 10, "bold"), command=self.generate_excel)
        self.gen_excel_btn.place(x=225, y=120)




    def generate_excel(self):
        """
        - Based on the record type chosen, this function will automatically create an xlsx file and open the file in MICROSOFT EXCEL
        """
        record_type = ["Entries", "Exit", "General_ledger", "Stock_level"]

        radio_get = self.radio_state.get() - 1

        if radio_get < 0 :
            messagebox.showinfo(
                title="Error",
                message="No record has been selected",
            )
        else:
            try:
                data = pandas.read_csv(f"./data/{record_type[radio_get]}.csv")
            except FileNotFoundError:
                messagebox.showinfo(
                    title="Error",
                    message="Record does not exit"
                )
            else:
                data.to_excel(f"./reports/{record_type[radio_get]}.xlsx", index=False)
                os.system(f'start "excel" "./reports/{record_type[radio_get]}.xlsx"')
                
            self.radio_state.set(-1)

