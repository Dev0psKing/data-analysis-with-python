#!/usr/bin/env python3

import math

def rectangle_area(length, base):
    return length * base

def triangle_area(length, base):
    return 0.5 * base * length

def circle_area(radius):
    return math.pi * radius ** 2

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle, or press Enter to quit): ").strip().lower()

        # Exit if the input is empty
        if not shape:
            break

        # Handle invalid shapes
        if shape not in ["triangle", "rectangle", "circle"]:
            print("Unknown shape!")
            continue

        try:
            # Handle specific shape calculations
            if shape == "circle":
                radius = float(input("Enter the radius: "))
                print(f"The area is {circle_area(radius):.6f}")
            else:
                base = float(input("Enter the base: "))
                length = float(input("Enter the height: "))
                if shape == "triangle":
                    print(f"The area is {triangle_area(length, base):.6f}")
                elif shape == "rectangle":
                    print(f"The area is {rectangle_area(length, base):.6f}")
        except ValueError:
            print("Invalid input!")
            continue

if __name__ == "__main__":
    main()



