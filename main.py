working_array = [0,0,0,0,0,0,0,0]
cell_pos = 0

with open("main.bf", "r") as f:
    content = f.read()

for char in content:
    if char == "+":
        working_array[cell_pos] += 1
    elif char == ">":
        cell_pos += 1
        if cell_pos > 7:
            cell_pos = 0
    elif char == "<":
        cell_pos -= 1
        if cell_pos < 0:
            cell_pos = 7
    elif char == ".":
        print(chr(working_array[cell_pos]), end="")
    elif char == ",":
        x = input()
        x = ord(x)
        working_array[cell_pos] = x
        del x
