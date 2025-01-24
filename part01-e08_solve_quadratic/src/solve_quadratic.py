#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
  """
  Solves a quadratic equation of the form ax^2 + bx + c = 0.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A tuple containing the two solutions of the quadratic equation.
  """
  delta = b**2 - 4*a*c
  if delta < 0:
    return None  # Or raise an exception, depending on desired behavior
  x1 = (-b + math.sqrt(delta)) / (2*a)
  x2 = (-b - math.sqrt(delta)) / (2*a)
  return (x1, x2)


if __name__ == "__main__":
    main()



 

