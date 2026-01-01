def count_of_wave_or_parabolic(arr: list[list[int]]) -> int:
    """
    Counts the number of sublists in the given 2D list that meet specific conditions
    related to wave or parabolic patterns.

    A sublist is considered valid if:
    1. All elements are either in increasing or decreasing order, and the sublist
       satisfies the adjacent threshold limit.
    2. Alternatively, if the `tolerate_single_bad_level` parameter is enabled,
       the sublist can tolerate a single deviation from the threshold limit
       while still being in increasing or decreasing order.

    Args:
        arr (list[list[int]]): A 2D list where each sublist is evaluated for
            wave or parabolic patterns.

    Returns:
        int: The count of sublists that meet the specified conditions.
    """
    count = 0
    for elements in arr:
        if (
            all_increasing(elements.copy())
            or all_decreasing(elements.copy())
        ) and is_under_adjacent_threshold_limit(3, elements.copy()):
            count += 1
        else:
            pass
            # arr = elements.copy()
            # if is_under_adjacent_threshold_limit(3, arr, True):
            #     if all_increasing(arr) or all_decreasing(arr):
            #         count += 1
            # else:
            #     arr = elements.copy()
            #     if all_increasing(arr, True) or all_decreasing(arr, True):
            #         if is_under_adjacent_threshold_limit(3, arr):
            #             count += 1

        # elif (
        #     all_increasing(elements.copy())
        #     or all_decreasing(elements.copy())
        # ) and is_under_adjacent_threshold_limit(3, elements.copy(), True):
        #         count += 1
        # elif (
        #     all_increasing(elements.copy())
        #     or all_decreasing(elements.copy())
        # ) and is_under_adjacent_threshold_limit(3, elements.copy()):
        #     if (
        #         all_increasing(elements.copy(), True)
        #         or all_decreasing(elements.copy(), True)
        #     ):
        #         count += 1
        # else:
        #     pass

    return count


def all_increasing(arr: list[int], tolerate_single_bad_level: bool = False) -> bool:
    """
        Determines if all elements in a list are in strictly increasing order.

        Args:
            arr (list[int]): The list of integers to check.
            tolerate_single_bad_level (bool, optional): If True, allows for a single
                instance where the order is not strictly increasing by removing the
                offending element and rechecking. Defaults to False.

        Returns:
            bool: True if the list is strictly increasing (or can be made so by
            tolerating a single bad level if specified), otherwise False.
    """
    for i in range(len(arr) - 1):
        if not (arr[i] < arr[i + 1]):
            if tolerate_single_bad_level:
                del arr[i + 1]
                return all_increasing(arr)
            else:
                return False

    return True


def all_decreasing(arr: list[int], tolerate_single_bad_level: bool = False) -> bool:
    """
    Determines if all elements in the given list are in strictly decreasing order.

    Args:
        arr (list[int]): A list of integers to check.
        tolerate_single_bad_level (bool, optional): If True, allows for a single
            non-decreasing pair by removing the offending element and rechecking.
            Defaults to False.

    Returns:
        bool: True if the list is strictly decreasing (or can be made so by
        tolerating a single bad level if `tolerate_single_bad_level` is True),
        otherwise False.
    """
    for i in range(len(arr) - 1):
        if not (arr[i] > arr[i + 1]):
            if tolerate_single_bad_level:
                del arr[i]
                return all_decreasing(arr)
            else:
                return False

    return True


def is_under_adjacent_threshold_limit(
    threshold: int, arr: list[int], tolerate_single_bad_level: bool = False
) -> bool:
    """
        Determines if the differences between adjacent elements in a list are within a specified threshold.

        Args:
            threshold (int): The maximum allowable difference between adjacent elements.
            arr (list[int]): The list of integers to evaluate.
            tolerate_single_bad_level (bool, optional): If True, allows one instance of a difference
                exceeding the threshold by removing the offending element and re-evaluating.
                Defaults to False.

        Returns:
            bool: True if all adjacent differences are within the threshold (or within tolerance
            if `tolerate_single_bad_level` is True), otherwise False.
    """
    for i in range(len(arr) - 1):
        difference = abs(arr[i] - arr[i + 1])
        if difference == 0 or difference > threshold:
            if tolerate_single_bad_level:
                del arr[i + 1]
                return is_under_adjacent_threshold_limit(threshold, arr)
            else:
                return False

    return True


def file_input_to_array(file: str) -> list[list[int]]:
    """
    Reads a file and converts its contents into a 2D list of integers.

    Each line in the file is split into individual elements, which are
    converted to integers and stored as a sublist in the resulting list.

    Args:
        file (str): The path to the input file.

    Returns:
        list[list[int]]: A 2D list where each sublist contains integers
        parsed from a line in the file.

    Raises:
        ValueError: If any element in the file cannot be converted to an integer.
        FileNotFoundError: If the specified file does not exist.
    """
    arr = list()
    with open(file, encoding="utf-8") as f:
        for line in f:
            elements = list(map(int, line.split()))
            arr.append(elements)

    return arr


if __name__ == "__main__":
    parsed_array = file_input_to_array("inputs/input2.txt")
    # parsed_array = file_input_to_array("inputs/input2_test.txt")
    print(count_of_wave_or_parabolic(parsed_array))
