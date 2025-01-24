#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    i = 0
    j = 0

    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1

    while i < len(L1):
        L.append(L1[i])
        i += 1
    while j < len(L2):
        L.append(L2[j])
        j += 1
    return L

def main():
  list1 = sorted([5, 2, 8, 1, 9])
  list2 = sorted([3, 7, 4, 6, 0])
  merged_list = merge(list1, list2)
  print("List 1:", list1)
  print("List 2:", list2)
  print("Merged List:", merged_list)


if __name__ == "__main__":
    main()