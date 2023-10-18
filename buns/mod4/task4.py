def IsPalindromePossible(str):
    if len(set(str)) == len(str) // 2 or len(set(str)) == len(str) // 2 + 1:
        return True
    else:
        return False
def create_palindrome(str):
    if IsPalindromePossible(str):
        letter_count = {}
        palindrome = []
        for letter in str:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        middle_letter = ''
        for letter, count in letter_count.items():
            if count % 2 != 0:
                middle_letter = letter
            palindrome.extend([letter] * (count // 2))
        palindrome = palindrome + [middle_letter] + list(palindrome[::-1])
        return ''.join(palindrome)
    else:
        return "Невозможно"

str = input()
if IsPalindromePossible(str):
    palindrome = create_palindrome(str)
    print(palindrome)
else:
    print("Невозможно")
