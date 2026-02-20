# Write a class Train which has methods to book a ticket, get Status (no of seats) and get fare information of 
# trains running under American Railways.
"""
1 2 3 4 5 6 7 8 9 10
"""
class Train:
    def __init__(self, name, fear, seat):
        self.name = name
        self.fear = fear
        self.seat = seat
    
    def getStatus(self):
        print(f"The name of the train is {self.name}.")
        print(f"The seats available in the train are {self.seat}.")

    def fareInformation(self):
        print(f"The price of the NY Express train is ${self.fear}.")

    def bookTickets(self):
        if(self.seat > 0):
            print(f"Your ticket has been booked! Your ticket number is {self.seat}.")
            self.seat = self.seat - 1
        else:
            print("Sorry the ticket is full. Try next time.\n")

    def cancelTicket(self, seatNo):
        pass

America = Train("NY Express: 1212", 1000, 2)
America.getStatus()
America.bookTickets()
America.bookTickets()
America.bookTickets()
America.getStatus()



    