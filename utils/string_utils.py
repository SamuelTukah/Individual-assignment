"""String utilities: count_vowels, reverse_string."""

def count_vowels(text: str) -> int:
    return sum(1 for ch in text.lower() if ch in "aeiou")

def reverse_string(text: str) -> str:
    return text[::-1]
