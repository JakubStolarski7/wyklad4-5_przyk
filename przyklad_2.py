# Surowe bajty
s = 'dąbek'               # napis Unicode: 5 znaków
print(s)
print(len(s))

print("-"*80)
b1 = s.encode('utf-8')    # kodowanie str -> bytes w UTF-8 (b1: sekwencja bajtów, niemutowalna)
print(b1)
print(len(b1))            # b1 ma 6 bajtów; znak "ą" koduje się jako 2 bajty w UTF-8
print(b1.decode('utf-8')) # dekodowanie bytes -> str (UTF-8)

print("-"*80)
b2 = bytes(s, encoding='utf-8')   # alternatywny sposób utworzenia bytes
print(b2)

print("-"*80)
print(b2[0])              # element bytes to liczba z zakresu 0..255 (tu: pierwszy bajt)
print(b2[:1])             # wycinek bytes jest wciąż typu bytes (nie int)

print("-"*80)
ba = bytearray(b2)        # bytearray: sekwencja bajtów MUTOWALNA
print(ba)
print(ba[-1:])            # wycinek bytearray daje bytearray
ba[0] = b'z'[0]           # modyfikacja na miejscu (mutowalność bytearray)
print(f"{ba.decode('utf-8') = }")

print("-"*80)
# Tworzenie tablicy z surowych danych (obiekt bytes)
import array
numbers1 = array.array('h', [-3, -1, 0, 1, 3])   # 'h' = 16-bitowe liczby całkowite (signed short)
print(numbers1)

b3 = bytes(numbers1)                             # surowe bajty z zawartości tablicy
print(f'{b3 = }')

numbers2 = array.array('h')                      # pusta tablica 16-bitowych intów
numbers2.frombytes(b3)                           # alternatywna inicjalizacja z bajtów
print(f'{numbers2 = }')                          # ta sama zawartość co numbers1

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")