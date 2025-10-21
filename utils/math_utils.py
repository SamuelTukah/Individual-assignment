"""Math utilities: factorial, gcd, fibonacci."""

from math import prod
from typing import List

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def fibonacci(n: int) -> List[int]:
    """Return first n fibonacci numbers (n>=0)."""
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
