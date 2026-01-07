from utils import FileIO as iO

def main():
    lines = iO.parse("input.txt", {'separator': 'nl'})
    items = [list(map(lambda x: to_integer(x), [item for item in line.split(' ') if item != ''])) for line in lines[:len(lines) - 1]]
    print(items)

    rows = len(items)
    cols = len(items[0])
    symbols = [symbol for symbol in lines[len(lines) - 1].split(' ') if symbol != '']

    print(symbols)

    symbol_idx = 0
    total = 0

    for col in range(cols):
        count = 1 if symbols[symbol_idx] == '*' else 0

        for row in range(rows):
            if symbols[symbol_idx] == '*':
                count *= items[row][col]
            elif symbols[symbol_idx] == '+':
                count += items[row][col]

        symbol_idx += 1

        total += count

    print(total)


def to_integer(s):
    s = s.replace(' ', '')
    return int(s)


if __name__ == '__main__':
    main()