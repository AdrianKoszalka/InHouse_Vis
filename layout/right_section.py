import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class RightSection(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.update()
        self.grid(row = 0, column = 2, sticky = 'NESW', padx = 20, pady = 20)
        self.background = '#dbdcdd'

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, bg = '#dbdcdd')
        self.canvas.grid(sticky='NESW')

        self.canvas.rowconfigure(0, weight = 1)
        self.canvas.columnconfigure(0, weight = 1)

        self.insert_bg()
        self.create_quit_button()

    def insert_bg(self):
        image = Image.open('layout/images/index_bar_bg.png')
        self.pic = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image = self.pic, anchor='nw')

    def create_quit_button(self):
        self.button_canvas = tk.Canvas(self.canvas, height = 40, width = 130, bd=0, highlightthickness=0, bg = '#313a46', cursor = "hand2")
        self.button_canvas.grid(sticky = "S", pady = (0, 10))

        self.quit_button_pic = Image.open('layout/images/quit_button.png')
        self.button_pic = ImageTk.PhotoImage(self.quit_button_pic)

        self.button = self.button_canvas.create_image(0, 0,  image = self.button_pic, anchor = "nw")

    def create_indexes(self, workers, workers_in, workers_p, workstation, workstation_used, workstation_p):
        self.canvas.create_text(10, 10, text = "Area Load", font = ('Lato', '15', 'normal'), fill = "#6a829a", anchor = 'nw')
        
        self.canvas.create_text(10, 50, text = "WORKERS:", font = ('Lato', '8', 'normal'), fill = "#6a829a", anchor = 'nw')
        self.canvas.create_text(
            10, 65, 
            text = "{}/{} ({}%)".format(workers_in, workers, workers_p), 
            font = ('Lato', '15', 'normal'), 
            fill = "white", 
            anchor = 'nw')

        self.canvas.create_text(10, 100, text = "USED WORKSTATION:", font = ('Lato', '8', 'normal'), fill = "#6a829a", anchor = 'nw')
        self.canvas.create_text(
            10, 115, 
            text = "{}/{} ({}%)".format(workstation_used, workstation, workstation_p), 
            font = ('Lato', '15', 'normal'), 
            fill = "white", 
            anchor = 'nw')


    def program_quit(self):
        pass
