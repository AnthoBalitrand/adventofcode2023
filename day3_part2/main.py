with open('input.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    input_array = list()
    # as input is not that big, import it as a two-dimensional array to work on it
    # bigger input would have to be managed differently 
    for l in lines:
        input_array.append(l.strip())

    gears = dict()

    for input_y in range(len(input_array)):
        curr_part_id = ""
        curr_part_id_valid = False
        curr_part_adj_gear = list()
        for input_x in range(len(input_array[input_y])):
            if (curr_val := input_array[input_y][input_x]).isnumeric():
                curr_part_id += curr_val
                # making sure that we are not trying to test adjacent values outside of the array limits
                min_offset_y = -1 if input_y > 0 else 0
                max_offset_y = 1 if input_y < len(input_array) else 0
                for offset_y in range(min_offset_y, max_offset_y + 1):
                    # making sure that we are not trying to test adjacent values outside of the array limits
                    min_offset_x = -1 if input_x > 0 else 0
                    max_offset_x = 1 if input_x < len(input_array[input_x]) else 0
                    for offset_x in range(min_offset_x, max_offset_x + 1):
                        if offset_x == 0 and offset_y == 0:
                            continue
                        try:
                            offset_val = input_array[input_y + offset_y][input_x + offset_x]
                            if not offset_val.isnumeric() and offset_val != '.':
                                curr_part_id_valid = True
                                if offset_val == "*":
                                    # found a gear, storing its location as a tuple on a list 
                                    # (some parts could be adjacent to multiple gears)
                                    if not ((input_y + offset_y, input_x + offset_x)) in curr_part_adj_gear:
                                        curr_part_adj_gear.append((input_y + offset_y, input_x + offset_x))
                        except IndexError:
                            pass
            end_of_line = input_x + 1 == len(input_array[input_y])
            if not curr_val.isnumeric() or end_of_line:
                if curr_part_id_valid and (not curr_val.isnumeric() or end_of_line):
                    print(f"{curr_part_id} is valid")
                    curr_part_id_valid = False
                    # on our dict of gears, each time a part is found adjacent to a gear, add it to the corresponding list of values
                    for gear in curr_part_adj_gear:
                        if not gear in gears:
                            gears[gear] = [curr_part_id]
                        else:
                            gears[gear].append(curr_part_id)
                        print(f"{curr_part_id} is adjacent to gear at {gear}")
                elif not curr_val.isnumeric() and curr_part_id:
                    print(f"{curr_part_id} is not valid")
                curr_part_id = ""
                # reinitializing the adjacent gears list before moving the next part number
                curr_part_adj_gear = list()

# for each gear having exactly 2 adjacent parts, calculate the ratio and add it to the result
for gear, values in gears.items():
    if len(values) == 2:
        res += int(values[0]) * int(values[1])

print(f"Result is {res}")
