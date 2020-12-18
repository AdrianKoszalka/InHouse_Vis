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
        self.update_idletasks()

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

        self.area_layout.rowconfigure(0, weight=1)
        self.area_layout.columnconfigure(0, weight=1)

        self.layout_canvas = tk.Canvas(self.area_layout, bd=0, highlightthickness=0, bg = '#dbdcdd')
        self.layout_canvas.grid(row = 0, column = 0, sticky = 'NESW')

        self.layout_canvas.columnconfigure(0, weight = 1)
        self.layout_canvas.rowconfigure(0, weight = 1)

        # self.insert_layout_bg()

    def insert_layout_bg(self):
        bg_image = Image.open('layout/images/area_layout_bg.png')

        self.pic = ImageTk.PhotoImage(bg_image)
        bg_image = self.layout_canvas.create_image(0, 0, image = self.pic, anchor='nw')

    def display_area_name(self, area_name):
        self.data_tima_canvas.create_text(15,45 , text = area_name, font = ('Lato', '18', 'normal'), fill = '#313a46', anchor = 'nw')

    def load_date_and_time_icon(self):

        calendar_image = Image.open('layout/images/calendar.png')
        self.calendar_pic = ImageTk.PhotoImage(calendar_image)
        self.data_tima_canvas.create_image(1060, 45, image=self.calendar_pic, anchor='nw')

        clock_image = Image.open('layout/images/clock.png')
        self.clock_pic = ImageTk.PhotoImage(clock_image)
        self.data_tima_canvas.create_image(1240,47, image=self.clock_pic, anchor='nw')

    def load_date(self, date_):

        self.data_tima_canvas.create_text(1100, 49 , text = date_.strftime("%d/%m/%Y"), font = ('Lato', '15', 'normal'), fill = '#939393', anchor = 'nw')

    def load_time(self):
        current_time = time.strftime("%H:%M:%S")

        self.dis_time = self.data_tima_canvas.create_text(1280,49 , text = current_time, font = ('Lato', '15', 'normal'), fill = '#939393', anchor = 'nw')

    def update_time(self):
        self.data_tima_canvas.delete(self.dis_time)
        
        self.load_time()

        self.data_tima_canvas.after(1000, self.update_time)

    def insert_image(self, path):

        self.frame_height = 960 
        self.frame_width = 1390
        self.half_frame_width = int(self.frame_width / 2)
        self.half_frame_height = int(self.frame_height / 2) 

        image = Image.open(path)
        image_width = image.size[0]
        image_height = image.size[1]

        self.layout_canvas.update()

        if image_width > self.frame_width or image_height > self.frame_height:
            ratio_w = image_width/self.frame_width
            ratio_h = image_height/self.frame_height
                
            if ratio_w > ratio_h:
                image = image.resize((int((image_width/ratio_w)-50), int((image_height/ratio_w)-50)), Image.ANTIALIAS)
                self.pic = ImageTk.PhotoImage(image)
                
                bg_image = Image.open('layout/images/area_layout_bg.png')
                self.pic_2 = ImageTk.PhotoImage(bg_image)
                
                pic = [self.pic_2, self.pic]

                for img in pic:
                    self.layout_canvas.create_image((self.half_frame_width, self.half_frame_height), image=img)
            else:
                image = image.resize((int((image_width/ratio_h)-50), int((image_height/ratio_h)-50)), Image.ANTIALIAS)
                self.pic = ImageTk.PhotoImage(image)
                
                bg_image = Image.open('layout/images/area_layout_bg.png')
                self.pic_2 = ImageTk.PhotoImage(bg_image)
                
                pic = [self.pic_2, self.pic]

                for img in pic:
                    self.layout_canvas.create_image((self.half_frame_width, self.half_frame_height), image=img)

    def load_dots(self, workstation_dict, sql_data):
        
        image_2 = Image.open("layout/images/red_dot.png")
        self.pik_2 = ImageTk.PhotoImage(image_2)

        image_3 = Image.open("layout/images/green_dot.png")
        self.pik_3 = ImageTk.PhotoImage(image_3)

        self.dots_tags = [] 
            
        for area_names in workstation_dict.keys():
            if area_names in sql_data.area_in:
                for positions in workstation_dict[area_names]:

                    dot_x = positions[0]
                    dot_y = positions[1]

                    self.green_point = self.layout_canvas.create_image((dot_x, dot_y), image=self.pik_3, tag = "{}_dot".format(area_names))
                    self.dots_tags.append("{}_dot".format(area_names))
            else:
                for positions in workstation_dict[area_names]:

                    dot_x = positions[0]
                    dot_y = positions[1]

                    self.red_point = self.layout_canvas.create_image((dot_x, dot_y), image=self.pik_2, tag = "{}_dot".format(area_names))
                    self.dots_tags.append("{}_dot".format(area_names))


    def display_workstation_info(self):
        
        for dots in self.dots_tags:
            self.layout_canvas.tag_bind(dots, '<Enter>', lambda event, dot = dots: self.display(event, dot))

    def display(self, event, dot):
        
        print(dot)

    def create_dots_position_dic(self, workstation_dict):
        
        self.dots_position = {}

        for areas in workstation_dict.keys():
            for position in workstation_dict[areas]:

                self.dots_position[areas] = [position[0] - 10, position[0] + 10, position[1] - 10, position[1] + 10]

        print(self.dots_position)

