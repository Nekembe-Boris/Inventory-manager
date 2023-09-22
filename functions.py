from tkinter import *
from tkinter import messagebox
import pandas

selected = ""

def clear(*args):
    """Clears the text in any entry widget that is passed as an argument"""
    for n in args:
        n.delete(0, END)

def forget(*args):
    """automatically hides any widget"""
    for n in args:
        n.place_forget()

def get_values(*args):
    """gets the values from any entry widget, stores it in a list and returns a tuple containing all the results that can easily be unpacked"""
    result = []
    for n in args:
        result.append(n.get())
    return tuple(result)


class Search():
    """
    - Clears any ENTRY section using the clear() function if any is present.
    - Loops through the stock csv file and automatically inserts all the data related to the material including the current quantity in stock to their corresponding entry widgets
    """

    def __init__(self, frame:Frame):
        self.frame = frame


    def listboxdis(self, x_cor, y_cor):
        """This function is responsible for displaying a Listbox that contains the materials in stock"""
        try:
            stock_data = pandas.read_csv("./data/Stock_level.csv")
        except FileNotFoundError:
            messagebox.showinfo(
                title="Error",
                message="You do not have any inventory"
                )
        else:

            self.material_list = stock_data.Material.to_list()

            self.listbox = Listbox(master=self.frame, height=20, width=30)
            self.listbox.place(x=x_cor, y=y_cor)
                

            for item in self.material_list:
                self.listbox.insert(self.material_list.index(item), item)



    def get_details(self):
        """Gets the name, domain, Unit and Quantity of the selected material and returns them."""

        stock_data = pandas.read_csv("./data/Stock_level.csv")
        
        global selected
        selected = ""

        for i in self.listbox.curselection():
            selected = (self.listbox.get(i))

        for (index, row) in stock_data.iterrows():

            if row.Material == selected:
                return row.Material, row.Domain, row.Unit, row.Quantity
   