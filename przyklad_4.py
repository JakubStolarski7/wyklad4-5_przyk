# porównanie dekoratorów @classmethod i @staticmethod

class A:
    @staticmethod
    def method_st(*args):
        # metoda statyczna -> nie dostaje ani self, ani cls
        return args

    @classmethod
    def method_cl(cls, *args):
        # metoda klasowa -> pierwszy argument to klasa (cls)
        return (cls, args)

    def method(self, *args):
        # zwykła metoda -> pierwszy argument to instancja (self)
        return (self, args)


if __name__ == '__main__':
    print(A.method_cl())              # cls = A
    print(A.method_cl('arg1', 'arg2'))
    print()

    print(A.method_st())              # brak self/cls
    print(A.method_st('arg1', 'arg2'))
    print()

    print(A().method())               # self = instancja A
    print(A().method('arg1', 'arg2'))

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
