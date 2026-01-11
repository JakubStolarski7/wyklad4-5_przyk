class Date:
    _formatting = {
        'rmd': '{d.year}-{d.month:02}-{d.day:02}',
        'mdr': '{d.month:02}/{d.day:02}/{d.year}',
        'dmr': '{d.day:02}/{d.month:02}/{d.year}',
    }

    def __init__(self, year, month, day):
        self.year  = int(year)
        self.month = int(month)
        self.day   = int(day)

    def __format__(self, fcode=''):
        code = fcode or 'rmd'        # domyślne formatowanie
        try:
            template = self._formatting[code]
        except KeyError:
            raise ValueError(f"Nieznany kod formatu: {code!r}")
        return template.format(d=self)


if __name__ == '__main__':
    date1 = Date(2009, 6, 5)

    print(format(date1))          # -> domyślnie 'rmd'
    print(format(date1, 'dmr'))
    print("Data: {:mdr}".format(date1))
    print(f"Data: {date1:mdr}")

    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")




