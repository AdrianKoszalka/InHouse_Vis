class Area_model(object):

    def __init__(
        self, 
        name = "Area_name",
        polish_name = "Polish_area_name",
        workstations = {},
        layout_path = ""
    ):
        self.name = name
        self.polish_name = polish_name
        self.workstations = workstations
        self.layout_path = layout_path