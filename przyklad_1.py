class Person1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Osoba o imieniu: {self.name}"


person1 = Person1("Jan")
print(str(person1))   # wywoływana jest metoda __str__()
print(person1)        # tak samo __str__()
print(repr(person1))  # brak __repr__ - dziedziczone po object

print("*" * 100)


class Person2:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Osoba o imieniu: {self.name}"

    def __repr__(self):
        # uwaga: !r wymusza formę repr na polu name
        return f"{type(self).__name__}(name = {self.name!r})"


person2 = Person2("Robert")
print(str(person2))    # __str__()
print(person2)         # __str__()
print(repr(person2))   # __repr__()

print("*" * 100)


class Person3:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{type(self).__name__}(name = {self.name!r})"


person3 = Person3("Filip")
print(str(person3))   # brak __str__ - użyty zostaje __repr__
print(person3)        # __repr__
print(repr(person3))  # __repr__
