#!/usr/bin/env python3

# def detect_ranges(L):
#     return []

# def main():
#     L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
#     result = detect_ranges(L)
#     print(L)
#     print(result)

# if __name__ == "__main__":
#     main()
def detect_ranges(numbers):
    """
    Detects and represents ranges in a list of integers.

    Args:
        numbers: A list of unique integers.

    Returns:
        A list containing numbers and pairs representing ranges.
    """

    if not numbers:
        return []  # Return an empty list for empty input

    sorted_numbers = sorted(numbers)
    result = []
    start_range = sorted_numbers[0]
    i = 0

    while i < len(sorted_numbers):
        current_number = sorted_numbers[i]

        # Check if the current number is the last one or not contiguous
        if i == len(sorted_numbers) - 1 or sorted_numbers[i + 1] != current_number + 1:
            if start_range == current_number:  # Not a range
                result.append(start_range)
            else:  # A range detected
                result.append((start_range, current_number+1))
            if i < len(sorted_numbers) - 1:
                start_range = sorted_numbers[i + 1]
        i+=1
    return result

def main():
    print(detect_ranges([2,5,4,8,12,6,7,10,13])) # Should print [2, (4, 9), 10, (12, 14)]
    print(detect_ranges([1,2,3,4,5])) # Should print [(1,6)]
    print(detect_ranges([1,5,6,7,10,15])) # Should print [1, (5, 8), 10, 15]
    print(detect_ranges([1])) # Should print [1]
    print(detect_ranges([])) # Should print []

if __name__ == "__main__":
  main()