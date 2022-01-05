class Train:

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.availableSeats = []
        for i in range(1, seats + 1): self.availableSeats.append(i)

    def bookTicket(self):
        if self.seats > 0:
            print("Congratulations! you have successfully booked your ticket!")
            print(f"Your seat number is {self.availableSeats.pop()}")
            self.seats -= 1
        else:
            print("Sorry, you cannot book ticket as there is no empty seat!")

    def getStatus(self):
        print(f"The number of empty seats available are {self.seats}")

    def getFare(self):
        print(f"The fare of the train is Rs. {self.fare}")
    
    def cancelTicket(self, seatNo):
        self.availableSeats.append(seatNo)
        self.seats += 1
        print("Your ticket has been cancelled successfully! You will receive your refund soon.")

rajdhani = Train("Rajdhani", 2100, 10)

# rajdhani.getFare()
rajdhani.getStatus()
rajdhani.bookTicket()
# rajdhani.getStatus()
rajdhani.bookTicket()
rajdhani.bookTicket()
rajdhani.cancelTicket(9)
rajdhani.bookTicket()
rajdhani.getStatus()