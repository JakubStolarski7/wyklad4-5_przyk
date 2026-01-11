import math, reprlib, numbers
from array import array

class Vektor:
    typecode = 'd'  # 8-bajtowy float

    def __init__(self, components):
        # components: dowolny iterowalny zbiór liczb
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        inner = reprlib.repr(self._components)
        inner = inner[inner.find('['):-1]
        return f"{type(self).__name__}({inner})"

    def __str__(self):
        return str(tuple(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        # Obsługa pojedynczego indeksu oraz wycinka.
        if isinstance(index, slice):
            # array('d')[slice] → array('d'), więc można bezpiecznie opakować w nasz typ
            return type(self)(self._components[index])
        if isinstance(index, numbers.Integral):
            return self._components[index]
        raise TypeError(f'Indeks musi być int albo slice, nie {type(index).__name__}')

    def __bytes__(self):
        return (ord(self.typecode).to_bytes(1, 'big') +
                bytes(self._components))

    def __eq__(self, other):
        try:
            return tuple(self) == tuple(other)
        except Exception:
            return NotImplemented

    def __abs__(self):
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
    v1 = Vektor(range(7))
    print('v1 ->', v1)
    print('(v1[1], v1[4]) ->', (v1[1], v1[4]))
    print('v1[1:4] ->', repr(v1[1:4]))  # nowy Vektor z podzakresem
    print('v1.__getitem__(slice(1,4,None)) ->', repr(v1.__getitem__(slice(1, 4, None))))

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")



