import time
import datetime

from windows import set_dpi_awareness
from layout.left_section import LeftSection
from layout.main_section import MainSection
from layout.right_section import RightSection
from layout.main_window import MainWindow
from sql_conector import SQLConnector
from objects.objects import objects


class Application():
    def __init__(self, *args, **kwargs):
        
        set_dpi_awareness()
        
        self.choosed_area = objects[0]
        self.current_date_and_time = datetime.datetime.now()
        self.current_time = time.strftime('%H:%M:%S')

        self.main_window = MainWindow()

        self.connector = SQLConnector()
        self.connector.import_workers()
        self.connector.import_log_records(self, self.current_time)
        self.connector.workers_in_or_out()
        self.connector.area_in_or_out()
        self.connector.calculate_capacity(self.choosed_area)

        self.left_section = LeftSection(self.main_window)
        self.left_section.create_workers_list(self.connector)
        self.left_section.grid_propagate(0)

        self.main_section = MainSection(self.main_window)
        self.main_section.display_area_name(self.choosed_area.name)
        self.main_section.load_date_and_time_icon()
        self.main_section.load_date(self.current_date_and_time)
        self.main_section.load_time()
        self.main_section.data_time_canvas.after(1000, self.main_section.update_time)
        self.main_section.insert_image(self.choosed_area.layout_path)
        self.main_section.load_dots(self.choosed_area.workstations, self.connector)
        self.main_section.mouse_enter_dots(self.choosed_area.workstations, self.connector)
        self.main_section.grid_propagate(0)

        self.right_section = RightSection(self.main_window)
        self.right_section.grid_propagate(0)
        self.right_section.button_canvas.tag_bind(self.right_section.button, "<Button-1>", self.quit_program)
        self.right_section.crate_title_textes()
        self.right_section.create_indexes(
            self.connector.workers_quantity,
            self.connector.workers_in_quantity,
            self.connector.workers_in_percent,
            self.connector.work_station_quantity,
            self.connector.work_station_in_quantity,
            self.connector.work_station_in_percent)

        self.time()
        
        self.main_window.mainloop()

    def quit_program(self, *args):
        self.main_window.destroy()

    def app_refresher(self, connector, left_section, main_section, right_section, time):
        
        #Refresh data from MySQL:
        self.connector = SQLConnector()
        self.connector.import_workers()
        self.connector.import_log_records(self, time)
        self.connector.workers_in_or_out()
        self.connector.area_in_or_out()
        self.connector.calculate_capacity(self.choosed_area)

        #Refresh workers list:
        self.left_section.update()
        
        for obj in self.left_section.tags_to_refresh:
            self.left_section.workers_list_canvas.delete(obj)
        
        self.left_section.create_workers_list(self.connector)

        #Refresh dots on the main layout:
        for dot in self.main_section.dots_tags:
            self.main_section.layout_canvas.delete(dot)
        
        self.main_section.load_dots(self.choosed_area.workstations,self.connector)
        self.main_section.mouse_enter_dots(self.choosed_area.workstations, self.connector)

        #Refresh area load index: 
        for obj in self.right_section.tags_to_refresh:
            self.right_section.load_index_canvas.delete(obj)
        
        self.right_section.create_indexes(
            self.connector.workers_quantity,
            self.connector.workers_in_quantity,
            self.connector.workers_in_percent,
            self.connector.work_station_quantity,
            self.connector.work_station_in_quantity,
            self.connector.work_station_in_percent)

    def time(self):
        
        refresh_frequency = ["00", "10", "20", "30", "40", "50"]
        now_time = time.strftime('%H:%M:%S')

        hours, minutes, seconds = now_time.split(":")

        if seconds in refresh_frequency:
            self.app_refresher(self.connector, self.left_section, self.main_section, self.right_section, now_time)

        self.main_window.after(1000, self.time)

app = Application()