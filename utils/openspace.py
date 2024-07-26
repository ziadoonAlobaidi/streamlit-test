from utils.table import Table
from utils.table import  Seat
import numpy as np

class Openspace:

    def __init__(self, number_of_tables, seats_per_table):
        self.number_of_tables = number_of_tables
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]

    def organize(self, names: str):
        """
        Randomly assign people to Seat objects in the different Table objects.
        """
        np.random.shuffle(names)
        name_index = 0
        total_seats = sum(len(table.seats) for table in self.tables)

        if len(names) > total_seats:
            raise ValueError("There are more names than seats available.")

        for table in self.tables:
            for seat in table.seats:
                if name_index < len(names):
                    seat.occupant = names[name_index]
                    name_index += 1
                else:
                    seat.occupant = None  # If there are more seats than names

    def display(self):
        """
        Display the different tables and their occupants in a nice and readable way.
        """
        occupants = {}
        for idx, table in enumerate(self.tables):
            table_key = f"Table {idx + 1}"
            occupants[table_key]=[]
            for seat in table.seats:
                occupant = seat.occupant if seat.occupant else "Empty"
                occupants[table_key].append(occupant)
        return occupants
