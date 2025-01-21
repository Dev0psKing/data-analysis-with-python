#!/usr/bin/env python3

# Function to triple a number
def triple(x):
    return x * 3

# Function to square a number
def square(x):
    return x ** 2

# Main function
def main():
    # Iterate through values 1 to 10
    for i in range(1, 11):
        t = triple(i)  # Call triple
        s = square(i)  # Call square
        if s > t:
            break  # Stop the loop if square > triple
        else:
            print(f"triple({i})=={t} square({i})=={s}")

# Entry point
if __name__ == "__main__":
    main()
