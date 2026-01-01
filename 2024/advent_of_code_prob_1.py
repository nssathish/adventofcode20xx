from os import path


def split_int_arrays(file: path) -> ([list[int], list[int]]):
    arr1 = list()
    arr2 = list()

    with open(file) as f:
        for line in f:
            element1, element2 = line.strip("\n").split()
            arr1.append(int(element1))
            arr2.append(int(element2))

    return [arr1, arr2]


def sum_of_difference(arr1: list[int], arr2: list[int]) -> int:
    arr1.sort()
    arr2.sort()

    return sum([abs(arr1[i] - arr2[i]) for i in range(len(arr1))])


def sum_of_num_of_occurrences(arr1: list[int], arr2: list[int]) -> int:
    cache = dict()
    for num in arr2:
        if num not in cache:
            cache[num] = num
        else:
            cache[num] += num

    return sum ([cache[value] if value in cache else 0 for value in arr1])

if __name__ == "__main__":
    arr1, arr2 = split_int_arrays("inputs/input1.txt")
    print(sum_of_difference(arr1, arr2))
    print(sum_of_num_of_occurrences(arr1, arr2))