from table import Table
from table import Seat
import random


class OpenSpace:
    def __init__(self, capacity_of_table = 4, number_of_tables = 6):
        self.number_of_tables = number_of_tables
        self.tables = [] # list of tables
        capacity_of_table = Table.capacity 
        for seat_index in range(number_of_tables): # Create loop for range of tables
            new_table = capacity_of_table
            self.tables.append(new_table) # new_table added to list of tables

#THERE IS A PROBLEM HERE I COULDNT HANDLE FOR NOW
    def organize(self, names):
        self.names = names
        random(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot() == True:
                    table.assign_seat(name)


    def display(self):
        for table_index, table in enumerate(self.tables, start=1):
            print(f"Table {table_index} Capacity is {table.capacity}")
            for seat_index, seat in enumerate(table.seats, start=1):
                if seat.free == False:
                    print(f"{seat.occupant} seating on the Seat {table_index} ")
                #else:
                    #print(f"Seat {table_index} is Empty")    

    def store(self,filename):
        self.filename = filename
        





