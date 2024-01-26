class Seat:
    def __init__(self, occupant = None, free = True):
       self.free = free
       self.occupant = occupant


    def set_occupant(self, name): # bool
        self.name = name
        if self.free == True: #checks if seat free
            self.occupant = name
            self.free = False # returns False because seat is not free anymore
            print(f"{self.occupant} has occupied the seat")
        else: 
            print("Seat is already occupied")        
            
        
    def remove_occupant(self, prv_name):
       self.prv_name = prv_name
       if self.free == False: # cheks if seat already occupied
           self.prv_name = self.occupant
           self.free = True
           self.occupant = None
           return prv_name
       else:
           print("seat is empty")
       
           

class Table():
    def __init__(self, seats, capacity = 4):
        self.capacity = capacity
        self.seats = [] # create empty list
        for seat_index in range(capacity):# 
            new_seat = Seat()
            self.seats.append(new_seat)
        

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free == True: #self.free not working we need to use seat.free because free is Seat's attribute
                return "There is an available seat"    

        
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free == True:
                seat.set_occupant(name)
                return (f"{name} has occupied the seat")


    def capacity_left(self):
        free_seats = 4
        for seat in self.seats:
            if seat.free == False:
                free_seats -= 1
        return (f"{free_seats} capacity left")        

            



""" TESTS
seat = Seat(occupant="Mehmet", free = False)
print("Is the seat free?: ",seat.free)
seat.remove_occupant("Mehmet")
print("Is the seat free?: ",seat.free)
seat.set_occupant("Mimoun")
print("Is the seat free?: ",seat.free)
print("Who is occupant: ",seat.occupant)

table = Table(seat, capacity = 4)
result = table.has_free_spot()
print(result)
result1 = table.assign_seat("Mehmet")
print(result1)
result2 = table.capacity_left()
print(result2)
result3 = table.assign_seat("Marten")
print(result3)
result4 = table.capacity_left()
print(result4) """

