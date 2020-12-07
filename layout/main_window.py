import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attributes('-fullscreen', True)
        self.configure(bg = '#dbdcdd')
        self.update()

        self.grid_propagate(0)
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, minsize = 340)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, minsize = 190)

    def quit_program(self):
        self.destroy()