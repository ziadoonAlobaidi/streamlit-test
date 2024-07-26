# Each function or class has to be typed.
from typing import Optional, List


class Seat:
    # Initializing 2 attributes (free, occupant).
    def __init__(self, free: bool = True, occupant:str = "") -> None:
        # Should be boolean.
        self.free: bool = free
        # Should be string.
        self.occupant: str = occupant

    # set_occupant method allows to assign a seat if it's free, otherwise returns message.
    def set_occupant(self, name:str) -> str:
        """
        Function that allows to assign a seat if it's free, otherwise returns message.

        :param name: Name of a person that you want to assign a seat.
        :return: Returns to whom the seat was assigned or if the seat is free.
        """
        if self.free:
            self.occupant = name
            self.free = False
            return f"Seat assigned to {name}"
        else:
            return 'Seat is not free'

    # remove_occupant method removes someone from a seat and returns name of the person.
    def remove_occupant(self) -> str:
        """
        Function that allows to remove someone from a seat and returns name of the person.

        :param self:
        :return: Returns the name of the person that you want to remove or if seat is free.
        """
        if self.free is False:
            previous_occupant = self.occupant
            self.occupant = ""
            self.free = True
            return f"Removed occupant: {previous_occupant}"
        if self.free:
            return "Seat is already free"

    # __str__ shows status of an object that belongs to the class (Seat).
    def __str__(self) -> str:
        """
        Function that shows status of an object that belongs to the class (Seat).

        :param self:
        :return: Returns the status of a seat.
        """
        status: str = "free" if self.free else "occupied"
        return f"Seat is {status}. Occupant: {self.occupant}"


# I am gonna create table class in table.py

class Table:
    """
    A class to represent a table with a certain capacity of seats.

    Attributes
    ----------
    capacity : int
        The number of seats at the table.
    seats : List[Seat]
        The list of seats at the table.

    Methods
    -------
    has_free_spot() -> bool:
        Checks if there is at least one free seat at the table.
    assign_seat(name: str) -> str:
        Assigns a seat to the given name if there is a free seat.
    left_capacity() -> int:
        Returns the number of free seats at the table.
    __str__() -> str:
        Returns a string representation of the table.
    """



    def __init__(self, capacity: int):

        """
        Initializes a new Table instance with the given capacity.

        :param capacity: The number of seats at the table.
        """ 

        self.capacity: int = capacity
        self.seats: List[Seat] = [Seat() for i in range(capacity)]


    def has_free_spot(self) -> bool:
        
        """
        Checks if there is at least one free seat at the table.

        :return: True if there is a free seat, False otherwise.
        """

        for seat in self.seats:
            if seat.free:
                return True
        return False         
    
    def assign_seat(self, name: str) -> str:
        """
        Assigns a seat to the given name if there is a free seat.

        :param name: The name to assign to a free seat.
        :return: A message indicating whether the seat was assigned or if there are no free seats.
        """ 
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return f"Seat assigned to {name}"
        return "No free seats left"        


    def left_capacity(self)-> int:
        """
        Returns the number of free seats at the table.

        :return: The number of free seats.
        """
        return sum(seat.free for seat in self.seats)
    
    def __str__(self) -> str:
        """
        Returns a string representation of the table.

        :return: A string indicating the total and free seats at the table.
        """
        return f"Table with {self.capacity} seats. {self.left_capacity()} left"







