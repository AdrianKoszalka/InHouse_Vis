from windows import set_dpi_awareness
from layout.left_section import LeftSection
from layout.main_section import MainSection
from layout.right_section import RightSection
from layout.main_window import MainWindow
from objects.objects import objects


class Application():
    def __init__(self, *args, **kwargs):
        
        self.choosed_area = objects[0]
        
        set_dpi_awareness()

        main_window = MainWindow()

        left_section = LeftSection(main_window)
        left_section.grid_propagate(0)

        main_section = MainSection(main_window)
        main_section.display_area_name(self.choosed_area.name)
        main_section.grid_propagate(0)

        right_section = RightSection(main_window)
        right_section.grid_propagate(0)

        main_window.mainloop()

app = Application()