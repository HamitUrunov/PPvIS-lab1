from Ticket import Ticket
class Passangers(Ticket):
    def __init__(self,seatNumber,baggage):
        self.seatNumber = seatNumber
        self.baggage = baggage