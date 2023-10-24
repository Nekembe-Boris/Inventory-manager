from tkinter import Tk, Label, Frame, Button
import datetime
from entry import EntryTab
from exit import ExitTab
from functions import Search
from auxillary_sec import StockCheck, Report
from language import french, english


BACKGROUND_COLOR = "#D3D3D3"
FONT1 = ("Century Gothic", 10, "bold")
FONT2 = ("Century Gothic", 8, "bold")
current_date = datetime.datetime.now()

class App():
    def __init__(self):

        self.root = Tk()
        self.root.title("Inventory Manager")
        self.root.geometry("1280x820")
        self.root.config(bg=BACKGROUND_COLOR, pady=2)

        self.date_label = Label(master=self.root, text="Date: ", font=FONT1, bg=BACKGROUND_COLOR)
        self.date_label.place(x=1100, y=0)
        self.date_label2 = Label(master=self.root, text=f"{current_date.strftime('%d   -   %b   -   %Y')}", font=FONT1, bg=BACKGROUND_COLOR)
        self.date_label2.place(x=1150, y=0)

        #Creating a Stock Frame and a stock object first because the INVENTORY_CHECK() function is used as an input by both entry and exit objects
        self.stock_frame = Frame(master=self.root, height=200, width=640, bg=BACKGROUND_COLOR)
        self.stock_frame.grid(column=0, row=1)
        self.stk_check = StockCheck(frame=self.stock_frame)

        #Entry frame and object
        self.entry_frame = Frame(master=self.root, height=580, width=640, bg="#949494")
        self.entry_frame.grid(column=0, row=0, pady=(30, 0))
        self.entry_funcs = Search(self.entry_frame)
        self.entry = EntryTab(frame=self.entry_frame, search=self.entry_funcs, update=self.stk_check)

        #Exit frame and Object
        self.exit_frame = Frame(master=self.root, height=580, width=640, bg="#949494")
        self.exit_frame.grid(column=1, row=0, pady=(30, 0))
        self.exit_funcs = Search(self.exit_frame)
        self.exit_sec = ExitTab(frame=self.exit_frame, search=self.exit_funcs, update=self.stk_check)

        #Report frame and object
        self.report_frame = Frame(master=self.root, height=200, width=640, bg=BACKGROUND_COLOR)
        self.report_frame.grid(column=1, row=1)
        self.report = Report(self.report_frame)

        self.translate_french_btn = Button(master=self.root, text="FR", font=FONT2, command=self.trans_to_fr)
        self.translate_french_btn.place(x=5, y=0)

        self.translate_en_btn = Button(master=self.root, text="EN", font=FONT2, command=self.trans_to_en)
        self.translate_en_btn.place(x=35, y=0)

        ##This makes the widgets responsive as the screensize increases
        n_columns = 2
        n_rows = 2
        for i in range(n_columns):
            self.root.grid_columnconfigure(i,  weight = 1)

        for i in range(n_rows):
            self.root.grid_columnconfigure(i,  weight = 2)

        self.root.mainloop()

    def trans_to_fr(self):
        french(entry=self.entry, exit_sec=self.exit_sec, stock=self.stk_check, report=self.report)

    def trans_to_en(self):
        english(entry=self.entry, exit_sec=self.exit_sec, stock=self.stk_check, report=self.report)


App()
