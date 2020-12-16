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
        set_dpi_awareness()
        self.choosed_area = objects[0]
        
        # self.current_date = datetime.datetime.now() 
        self.current_date = datetime.date(2020,12,12) ##Do usunięcia
        self.current_time = datetime.time(6,53,00) ##Do usunięcia

        self.main_window = MainWindow()

        connector = SQLConnector()
        connector.import_workers()
        connector.import_log_records(self)
        connector.workers_in_or_out()
        connector.area_in_or_out()
        connector.calculate_capacity(self.choosed_area)

        left_section = LeftSection(self.main_window)
        left_section.create_workers_list(connector)
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
            connector.workers_quantity,
            connector.workers_in_quantity,
            connector.workers_in_percent,
            connector.work_station_quantity,
            connector.work_station_in_quantity,
            connector.work_station_in_percent)
        
        self.main_window.mainloop()

    def quit_program(self, *args):
        self.main_window.destroy()

app = Application()

