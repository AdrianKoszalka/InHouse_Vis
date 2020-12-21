import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import time
import pandas as pd

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

        self.data_time_canvas = tk.Canvas(self.data_time_bar, bd=0, highlightthickness=0, bg = '#dbdcdd')
        self.data_time_canvas.grid(row = 0, column = 0, sticky = 'NESW')

        self.area_layout = tk.Frame(self)
        self.area_layout.grid(row = 1, column = 0, sticky = 'NESW')
        self.area_layout.grid_propagate(0)

        self.area_layout.rowconfigure(0, weight=1)
        self.area_layout.columnconfigure(0, weight=1)

        self.layout_canvas = tk.Canvas(self.area_layout, bd=0, highlightthickness=0, bg = '#dbdcdd')
        self.layout_canvas.grid(row = 0, column = 0, sticky = 'NESW')

        self.layout_canvas.columnconfigure(0, weight = 1)
        self.layout_canvas.rowconfigure(0, weight = 1)

    def insert_layout_bg(self):
        bg_image = Image.open('layout/images/area_layout_bg.png')

        self.background_image = ImageTk.PhotoImage(bg_image)
        bg_image = self.layout_canvas.create_image(0, 0, image = self.background_image, anchor='nw')

    def display_area_name(self, area_name):
        self.data_time_canvas.create_text(15,45 , text = area_name, font = ('Lato', '18', 'normal'), fill = '#313a46', anchor = 'nw')

    def load_date_and_time_icon(self):

        calendar_image = Image.open('layout/images/calendar.png')
        self.calendar_pic = ImageTk.PhotoImage(calendar_image)
        self.data_time_canvas.create_image(1060, 45, image=self.calendar_pic, anchor='nw')

        clock_image = Image.open('layout/images/clock.png')
        self.clock_pic = ImageTk.PhotoImage(clock_image)
        self.data_time_canvas.create_image(1240,47, image=self.clock_pic, anchor='nw')

    def load_date(self, date_):

        self.data_time_canvas.create_text(1100, 49 , text = date_.strftime("%d/%m/%Y"), font = ('Lato', '15', 'normal'), fill = '#939393', anchor = 'nw')

    def load_time(self):
        self.current_time = time.strftime('%H:%M:%S')

        self.dis_time = self.data_time_canvas.create_text(1280,49 , text = self.current_time, font = ('Lato', '15', 'normal'), fill = '#939393', anchor = 'nw')

    def update_time(self):
        self.data_time_canvas.delete(self.dis_time)
        
        self.load_time()

        self.data_time_canvas.after(1000, self.update_time)

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
                self.area_layout_image = ImageTk.PhotoImage(image)
                
                bg_image = Image.open('layout/images/area_layout_bg.png')
                self.background_image = ImageTk.PhotoImage(bg_image)
                
                pic = [self.background_image, self.area_layout_image]

                for img in pic:
                    self.layout_canvas.create_image((self.half_frame_width, self.half_frame_height), image=img)
            else:
                image = image.resize((int((image_width/ratio_h)-50), int((image_height/ratio_h)-50)), Image.ANTIALIAS)
                self.area_layout_image = ImageTk.PhotoImage(image)
                
                bg_image = Image.open('layout/images/area_layout_bg.png')
                self.background_image = ImageTk.PhotoImage(bg_image)
                
                pic = [self.background_image, self.area_layout_image]

                for img in pic:
                    self.layout_canvas.create_image((self.half_frame_width, self.half_frame_height), image=img)

    def load_dots(self, workstation_dict, sql_data):
        
        image_2 = Image.open("layout/images/red_dot.png")
        self.red_dot_image = ImageTk.PhotoImage(image_2)

        image_3 = Image.open("layout/images/green_dot.png")
        self.green_dot_image = ImageTk.PhotoImage(image_3)

        self.dots_tags = [] 
            
        for area_names in workstation_dict.keys():
            if area_names in sql_data.area_in:
                for positions in workstation_dict[area_names]:

                    dot_x = positions[0]
                    dot_y = positions[1]

                    green_point = self.layout_canvas.create_image((dot_x, dot_y), image=self.green_dot_image, tag = "{}".format(area_names))
                    self.dots_tags.append("{}".format(area_names))
            else:
                for positions in workstation_dict[area_names]:

                    dot_x = positions[0]
                    dot_y = positions[1]

                    red_point = self.layout_canvas.create_image((dot_x, dot_y), image=self.red_dot_image, tag = "{}".format(area_names))
                    self.dots_tags.append("{}".format(area_names))


    def mouse_enter_dots(self, workstation_dict, sql_data):
        
        for dots in self.dots_tags:
            self.layout_canvas.tag_bind(dots, '<Enter>', lambda event, dot = dots, workstation_dict = workstation_dict, sql_data=sql_data: self.display_workstation_info(event, dot, workstation_dict, sql_data))
            self.layout_canvas.tag_bind(dots, '<Leave>', lambda event: self.clear_layout_area(event))

    def display_workstation_info(self, event, dot, workstation_dict, sql_data):
        
        dots_position = workstation_dict[dot]

        workers_name = sql_data.workers_df[sql_data.workers_df['work_station'] == dot]['name'].values
        workers_second_name = sql_data.workers_df[sql_data.workers_df['work_station'] == dot]['sec_name'].values

        self.layout_canvas.config(cursor = "hand2")
        
        try:
            worker_full_name = str(workers_name[0] + " " + workers_second_name[0])
        except:
            worker_full_name = None

        try:
            workers_id = sql_data.workers_df[sql_data.workers_df['work_station'] == dot].index.values
        except:
            workers_id = None

        workstation_label_bg = Image.open('layout/images/workstation_label.png')
        self.workstation_label = ImageTk.PhotoImage(workstation_label_bg)

        self.layout_canvas.create_image(dots_position[0][0] - 60, dots_position[0][1] - 60, image = self.workstation_label, anchor = 'nw', tag = "w_label_bg")
        self.layout_canvas.create_text(dots_position[0][0] - 55, dots_position[0][1] - 55, text = dot, anchor = 'nw', font = ('Lato', '7', 'bold'), fill = "#313a46", tag = "w_workstation_name")

        try:
            if workers_id[0] in sql_data.workers_in:
                self.layout_canvas.create_text(dots_position[0][0] - 55, dots_position[0][1] - 42, text = worker_full_name, anchor = 'nw', font = ('Lato', '9', 'bold'), fill = "#67cd35", tag = "w_worker_name")
            else:
                self.layout_canvas.create_text(dots_position[0][0] - 55, dots_position[0][1] - 42, text = worker_full_name, anchor = 'nw', font = ('Lato', '9', 'bold'), fill = "#cd3535", tag = "w_worker_name")
        except:
            self.layout_canvas.create_text(dots_position[0][0] - 55, dots_position[0][1] - 42, text = "Empty Workstation", anchor = 'nw', font = ('Lato', '9', 'bold'), fill = "#313a46", tag = "w_worker_name")

    def clear_layout_area(self, event):

        self.layout_canvas.delete("w_label_bg", "w_workstation_name", "w_worker_name")
        self.layout_canvas.config(cursor = "arrow")
