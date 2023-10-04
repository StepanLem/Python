input_string = input()
s = ""
i = ""
space_count = 0
for k in range(0, len(input_string)):
  if input_string[k] != "," and space_count == 0:
    s += input_string[k]
  elif input_string[k] != "," and space_count == 1:
    i += input_string[k]
  else:
    space_count += 1
count = 0
for j in s:
    if j == i:
        count += 1
    else:
        print(count)
        break
