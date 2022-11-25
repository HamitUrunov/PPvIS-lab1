from models.Station import Station
class Ways():

    def __init__(self):
        self.Toshkent = Station("Toshkent") 
        self.Samarkand = Station("Samarkand", 3)
        self.Buhara = Station("Buhara", 6)
        self.Hiva = Station("Hiva", 8)
        self.Shimkent = Station("Shimkent",5)
        self.firstWay = [self.Toshkent.name, self.Samarkand.name,self.Shimkent.name]
        self.secondWay = [self.Toshkent.name, self.Buhara.name,self.Hiva.name]
        self.thirdWay = [ self.Shimkent.name, self.Samarkand.name,self.Toshkent.name]
