
class Config:
    platform = "sklearn"
    input = ["Bank_Dynamic_Beta", "CMAX_Bank", "Id_Vol_Bank", "Slope", "Id_Vol_Bond", "CDS", "Id_Vol_Stock", "CMAX_Stock",
             "CMAX_Spread", "Ted","Libor", "USDTRY","EUROTRY"]
    output = "FSI"

    def __init__(self):
        pass
