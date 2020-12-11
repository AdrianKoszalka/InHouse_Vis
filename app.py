import tkinter as tk
import datetime

from windows import set_dpi_awareness
from layout.left_section import LeftSection
from layout.main_section import MainSection
from layout.right_section import RightSection
from layout.main_window import MainWindow
from objects.objects import objects
from sql_conector import SQLConnector


class Application():
    def __init__(self, *args, **kwargs):
        
        self.choosed_area = objects[0]
        
        self.current_date = datetime.datetime.now()

        print(self.current_date)
        set_dpi_awareness()

        self.main_window = MainWindow()

        left_section = LeftSection(self.main_window)
        left_section.grid_propagate(0)

        main_section = MainSection(self.main_window)
        main_section.display_area_name(self.choosed_area.name)
        main_section.load_date_and_time_icon()
        main_section.load_date(self.current_date)
        main_section.grid_propagate(0)

        right_section = RightSection(self.main_window)
        right_section.grid_propagate(0)
        right_section.button_canvas.tag_bind(right_section.button, "<Button-1>", self.quit_program)
        right_section.create_indexes(
            self.choosed_area.workers_quantity,
            self.choosed_area.workers_in_quantity,
            self.choosed_area.workers_in_percent,
            self.choosed_area.workstation_quantity,
            self.choosed_area.workstation_used_quantity,
            self.choosed_area.workstation_used_percent)

        connector = SQLConnector()
        connector.import_workers()
        connector.import_log_records(self)
        

        self.main_window.mainloop()

    def quit_program(self, *args):
        self.main_window.destroy()

app = Application()

