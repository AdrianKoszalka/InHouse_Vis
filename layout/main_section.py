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

    # def insert_image(self):

    #     image = Image.open("Layouts/Layout2.jpg")
    #     image_width = image.size[0]
    #     image_height = image.size[1]

    #     if image_width > self.frame_width or image_height > self.frame_height:
    #         ratio_w = image_width/self.frame_width
    #         ratio_h = image_height/self.frame_height
                
    #         if ratio_w > ratio_h:
    #             image = image.resize((int((image_width/ratio_w)-50), int((image_height/ratio_w)-50)), Image.ANTIALIAS)
    #             self.pic = ImageTk.PhotoImage(image)
    #             self.canvas.create_image((self.half_frame_width, self.half_frame_height), image=self.pic)
    #         else:
    #             image = image.resize((int((image_width/ratio_h)-50), int((image_height/ratio_h)-50)), Image.ANTIALIAS)
    #             self.pic = ImageTk.PhotoImage(image)
    #             self.canvas.create_image((self.half_frame_width, self.half_frame_height), image=self.pic)

    # def load_dots(self, sthelse):
        
    #     image_2 = Image.open("images/red_dot.png")
    #     self.pik_2 = ImageTk.PhotoImage(image_2)

    #     image_3 = Image.open("images/green_dot.png")
    #     self.pik_3 = ImageTk.PhotoImage(image_3)

    #     self.area_in = []

    #     for ids in connect.workers_in:
    #         self.area_in.append(connect.workers_df.loc[ids, 'work_station'])
            
    #     for area_names in self.location_dic.keys():
    #         if area_names in self.area_in:
    #             for positions in self.location_dic[area_names]:

    #                 dot_x = positions[0]
    #                 dot_y = positions[1]

    #                 self.canvas.create_image((dot_x, dot_y), image=self.pik_3)
    #         else:
    #             for positions in self.location_dic[area_names]:

    #                 dot_x = positions[0]
    #                 dot_y = positions[1]

    #                 self.canvas.create_image((dot_x, dot_y), image=self.pik_2)
