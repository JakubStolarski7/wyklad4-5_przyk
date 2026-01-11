import math, reprlib
from array import array

class Vektor:
    typecode = 'd'  # 8-bajtowy float

    def __init__(self, components):
        # components: dowolny iterowalny zbiór liczb
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        inner = reprlib.repr(self._components)   # bez castowania do listy
        inner = inner[inner.find('['):-1]        # wycięcie "array('d'," i ')'
        return f"{type(self).__name__}({inner})"

    def __str__(self):
        # „ładna” wersja - jako krotka liczb
        return str(tuple(self))

    def __bytes__(self):
        # 1 bajt typecode + surowe bajty tablicy
        return (ord(self.typecode).to_bytes(1, 'big') +
                bytes(self._components))

    def __eq__(self, other):
        # porównanie wartościowe dla dowolnych iterowalnych
        try:
            return tuple(self) == tuple(other)
        except Exception:
            return NotImplemented

    def __abs__(self):
        # norma euklidesowa w N wymiarach
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, sequence_of_bytes):
        # zgodne z 2D: pierwszy bajt = typecode, reszta = dane
        typecode = chr(sequence_of_bytes[0])
        if typecode != cls.typecode:
            raise ValueError(f"inny typecode: {typecode!r} (oczekiwano {cls.typecode!r})")
        memv = memoryview(sequence_of_bytes[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vektor([2, 3, 4, 5, -3, 4, 7])
    print('v1 ->', v1)                 # str
    print('repr(v1) ->', repr(v1))     # repr
    print('abs(v1) ->', abs(v1))       # norma
    raw = bytes(v1)
    v2 = Vektor.frombytes(raw)
    print('v2 == v1 ->', v2 == v1)
