# definicja dekoratora klasy

def complete_comparisons(cls):
    assert cls.__lt__ is not object.__lt__, (
        f"{cls.__name__} musi definiować '<'")
    if cls.__eq__ is object.__eq__:
        cls.__eq__ = lambda self, other: not (cls.__lt__(self, other) or cls.__lt__(other, self))
    cls.__ne__ = lambda self, other: not cls.__eq__(self, other)
    cls.__gt__ = lambda self, other: cls.__lt__(other, self)
    cls.__le__ = lambda self, other: not cls.__lt__(other, self)
    cls.__ge__ = lambda self, other: not cls.__lt__(self, other)
    return cls

# Można wykorzytać wbudowany dekorator: functools.total_ordering
#(ale należy zdefiniować jeszcze metodę __eq__())
# import functools
# @functools.total_ordering
@complete_comparisons
class FuzzyBool:
    def __init__(self, value=0.0):
        self._value = value if 0.0 <= value <= 1.0 else 0.0

    def __invert__(self):
        return FuzzyBool(1.0 - self._value)

    def __and__(self, other):
        return FuzzyBool(min(self._value, other._value))

    def __iand__(self, other):
        self._value = min(self._value, other._value)
        return self

    @staticmethod
    def conjunction(*fuzzies):
        return FuzzyBool(min([float(x) for x in fuzzies]))

    def __or__(self, other):
        return FuzzyBool(max(self._value, other._value))

    def __ior__(self, other):
        self._value = max(self._value, other._value)
        return self
    
    @staticmethod
    def disjunction(*fuzzies):
        return FuzzyBool(max([float(x) for x in fuzzies]))

    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__,self._value))

    def __str__(self):
        return str(self._value)

    def __bool__(self):
        return self._value > 0.5

    def __int__(self):
        return round(self._value)

    def __float__(self):
        return self._value

    def __lt__(self, other):
        return self._value < other._value

    def __eq__(self, other):
        return self._value == other._value


    def __format__(self, format_spec):
        return format(self._value, format_spec)

if __name__ == '__main__':
    fb1 = FuzzyBool(0.2)
    fb2 = FuzzyBool(0.6)
    fb3 = FuzzyBool(7)
    print('r1 ->', fb1)
    print('r2 ->', fb2)
    print('r3 ->', fb3)
    print('~r1 ->', ~fb1)
    print('r1 | r2 ->', fb1 | fb2)
    print('r1 & r2 ->', fb1 & fb2)
    print('r1 < r2 ->', fb1 < fb2)
    print('r1 >= r2 ->', fb1 >= fb2)
    print('FuzzyBool.conjunction(r1,r2,r3) ->',
          FuzzyBool.conjunction(fb1,fb2,fb3))
    print('FuzzyBool.disjunction(r1,r2,r3) ->',
       FuzzyBool.disjunction(fb1,fb2,fb3))

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
