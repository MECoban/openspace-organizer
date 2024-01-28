from table import Table
from table import Seat
import random


class OpenSpace:
    def __init__(self, capacity_of_table : int = 4, number_of_tables : int = 6):
        self.number_of_tables = number_of_tables
        self.capacity_of_table = capacity_of_table
        self.tables = [Table() for i in range(self.number_of_tables)]# list of tables

    def organize(self, names : list):
        self.names = names
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot() == True: #checks free seats with has_free_spot method from table class
                    table.assign_seat(name) #assings a person with assign_seat method from table class
                    break
        if len(names) > len(self.tables)*4: # 
            raise ValueError("There is too much people for 24 seat")


    def display(self):
        for table_index, table in enumerate(self.tables, start=1):
            print(f"Table {table_index} Capacity is {Table.capacity}")
            for seat_index, seat in enumerate(table.seats, start=1):
                if seat.free == False:
                    print(f"{seat.occupant} seating on the Seat {table_index} ")
                else:
                    print(f"Seat {table_index} is Empty")    

    """Store the repartition in filename """

    def store(self,filename):
        self.filename = filename
        filename = "/Users/mehmet/Desktop/openspace-organizer/openspace-organizer-1/colleagues.txt"
        with open(filename, "w") as output_filename:
            for table_index, table in enumerate(self.tables):
                for seat_index, seat in enumerate(table.seats):
                    if seat.free == False:
                        output_filename.write(f"{Seat.occupant} sitting on Table {table_index}, Seat{seat_index} ")
                    else:
                        output_filename.write(f"Table{table_index}, Seat{seat_index} is Free ")