# q3a
"""Q3a: map, filter, reduce example with numbers list."""

from functools import reduce

numbers = [2, 5, 8, 11, 14, 17, 20]

#map to square each number
squares = list(map(lambda x: x*x, numbers))

#filter to select only squares > 100
big_squares = list(filter(lambda s: s > 100, squares))

#reduce to compute sum of remaining numbers
sum_big_squares = reduce(lambda a,b: a+b, big_squares, 0)

if __name__ == "__main__":
    print("Numbers:", numbers)
    print("Squares:", squares)
    print("Squares > 100:", big_squares)
    print("Sum of squares > 100:", sum_big_squares)
