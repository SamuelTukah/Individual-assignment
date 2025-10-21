"""Demo that uses string_tools module to accept user input and print results."""
from string_tools import count_vowels, is_palindrome

def main():
    text = input("Enter some text: ")
    vowels = count_vowels(text)
    palindrome = is_palindrome(text)
    print(f"Number of vowels: {vowels}")
    print(f"Is palindrome: {palindrome}")

if __name__ == "__main__":
    main()
