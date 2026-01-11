# alternatywny konstruktor
import time

class Date:
    def __init__(self, year, month, day):
        self.year  = int(year)
        self.month = int(month)
        self.day   = int(day)

    @classmethod
    def today(cls):
        # alternatywny konstruktor: zwraca instancję z aktualnej daty
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __repr__(self):
        # repr: jednoznaczna i diagnozowalna postać obiektu
        return f"{type(self).__name__}({self.year!r}, {self.month!r}, {self.day!r})"


if __name__ == '__main__':
    date1 = Date(1999, 4, 11)
    date2 = Date.today()

    print(date1)  # __repr__
    print(date2)  # __repr__

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
