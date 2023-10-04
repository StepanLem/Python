consonant_letter = "бвгджзйклмнпрстфхцчшщ"
vowel_letter = "аеёиоуыэюя"
s = input()
vowel_count = 0
consonant_count = 0
for i in s:
    if i in vowel_letter:
        vowel_count += 1
    elif i in consonant_letter:
        consonant_count += 1
    else:
        continue
print(vowel_count, consonant_count)
