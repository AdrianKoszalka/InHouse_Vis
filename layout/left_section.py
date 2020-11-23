import tkinter as tk
from tkinter import ttk

class LeftSection(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        label = tk.Label(self, bg = '#313a46')
        label.grid(row = 0, column = 0, sticky="NESW")