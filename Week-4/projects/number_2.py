def is_palindrome():
    word = input("Enter the word: ")
    return bool(word == word[::-1])

print(is_palindrome())
