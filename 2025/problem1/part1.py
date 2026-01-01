import utils.FileIO as FileIO

def solve() -> int:
    lines = FileIO.parse_file('/Users/sathishkumar/GitHub-nssathish/adventofcode20xx/2025/problem1/input.txt')

    # set the initial position to 50
    count = 0
    dial_pointer = 50

    for line in lines:
        operation = line[0]
        rotations = int(line[1:]) % 100

        if operation == "L":
            dial_pointer = rotate_left(dial_pointer, rotations)
        elif operation == "R":
            dial_pointer = rotate_right(dial_pointer, rotations)

        if dial_pointer == 0:
            count += 1

    return count


def rotate_left(pointer: int, rotations: int) -> int:
    pointer -= rotations
    if pointer < 0:
        pointer = 100 - abs(pointer)
    print(f'Op: "Left", Pointer: {pointer}')

    return pointer

def rotate_right(pointer: int, rotations: int) -> int:
    pointer += rotations

    if pointer >= 100:
        pointer -= 100
    print(f'Op: "Right", Pointer: {pointer}')

    return pointer


if __name__ == '__main__':
    print(solve())