
"""String utility module."""

def count_vowels(text: str) -> int:
    """Return the count of vowels in text (case-insensitive)."""
    vowels = set("aeiou")
    text = text.lower()
    return sum(1 for ch in text if ch in vowels)

def is_palindrome(text: str) -> bool:
    """Check if a text is palindrome ignoring spaces and punctuation."""
    # normalising tokeep letters/digits only, lowercase
    filtered = "".join(ch.lower() for ch in text if ch.isalnum())
    return filtered == filtered[::-1]
