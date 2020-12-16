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

    def create_workers_list(self, connect): 
        
        self.full_name_in = []
        self.full_name_out = []

        for ids in connect.workers_in:
            self.full_name_in.append(connect.workers_df.loc[ids, 'sec_name'] + " " + connect.workers_df.loc[ids, 'name'] )

        self.sorted_full_name_in = sorted(self.full_name_in)

        for ids in connect.workers_out:
            self.full_name_out.append(connect.workers_df.loc[ids, 'sec_name'] + " " + connect.workers_df.loc[ids, 'name'] )

        self.sorted_full_name_out = sorted(self.full_name_out)

        self.canvas.create_text(
            25, 95, 
            text = "WORKERS IN:",
            font = ('Lato', '12', 'normal'), 
            fill = "#6a829a", 
            anchor = 'nw'
        )

        self.y_position = 120

        for names in self.sorted_full_name_in:
            self.canvas.create_text(
                30, self.y_position, 
                text = names,
                font = ('Lato', '10', 'normal'),
                fill = "#9fcabe",
                anchor = 'nw'
            )
            self.y_position += 20

        self.y_position += 10
        self.canvas.create_text(
            25, self.y_position, 
            text = "WORKERS OUT:",
            font = ('Lato', '12', 'normal'), 
            fill = "#6a829a", 
            anchor = 'nw'
        )
        self.y_position += 25

        for names in self.sorted_full_name_out:
            self.canvas.create_text(
                30, self.y_position, 
                text = names,
                font = ('Lato', '10', 'normal'),
                fill = "#cb9aa4",
                anchor = 'nw'
            )
            self.y_position += 20