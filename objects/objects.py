from models.area_model import Area_model
from sql_conector import SQLConnector

carpetry_shop = Area_model(
    name = "Carpentry Shop",
    polish_name = "Stolarnia", 
    workstations = {
        "Machine_1_1":[(470,75)],
        "Machine_1_2":[(470,155)],
        "Machine_2_1":[(470,253)],
        "Machine_2_2":[(470,332)],
        "Machine_3_1":[(760,270)],
        "Machine_3_2":[(760,77)],
        "Machine_3_3":[(1142,77)],
        "Machine_3_4":[(1142,270)],
        "Machine_4":[(1254,113)],
        "Machine_5":[(1347,605)],
        "Table_1":[(503,760)],
        "Table_2":[(630,760)],
        "Table_3":[(755,760)],
        "Table_4":[(880,760)],
        "Table_5":[(1005,760)],
        "Table_6":[(1131,760)],
        "Table_7":[(503,540)],
        "Table_8":[(630,540)],
        "Table_9":[(755,540)],
        "Table_10":[(880,540)],
        "Table_11":[(1005,540)],
        "Table_12":[(1131,540)]},
    layout_path = "layout/images/Layout3.jpg"
    )
    

other = Area_model()

objects = [carpetry_shop, other]