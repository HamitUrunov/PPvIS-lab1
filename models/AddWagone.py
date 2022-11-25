from Wagone import Wagone
class AddWagonne(Wagone):
    def __init__(self):
        super().__init__()
        self.maxWeight = 100
        self.count = 2 
        self.time
        self.wagoneadded = False
        self.loadingCargo = False
    
    def addWagone(self):
        self.wagoneadded = True
    
    def cargoLoading(self):
         self.loadingCargo = True
