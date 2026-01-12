from utils import FileIO as iO


def main():
    lines = iO.parse('input.txt', {'separator': '\n'})
    symbols = []
    symbols_line = lines[-1]
    i = 0

    for j in range(1, len(symbols_line)):
        if symbols_line[j] != ' ':
            symbols.append(symbols_line[i:j])
            i = j
    else:
        symbols.append(symbols_line[i:])

    lines = lines[: -1]

    items = split_by_symbol_length(lines, symbols)
    print(calculate(items, symbols))


def calculate(items, symbols):
    symbols = [symbol.strip() for symbol in symbols]
    outer_cols_range = len(items)
    total = 0

    for outer_col in range(outer_cols_range):
        inner_col_items = items[outer_col]
        inner_col_range = len(inner_col_items[0])
        total += calculate_inner_columns(inner_col_range, inner_col_items, symbols[outer_col])
    return total


def calculate_inner_columns(inner_col_range, inner_col_items, symbol):
    result = 1 if symbol == '*' else 0
    inner_rows_range = len(inner_col_items)

    for inner_col in range(inner_col_range):
        inner_col_result = [inner_col_items[i][inner_col] for i in range(inner_rows_range) if inner_col_items[i] != '']
        if symbol == '*':
            try:
              result *= int(''.join(inner_col_result))
            except ValueError:
                print(f'Multiplication Value Error: {inner_col_items}')

        elif symbol == '+':
            try:
              result += int(''.join(inner_col_result))
            except ValueError:
                print(f'Addition Value Error: {inner_col_items}')

    return result


def split_by_symbol_length(lines, symbols):
    result = []
    rows = len(lines)
    col_pointer = 0
    symbol_idx = 0
    symbols_length = sum([len(symbol) for symbol in symbols])

    while col_pointer < symbols_length:
        symbol_length = len(symbols[symbol_idx]) if symbol_idx < len(symbols) - 1 else len(symbols[symbol_idx]) + 1
        row_items = []

        for row in range(rows):
            if symbol_length > len(lines[row][col_pointer:]):
                column_items = lines[row][col_pointer:]
            else:
                column_items = lines[row][col_pointer:col_pointer + symbol_length - 1]

            if len(column_items) < symbol_length - 1:
                spaces = ' ' * (symbol_length - 1 - len(column_items))
                column_items += spaces

            row_items.append(column_items)

        result.append(row_items)
        col_pointer += symbol_length
        symbol_idx += 1

    return result


if __name__ == '__main__':
    main()