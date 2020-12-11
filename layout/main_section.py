import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import time

class MainSection(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        self.grid(row = 0, column = 1, sticky = 'NESW')
        self.background = '#dbdcdd'
        self.update()

        self.rowconfigure(0, minsize = 100)
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(0, weight = 1)  

        self.data_time_bar = ttk.Frame(self)
        self.data_time_bar.grid(row = 0, column = 0, sticky = 'NESW')
        self.data_time_bar.update()
        self.data_time_bar.grid_propagate(0)

        self.data_time_bar.rowconfigure(0, weight = 1)
        self.data_time_bar.columnconfigure(0, weight = 1)

        self.data_tima_canvas = tk.Canvas(self.data_time_bar, bd=0, highlightthickness=0, bg = '#dbdcdd')
        self.data_tima_canvas.grid(row = 0, column = 0, sticky = 'NESW')

        self.load_time()
        self.data_tima_canvas.after(1000, self.update_time)

        self.area_layout = tk.Frame(self)
        self.area_layout.grid(row = 1, column = 0, sticky = 'NESW')
        self.area_layout.grid_propagate(0)
        self.area_layout.update_idletasks()

        self.area_layout.rowconfigure(0, weight=1)
        self.area_layout.columnconfigure(0, weight=1)

        self.layout_canvas = tk.Canvas(self.area_layout, bd=0, highlightthickness=0, bg = '#dbdcdd')
        self.layout_canvas.grid(row = 0, column = 0, sticky = 'NESW')

        self.insert_layout_bg()

    def insert_layout_bg(self):
        image = Image.open('layout/images/area_layout_bg.png')
        self.pic = ImageTk.PhotoImage(image)
        self.layout_canvas.create_image(0, 0, image = self.pic, anchor='nw')

    def display_area_name(self, area_name):
        self.data_tima_canvas.create_text(15,45 , text = area_name, font = ('Lato', '18', 'normal'), fill = '#313a46', anchor = 'nw')

    def load_date_and_time_icon(self):

        calendar_image = Image.open('layout/images/calendar.png')
        self.pic_1 = ImageTk.PhotoImage(calendar_image)
        self.data_tima_canvas.create_image(1060, 45, image=self.pic_1, anchor='nw')

        clock_image = Image.open('layout/images/clock.png')
        self.pic_2 = ImageTk.PhotoImage(clock_image)
        self.data_tima_canvas.create_image(1240,47, image=self.pic_2, anchor='nw')

    def load_date(self, date_):

        self.data_tima_canvas.create_text(1100, 49 , text = date_.strftime("%d/%m/%Y"), font = ('Lato', '15', 'normal'), fill = '#939393', anchor = 'nw')

    def load_time(self):
        current_time = time.strftime("%H:%M:%S")

        self.dis_time = self.data_tima_canvas.create_text(1280,49 , text = current_time, font = ('Lato', '15', 'normal'), fill = '#939393', anchor = 'nw')

    def update_time(self):
        self.data_tima_canvas.delete(self.dis_time)
        
        self.load_time()

        self.data_tima_canvas.after(1000, self.update_time)
