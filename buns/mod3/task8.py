phone_number = input()
cleaned_number = phone_number.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
print(cleaned_number)