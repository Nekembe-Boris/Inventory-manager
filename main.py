from tkinter import *
import datetime
from entry import EntryTab
from exit import ExitTab
from functions import Search
from auxillary_sec import StockCheck, Report
from language import french , english


BACKGROUND_COLOR = "#D3D3D3"
current_date = datetime.datetime.now()

#Creating the root window[Note that it was given the minimum screen dimension of a laptop or desktop]
root = Tk()
root.title("Inventory Manager")
root.geometry("1280x820")
root.config(bg=BACKGROUND_COLOR, pady=2)

#The date widget
date_label = Label(master=root, text="Date: ", font=("Century Gothic", 10, "bold"), bg=BACKGROUND_COLOR)
date_label.place(x=1100, y=0)
date_label2 = Label(master=root, text=f"{current_date.strftime('%d   -   %b   -   %Y')}", font=("Century Gothic", 10, "bold"), bg=BACKGROUND_COLOR)
date_label2.place(x=1150, y=0)

##Creating a Stock Frame and a stock object first because the INVENTORY_CHECK() function is used as an input by both entry and exit objects
stock_frame = Frame(master=root, height=200, width=640, bg=BACKGROUND_COLOR)
stock_frame.grid(column=0, row=1)
stock = StockCheck(stock_frame)

#Entry frame and object
entry_frame = Frame(master=root, height=580, width=640, bg="#949494")
entry_frame.grid(column=0, row=0, pady=(30, 0))
entry_funcs = Search(entry_frame)
entry = EntryTab(frame=entry_frame, search=entry_funcs, update=stock)

#Exit frame and Object
exit_frame = Frame(master=root, height=580, width=640, bg="#949494")
exit_frame.grid(column=1, row=0, pady=(30, 0))
exit_funcs = Search(exit_frame)
exit_sec = ExitTab(frame=exit_frame, search=exit_funcs, update=stock)

#Report frame and object
report_frame = Frame(master=root, height=200, width=640, bg=BACKGROUND_COLOR)
report_frame.grid(column=1, row=1)
report = Report(report_frame)

##This widgets responsive as the screensize increases
n_columns = 2
n_rows = 2
for i in range(n_columns):
    root.grid_columnconfigure(i,  weight = 1)

for i in range(n_rows):
    root.grid_columnconfigure(i,  weight = 2)


#This section takes care of the translation functionality of the program
def trans_to_fr():
    french(entry=entry, exit_sec=exit_sec, stock=stock, report=report)

def trans_to_en():
    english(entry=entry, exit_sec=exit_sec, stock=stock, report=report)

translate_french_btn = Button(master=root, text="FR", font=("Century Gothic", 8, "bold"), command=trans_to_fr)
translate_french_btn.place(x=5, y=0)

translate_en_btn = Button(master=root, text="EN", font=("Century Gothic", 8, "bold"), command=trans_to_en)
translate_en_btn.place(x=35, y=0)


root.mainloop()
