from pycparser.ply.yacc import resultlimit

import utils.FileIO as FileIO

def solve() -> int:
    lines = FileIO.parse('/Users/sathishkumar/GitHub-nssathish/adventofcode20xx/2025/problem1/input.txt')

    # set the initial position to 50
    result = 0
    dial_pointer = 50

    for line in lines:
        operation = line[0]
        rotations = int(line[1:])
        turns = rotations % 100
        result += (rotations // 100)
        zero_passed_count = 0

        if operation == "L":
            zero_passed_count, dial_pointer = rotate_left(dial_pointer, turns)
        elif operation == "R":
            zero_passed_count, dial_pointer = rotate_right(dial_pointer, turns)

        if dial_pointer == 0:
            result += (1 + zero_passed_count)

        result += zero_passed_count

    return result


def rotate_left(pointer: int, rotations: int) -> list:
    current_pointer = pointer
    pointer -= rotations
    count = 0
    if pointer < 0:
        pointer = 100 - abs(pointer)
        if current_pointer != 0 and pointer != 0:
            count = 1
    print(f'Op: "Left", Count: {count}, Pointer: {pointer}')

    return [count, pointer]

def rotate_right(pointer: int, rotations: int) -> list:
    current_pointer = pointer
    pointer += rotations
    count = 0

    if pointer >= 100:
        pointer -= 100
        if current_pointer != 0 and pointer != 0:
            count = 1
    print(f'Op: "Right", Count: {count} Pointer: {pointer}')

    return [count, pointer]


if __name__ == '__main__':
    print(solve())