input_file = open("input.txt")
n = int(input_file.readline())
current_step = 1
x = 0
y = 0
current_count_steps = 0
while n > 0:
    if current_count_steps % 4 == 0:
        if (n >= current_step):
            x -= current_step
            n -= current_step
            current_count_steps += 1
        else:
            x -= n
            break
    elif current_count_steps % 4 == 1:
        if (n >= current_step):
            y -= current_step
            n -= current_step
            current_count_steps += 1
        else:
            y -= n
            break
    elif current_count_steps % 4 == 2:
        current_step += 1
        if (n >= current_step):
            x += current_step
            n -= current_step
            current_count_steps += 1
        else:
            x += n
            break
    elif current_count_steps % 4 == 3:
        if (n >= current_step):
            y += current_step
            n -= current_step
            current_step += 1
            current_count_steps += 1
        else:
            y += n
            break
with open("output.txt", "a") as output_file:
    output_file.write(f"{x} {y}")
