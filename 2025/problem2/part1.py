import utils.FileIO as FileIO

def solve():
    lines = FileIO.parse("/Users/sathishkumar/GitHub-nssathish/adventofcode20xx/2025/problem2/input.txt", {"separator": "comma"})
    count = 0

    for line in lines:
        start = int(line[0])
        end = int(line[1])
        for i in range(start, end + 1):
            string = str(i).lstrip("0")
            n = len(string)
            if n % 2 == 0 and string[0:n//2] == string[n//2:]:
                count += i
    print(count)

if __name__ == "__main__":
    solve()