from models.area_model import Area_model

carpetry_shop = Area_model(
    name = "Carpentry Shop",
    polish_name = "Stolarnia",
    workers_in_quantity= 10,
    workers_quantity= 20,
    workers_in_percent= 50
)

other = Area_model()

objects = [carpetry_shop, other]