"""
.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|
"""
from utils import FileIO as iO
from utils import string_ops as so

def main():
    lines = iO.parse('input.txt', {'separator': '\n'})
    items = so.to_array(lines)

    items = first_beam(items)
    count = 0
    
    for i in range(2, len(items) - 1):
        item: list = items[i]
        for idx, ch in enumerate(item):
            if ch == '^' and items[i-1][idx] == '|':
                count += 1
                item[idx-1] = item[idx+1] = '|'
            elif ch == '.' and items[i-1][idx] == '|':
                item[idx] = '|'
            else:
                continue
        # print("".join(item))
    
    return count


def first_beam(items) -> list:
    torch: list = items[0]
    medium: list = items[1]
    reflector: list = items[2]

    torch_idx = torch.index('S')
    medium[torch_idx] = '|'
    if reflector[torch_idx] == '^':
        if torch_idx - 1 >= 0:
            reflector[torch_idx - 1] = '|'
        if torch_idx + 1 < len(reflector):
            reflector[torch_idx + 1] = '|'
    
    return items


if __name__ == '__main__':
    print(main())