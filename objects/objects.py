from models.area_model import Area_model
from sql_conector import SQLConnector

carpetry_shop = Area_model(
    name = "Carpentry Shop",
    polish_name = "Stolarnia", 
    workstations = {
        "Machine_1_1":[(310,113)],
        "Machine_1_2":[(310,185)],
        "Machine_2_1":[(310,280)],
        "Machine_2_2":[(310,352)],
        "Machine_3_1":[(620,285)],
        "Machine_3_2":[(620,120)],
        "Machine_3_3":[(1012,120)],
        "Machine_3_4":[(1012,285)],
        "Machine_4":[(1135,148)],
        "Machine_5":[(1233,620)],
        "Table_1":[(345,745)],
        "Table_2":[(477,745)],
        "Table_3":[(609,745)],
        "Table_4":[(742,745)],
        "Table_5":[(874,745)],
        "Table_6":[(1006,745)],
        "Table_7":[(345,540)],
        "Table_8":[(477,540)],
        "Table_9":[(609,540)],
        "Table_10":[(742,540)],
        "Table_11":[(874,540)],
        "Table_12":[(1006,540)]},
    layout_path = "layout/images/Layout3.jpg"
    )
    

other = Area_model()

objects = [carpetry_shop, other]