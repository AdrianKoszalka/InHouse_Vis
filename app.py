import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awareness
from layout.left_section import LeftSection
from layout.main_section import MainSection
from layout.right_section import RightSection

set_dpi_awareness()

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attributes('-fullscreen', True)
        self.configure(bg = '#f9fafd')
        self.update()

        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0,1,2), weight = 1)

        left_section = LeftSection(self)
        left_section.grid(row = 0, column = 0, sticky = 'NESW')

        main_section = MainSection(self)
        main_section.grid(row = 0, column = 1, sticky = 'NESW')

        right_section = RightSection(self)
        right_section.grid(row = 0, column = 2, sticky = 'NESW')

app = MainWindow()
app.mainloop()