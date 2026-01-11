class A:
    pass                   # brak __eq__ i __hash__ -> hash oparty o id, porównanie tożsamości

class B:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y
        # UWAGA: tu nie ma __hash__ -> obiekty NIE są haszowalne
        # (bo __eq__ zmienia semantykę równości, więc hash musi być spójny z eq)

class C:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self): return self._x
    @property
    def y(self): return self._y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # poprawny hash: XOR hashy komponentów
        return hash(self.x) ^ hash(self.y)


if __name__ == '__main__':
    a1 = A()
    b1 = A()
    a11 = a1
    print(hash(a1), hash(b1))
    print(id(a1), id(b1))
    print(a1 == b1)                      # False, bo brak __eq__ -> porównanie tożsamości
    print(a11 == a1)

    print("-" * 100)

    a2 = B(1, 2)
    b2 = B(1, 2)
    c2 = B(3, 4)
    print(id(a2), id(b2))
    print(a2 == b2, a2 == c2)            # równość działa na podstawie stanu
    print(a2 is b2, a2 is c2)            # ale tożsamość dalej False
    # print(hash(a2))  # TypeError: unhashable type: 'B'

    print("-" * 100)

    a3 = C(1, 2)
    b3 = C(1, 2)
    c3 = C(3, 4)
    print(id(a3), id(b3))
    print(a3 == b3, a3 == c3)
    print(hash(a3))                      # równe obiekty → ta sama wartość hash
    print(hash(b3))
    print(hash(c3))                      # inny stan → inny hash
