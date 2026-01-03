from utils import FileIO as io

def solve():
	lines = io.parse("input.txt", {"separator": "nl"})
	items = [list(item) for item in lines]

	valid_rolls = 0
	previous_valid_rolls = 0

	while True:
		marked_items = []
		for idx, item in enumerate(items):
			rolls, marked_item = get_valid_rolls(item, idx, items)
			valid_rolls += rolls
			marked_items.append(marked_item)

		if valid_rolls == previous_valid_rolls:
			break

		previous_valid_rolls = valid_rolls
		items = marked_items

	return valid_rolls

def get_valid_rolls(item: list, row: int, source: list[list]) -> list:
	valid_rolls = 0
	marked_item = []

	for col, item in enumerate(item):
		if item == '@':
			top_rolls: int = get_top_rolls(row, col, source)
			bottom_rolls: int = get_bottom_rolls(row, col, source)
			side_rolls: int = get_side_rolls(row, col, source)

			if top_rolls + bottom_rolls + side_rolls < 4:
				marked_item.append('.')
				valid_rolls += 1
			else:
				marked_item.append(item)
		else:
			marked_item.append(item)

	return [valid_rolls, marked_item]


def get_top_rolls(row: int, col: int, source: list[list]) -> int:
	count = 0
	top_row = row - 1
	top_cols = [col - 1, col, col + 1]
	if top_row < 0:
		return 0

	for top_col in top_cols:
		if 0 <= top_col < len(source[0]) and source[top_row][top_col] == '@':
			count += 1

	return count


def get_bottom_rolls(row: int, col: int, source: list[list]) -> int:
	count = 0
	bottom_row = row + 1
	if bottom_row >= len(source):
		return 0

	bottom_cols = [col - 1, col, col + 1]
	for bottom_col in bottom_cols:
		if 0 <= bottom_col < len(source[0]) and source[bottom_row][bottom_col] == '@':
			count += 1

	return count


def get_side_rolls(row: int, col: int, source: list[list]) -> int:
	count = 0
	side_cols = [col - 1, col + 1]
	for side_col in side_cols:
		if 0 <= side_col < len(source[0]) and source[row][side_col] == '@':
			count += 1

	return count


if __name__ == '__main__':
	print(solve())