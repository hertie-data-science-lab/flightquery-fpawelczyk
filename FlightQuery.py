from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expected period'''

    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"

        def __init__(self, origin, destination, date, time):
            self._origin = origin
            self._dest = destination
            self._date = date
            self._time = time

        def __lt__(self, other):
            if self._origin != other._origin:
                return self._origin < other._origin
            if self._dest != other._dest:
                return self._dest < other._dest
            if self._date != other._date:
                return self._date < other._date
            return self._time < other._time

    def query(self, k1, k2):
        key1 = self.Key(*k1)
        key2 = self.Key(*k2)

        for key, value in self.items():
            if key1 <= key <= key2:
                print(f"{key._origin} -> {key._dest} @ {key._date} {key._time} : {value}")


a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3")]

for each in s:
    key = a.Key(*each[:-1])
    value = each[-1]
    a[key] = value

print(len(a))

k1 = ("A", "B", 622, 1200)
k2 = ("A", "B", 622, 1300)
a.query(k1, k2)
