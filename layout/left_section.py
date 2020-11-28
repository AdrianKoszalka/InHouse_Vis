import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class LeftSection(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        self.update()
        self.grid(row = 0, column = 0, sticky = 'NESW', padx = 20, pady = 20)
        self.background = '#dbdcdd'

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, bg = '#dbdcdd')
        self.canvas.grid(sticky='NESW')

        self.insert_bg()

    def insert_bg(self):
        image = Image.open('layout/images/workers_list_bg.png')
        self.pic = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image = self.pic, anchor='nw')