import math
from array import array

class Vector2D:
    # Atrybut klasy typecode określa format liczbowy używany przy konwersji do/z bajtów.
    # 'd' = float64 (minimum: 8 bajtów na liczbę).
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        # Dzięki iterowalności możemy łatwo pisać tuple(self), *self itd.
        return (e for e in (self.x, self.y))

    def __repr__(self):
        # !r wymusza formę repr na polach; *self działa, bo obiekt jest iterowalny.
        return '{0}({1!r}, {2!r})'.format(type(self).__name__, *self)

    def __str__(self):
        # „Ładna” wersja: pokazujemy wartości jako krotkę.
        return str(tuple(self))

    def __bytes__(self):
        # Zapis do bajtów: 1 bajt z typecode + surowe bajty z array(...)
        # Używamy encode('ascii'), bo typecode to pojedynczy znak ASCII.
        return (self.typecode.encode('ascii') +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        # Równość po wartościach (x, y). Działa też dla iterowalnych długości 2.
        try:
            ox, oy = other  # duck-typing: próbujemy rozpakować other
        except Exception:
            return NotImplemented
        return (self.x, self.y) == (float(ox), float(oy))

    def __abs__(self):
        # Długość wektora.
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # True gdy wektor niezerowy.
        return bool(abs(self))

    def angle(self):
        # Kąt w RADIANACH (atan2).
        return math.atan2(self.y, self.x)

    def __format__(self, fcode: str = ''):
        """
        Obsługiwane specyfikatory:
          - standardowe float formaty (np. '', '.3f', '.2e', itp.)
          - sufiks 'p' => format w POLARNYCH: <r, theta>, gdzie r=|v|, theta=atan2(y,x) [radiany]
            np. 'p', '.3fp', '.2ep'
        """
        if fcode.endswith('p'):
            base = fcode[:-1]     # np. '.3f' z '.3fp'
            parts = (abs(self), self.angle())
            template = '<{}, {}>'
        else:
            base = fcode
            parts = self
            template = '({}, {})'
        comps = (format(c, base) for c in parts)
        return template.format(*comps)

    @classmethod
    def frombytes(cls, seq: bytes):
        typecode = chr(seq[0])
        if typecode != cls.typecode:
            raise ValueError(f"inny typecode: {typecode!r} (oczekiwano {cls.typecode!r})")
        memv = memoryview(seq[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':
    v1 = Vector2D(2.45, 3.55)
    print('współrzędne biegunowe ->', format(v1, 'p'))
    print('współrzędne biegunowe ->', format(v1, '.3ep'))
    print('współrzędne biegunowe ->', format(v1, '.5fp'))
    print('współrzędne kartezjańskie ->', format(v1))
    print('współrzędne kartezjańskie ->', format(v1, '.1f'))
    print('współrzędne kartezjańskie ->', f"{v1:.1f}")
    print('współrzędne kartezjańskie ->', f"{v1:.1fp}")

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
