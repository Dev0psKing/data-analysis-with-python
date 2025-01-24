#!/usr/bin/env python3

# def interleave(*lists):
#     return []

# def main():
#     print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

# if __name__ == "__main__":
#     main()
def interleave(*lists):
    """
    Interleaves elements from multiple lists into a single list.

    Args:
        *lists: An arbitrary number of lists of equal length.

    Returns:
        A new list containing elements from the input lists interleaved.
    """
    result = []
    for elements in zip(*lists):
        result.extend(elements)
    return result

def main():
    # Example usage:
    list1 = [1, 2, 3]
    list2 = [20, 30, 40]
    list3 = ['a', 'b', 'c']
    print(interleave(list1, list2, list3))  # Expected output: [1, 20, 'a', 2, 30, 'b', 3, 40, 'c']

    list4 = [True, False, True]
    list5 = [0, 1, 0]
    print(interleave(list1, list4, list5)) # Expected output: [1, True, 0, 2, False, 1, 3, True, 0]

    list6 = [10, 20]
    list7 = [30, 40]
    print(interleave(list6, list7)) # Expected output: [10, 30, 20, 40]
    print(interleave([1,2],[3,4],[5,6],[7,8])) # Expected output: [1, 3, 5, 7, 2, 4, 6, 8]
    print(interleave()) # Expected Output: []

if __name__ == "__main__":
    main()