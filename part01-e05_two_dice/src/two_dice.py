#!/usr/bin/env python3

def main():
   
    for i in range(1, 7):  # Values for the first die (1 to 6)
        for j in range(1, 7):  # Values for the second die (1 to 6)
            if i + j == 5:
                print(f"({i},{j})")  # Removed the space before the comma

if __name__ == "__main__":
    main()