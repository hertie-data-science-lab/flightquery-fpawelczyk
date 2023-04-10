# -*- coding: utf-8 -*-
"""
Date: April 10th 2023
@author: Juan Pablo Brasdefer [225936] (juanbrasdefer) Fabian Pawelczyk [226921] (fpawelczyk)
"""
from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''

    # Query method to find flights within a specified range of keys
    def query(self, k1, k2):
        # Find the first flight equal to or greater than k1
        start = self.find_ge(k1)

        # Iterate through the flights in the SortedTableMap and print flights within the specified range
        while start and start[0] <= k2:
            key, value = start
            print(f"{key[0]} -> {key[1]} @ {key[2]} {key[3]} : {value}")
            start = self.find_gt(key)

# Example usage
a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3")]

# Populate the FlightQuery object with flight data
for each in s:
    key = each[:-1]
    value = each[-1]
    a[key] = value

# Print the number of flights in the FlightQuery object
print(len(a))

# Query for flights between k1 and k2, inclusive
k1 = ("A", "B", 622, 1200)
k2 = ("A", "B", 622, 1300)
a.query(k1, k2)