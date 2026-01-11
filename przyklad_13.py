# jak działa wycinanie
class A:
    def __getitem__(self, index):
        return index  # zwracamy dokładnie to, co Python przekazał


if __name__ == '__main__':
    a = A()

    def show(label, value):
        print(f"{label:18} -> {value!r:20}  (type: {type(value).__name__})")

    show('a[1]', a[1])                         # int
    show('a[8]', a[8])                         # int
    show('a[1:5]', a[1:5])                     # slice(1, 5, None)
    show('a[1:7:4]', a[1:7:4])                 # slice(1, 7, 4)
    show('a[1:]', a[1:])                       # slice(1, None, None)

    # indeksowanie wielowymiarowe -> tuple elementów (int/slice/...)
    show('a[1:5:2, 1]', a[1:5:2, 1])           # (slice(1, 5, 2), 1)
    show('a[1:5:2, 1:7]', a[1:5:2, 1:7])       # (slice(1, 5, 2), slice(1, 7, None))

    print()

    # Praktyczne użycie slice.indices(sequence_length):
    s = 'DOMEK'
    print('s ->', s)
    print('s[:20:2] ->', s[:20:2])             # wycinek z "dużym" stopniem i końcem
    print('s[-7:8] ->', s[-7:8])               # wycinek z indeksami ujemnymi / poza zakresem

    # Normalizacja parametrów slice względem długości sekwencji:
    norm1 = slice(None, 20, 2).indices(len(s))   # -> (start, stop, step) po „przycięciu”
    norm2 = slice(-7, 8, None).indices(len(s))
    norm3 = slice(1, None, None).indices(len(s))
    print('slice(None,20,2).indices(len(s)) ->', norm1)
    print('slice(-7,8,None).indices(len(s)) ->', norm2)
    print('slice(1,None,None).indices(len(s)) ->', norm3)

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
