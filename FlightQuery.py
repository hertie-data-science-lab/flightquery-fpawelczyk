# -*- coding: utf-8 -*-
"""
Date: April 9th 2023
@author: Juan Pablo Brasdefer [225936] (juanbrasdefer) Fabian Pawelczyk [226921] (fpawelczyk)
"""
from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''

    # Nested Key class for FlightQuery
    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"

        # Constructor to initialize origin, destination, date, and time
        def __init__(self, origin, destination, date, time):
            self._origin = origin
            self._dest = destination
            self._date = date
            self._time = time

        # Less than comparison operator for lexicographic ordering of keys
        def __lt__(self, other):
            if self._origin != other._origin:
                return self._origin < other._origin
            if self._dest != other._dest:
                return self._dest < other._dest
            if self._date != other._date:
                return self._date < other._date
            return self._time < other._time

    # Query method to find flights within a specified range of keys
    def query(self, k1, k2):
        # Create Key objects from the provided tuples
        key1 = self.Key(*k1)
        key2 = self.Key(*k2)

        # Iterate through the items in the SortedTableMap and print flights within the specified range
        for key, value in self.items():
            if key1 <= key <= key2:
                print(f"{key._origin} -> {key._dest} @ {key._date} {key._time} : {value}")


# Example usage
a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3")]

# Populate the FlightQuery object with flight data
for each in s:
    key = a.Key(*each[:-1])
    value = each[-1]
    a[key] = value

# Print the number of flights in the FlightQuery object
print(len(a))

# Query for flights between k1 and k2, inclusive
k1 = ("A", "B", 622, 1200)
k2 = ("A", "B", 622, 1300)
a.query(k1, k2)
