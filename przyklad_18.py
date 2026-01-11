import math, reprlib, numbers, functools, itertools
from array import array

class Vektor:
    typecode = 'd'  # 8-bajtowy float

    def __init__(self, components):
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
        if isinstance(index, slice):
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

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(lambda a, b: a ^ b, hashes, 0)

    def __bool__(self):
        return bool(abs(self))

    def __pos__(self):
        return type(self)(self._components)  # kopia 1 do 1

    def __neg__(self):
        return type(self)(-x for x in self._components)  # transformacja komponentów źródłowych


    def angle(self, n):
        r = math.sqrt(sum(x ** 2 for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):

        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fcode=''):
        if fcode.endswith('h'):
            fcode = fcode[:-1]
            wsp = itertools.chain([abs(self)], self.angles())
            tpl = "<{}>"
        else:
            wsp = self
            tpl = "({})"
        comps = (format(w, fcode) for w in wsp)
        return tpl.format(", ".join(comps))

    # ---------------- standardowe pola x,y,z,t ----------------
    fields = 'xyzt'

    def __getattr__(self, name):
        if len(name) == 1:
            index = type(self).fields.find(name)
            if 0 <= index < len(self._components):
                return self._components[index]
        raise AttributeError(f'Obiekt {type(self).__name__!r} nie ma atrybutu {name!r}')

    def __setattr__(self, name, value):
        if len(name) == 1:
            if name in type(self).fields:
                raise AttributeError(f'{name!r} - tylko do odczytu')
            elif name.islower():
                raise AttributeError(
                    f"nie można ustawić atrybutu o nazwach od 'a' do 'z' w klasie {type(self).__name__!r}"
                )
        super().__setattr__(name, value)

    @classmethod
    def frombytes(cls, sequence_of_bytes):
        typecode = chr(sequence_of_bytes[0])
        if typecode != cls.typecode:
            raise ValueError(f"inny typecode: {typecode!r} (oczekiwano {cls.typecode!r})")
        memv = memoryview(sequence_of_bytes[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vektor(range(5))
    print("v1 ->  ", +v1)
    print(v1 is +v1, v1 == +v1)
    print("-v1 -> ", -v1)





input("\n\nAby zakończyć program, naciśnij klawisz Enter.")



