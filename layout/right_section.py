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

        self.load_index_canvas = tk.Canvas(self, bd=0, highlightthickness=0, bg = '#dbdcdd')
        self.load_index_canvas.grid(sticky='NESW')

        self.load_index_canvas.rowconfigure(0, weight = 1)
        self.load_index_canvas.columnconfigure(0, weight = 1)

        self.insert_bg()
        self.create_quit_button()

    def insert_bg(self):
        
        right_section_bg = Image.open('layout/images/index_bar_bg.png')
        
        self.background_image = ImageTk.PhotoImage(right_section_bg)
        self.load_index_canvas.create_image(0, 0, image = self.background_image, anchor='nw')

    def create_quit_button(self): 
        
        self.button_canvas = tk.Canvas(self.load_index_canvas, height = 40, width = 130, bd=0, highlightthickness=0, bg = '#313a46', cursor = "hand2")
        self.button_canvas.grid(sticky = "S", pady = (0, 10))

        self.quit_button_pic = Image.open('layout/images/quit_button.png')
        self.button_pic = ImageTk.PhotoImage(self.quit_button_pic)

        self.button = self.button_canvas.create_image(0, 0,  image = self.button_pic, anchor = "nw")

    def crate_title_textes(self):

        self.load_index_canvas.create_text(
            10, 10, 
            text = "Area Load", 
            font = ('Lato', '15', 'normal'), 
            fill = "#6a829a", 
            anchor = 'nw', 
            tag = "title text")

        self.load_index_canvas.create_text(
            10, 50, 
            text = "WORKERS:", 
            font = ('Lato', '8', 'normal'), 
            fill = "#6a829a", 
            anchor = 'nw', 
            tag = "workers_text")

        self.load_index_canvas.create_text(
            10, 100, 
            text = "USED WORKSTATION:", 
            font = ('Lato', '8', 'normal'), 
            fill = "#6a829a", 
            anchor = 'nw', 
            tag = "workstation_text")

    def create_indexes(self, workers, workers_in, workers_p, workstation, workstation_used, workstation_p):

        self.tags_to_refresh = ["workers_index", "workstation_index"]
        
        self.load_index_canvas.create_text(
            10, 65, 
            text = "{}/{} ({}%)".format(workers_in, workers, workers_p), 
            font = ('Lato', '15', 'normal'), 
            fill = "white", 
            anchor = 'nw',
            tag = "workers_index")

        self.load_index_canvas.create_text(
            10, 115, 
            text = "{}/{} ({}%)".format(workstation_used, workstation, workstation_p), 
            font = ('Lato', '15', 'normal'), 
            fill = "white", 
            anchor = 'nw',
            tag = "workstation_index")