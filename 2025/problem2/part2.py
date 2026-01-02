import re
import utils.FileIO as FileIO

def solve():
    lines = FileIO.parse("/Users/sathishkumar/GitHub-nssathish/adventofcode20xx/2025/problem2/input1.txt", {"separator": "comma"})
    count = 0

    for line in lines:
        start = int(line[0])
        end = int(line[1])
        for i in range(start, end + 1):
            string = str(i).lstrip("0")
            n = len(string)
            if (n % 2 == 0 and string[0:n//2] == string[n//2:]) or (repeats_by_math(string)):
                print(string)
                count += i

    print(count)

#50793864718
def repeats_by_regex(string: str) -> bool:
    for i in range(len(string)):
        # match the patter and return if the match is successful
        match = re.match(f"({string[:i]})+$", string)
        if match:
            print(string)
            return True
    return False


def repeats_by_math(string: str) -> bool:
    number = int(string)
    start = 0 if string[0] != "1" else 1
    n = len(string)

    for i in range(start, n):
        divisor = int(string[:i+1])
        if number % divisor == 0:
            quotient = number // divisor
            if palindrome(str(quotient)):
                return True
            else:
                continue
        else:
            continue

    return False

def palindrome(string: str) -> bool:
    return len(string) > 1 and string[::-1] == string


if __name__ == "__main__":
    solve()