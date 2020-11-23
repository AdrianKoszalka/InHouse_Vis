import tkinter as tk
from tkinter import ttk

class RightSection(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        label = tk.Label(self, background = '#313a46')
        label.grid(sticky="NESW")