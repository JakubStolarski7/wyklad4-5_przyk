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
        # !r wymusza formę repr na polach; *self działa, bo obiekt jest iterowalny
        return '{0}({1!r}, {2!r})'.format(type(self).__name__, *self)

    def __str__(self):
        # „ładna” wersja: pokazujemy wartości jako krotkę
        return str(tuple(self))

    def __bytes__(self):
        # Zapis do bajtów: 1 bajt z typecode + surowe bajty z array(...)
        # Używamy encode('ascii'), bo typecode to pojedynczy znak ASCII.
        return (self.typecode.encode('ascii') +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        # Równość na bazie wartości (x, y). Działa z innymi iterowalnymi długości 2
        # (np. tuple/list). Jeśli porównanie nie ma sensu → NotImplemented.
        try:
            ox, oy = other  # duck-typing: próbujemy rozpakować obiekt po prawej
        except Exception:
            return NotImplemented
        return (self.x, self.y) == (float(ox), float(oy))

    def __abs__(self):
        # Długość wektora
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # Prawda, gdy wektor niezerowy
        return bool(abs(self))

    @classmethod
    def frombytes(cls, seq: bytes):
        typecode = chr(seq[0])
        if typecode != cls.typecode:
            raise ValueError(f"inny typecode: {typecode!r} (oczekiwano {cls.typecode!r})")
        memv = memoryview(seq[1:]).cast(typecode)
        return cls(*memv)

if __name__ == '__main__':
    # Reprezentacja bajtowa oraz odtworzenie obiektu
    v1 = Vector2D(2.5, 3.5)
    print("v1 ->", v1)
    raw = bytes(v1)
    print('bytes(v1) ->', raw)
    v1_copy = Vector2D.frombytes(raw)
    print('frombytes(bytes(v1)) ->', v1_copy, '==', v1, '->', v1_copy == v1)


    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")



