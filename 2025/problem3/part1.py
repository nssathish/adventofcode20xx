import utils.FileIO as FileIO

def solve():
    lines = FileIO.parse("/Users/sathishkumar/GitHub-nssathish/adventofcode20xx/2025/problem3/input.txt", {"separator": "nl"})
    print(lines)
    count = 0
    for line in lines:
        max = get_max(line)
        print(max)
        count += max

    print(count)


def get_max(number: str) -> int:
    max1 = number[0]
    max2 = number[1]
    max = int(max1 + max2)

    for i in range(2, len(number)):
        if int(max1 + number[i]) > max and int(max2 + number[i]) < int(max1 + number[i]):
            max = int(max1 + number[i])
            max2 = number[i]
        elif int(max2 + number[i]) > max:
            max = int(max2 + number[i])
            max1 = max2
            max2 = number[i]
        else:
            continue

    return max

def get_max_12(number: str) -> int:
    start = number[0]

    i = 1
    count = 0
    n = len(number)
    while count < 12:
        current_integer = int(number[i])
        if current_integer > start:
            start = int(number[i])

if __name__ == "__main__":
    solve()
