from utils import FileIO as iO

def solve():
    lines = iO.parse('input.txt', {'separator': '\n'})

    ranges = [list(map(int, line.split('-'))) for line in lines if '-' in line]
    ingredients = [int(line) for line in lines if '-' not in line and len(line)]

    fresh_ingredients = [get_fresh_ingredients(ingredient, ranges) for ingredient in ingredients]
    print(sum(fresh_ingredients))


def get_fresh_ingredients(ingredient, ranges) -> int:
    for ingredient_range in ranges:
        if ingredient in range(ingredient_range[0], ingredient_range[1] + 1):
            return 1
    return 0


if __name__ == '__main__':
    solve()