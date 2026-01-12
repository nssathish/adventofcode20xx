from utils import FileIO as iO

def solve():
    lines = iO.parse('input.txt', {'separator': '\n'})

    ingredient_ids = sorted(list(map(int, line.split('-'))) for line in lines if '-' in line)

    previous_end = 0
    count = 0
    for start, end in ingredient_ids:
        if start > previous_end:
            count += end - start + 1
            previous_end = end
        else:
            overlap = end - previous_end
            if overlap > 0:
                count += overlap
                previous_end = end

    print(count)


if __name__ == '__main__':
    solve()
