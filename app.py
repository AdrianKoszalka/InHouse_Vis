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

        # self.font = ('Lato', '20', 'bold')

        self.attributes('-fullscreen', True)
        self.configure(bg = '#dbdcdd')
        self.update()

        self.grid_propagate(0)
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, minsize = 340)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, minsize = 190)

        left_section = LeftSection(self)
        left_section.grid_propagate(0)

        main_section = MainSection(self)
        main_section.grid_propagate(0)

        right_section = RightSection(self)
        right_section.grid_propagate(0)

app = MainWindow()
app.mainloop()