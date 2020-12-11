class Area_model(object):

    def __init__(
        self, 
        name = "Area_name",
        polish_name = "Polish_area_name",
        workers_quantity = 0, 
        workers_in_quantity = 0,
        workers_in_percent = 0,
        workstation_quantity = 0,
        workstation_used_quantity = 0,
        workstation_used_percent = 0
    ):
        self.name = name
        self.polish_name = polish_name
        self.workers_quantity = workers_quantity
        self.workers_in_quantity = workers_in_quantity
        self.workers_in_percent = workers_in_percent
        self.workstation_quantity = workstation_quantity
        self.workstation_used_quantity = workstation_used_quantity
        self.workstation_used_percent = workstation_used_percent