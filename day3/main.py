with open('input.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    input_array = list()
    # as input is not that big, import it as a two-dimensional array to work on it
    # bigger input would have to be managed differently 
    for l in lines:
        input_array.append(l.strip())

    for input_y in range(len(input_array)):
        curr_part_id = ""
        curr_part_id_valid = False
        for input_x in range(len(input_array[input_y])):
            if (curr_val := input_array[input_y][input_x]).isnumeric():
                curr_part_id += curr_val
                min_offset_y = -1 if input_y > 0 else 0
                max_offset_y = 1 if input_y < len(input_array) else 0
                for offset_y in range(min_offset_y, max_offset_y + 1):
                    min_offset_x = -1 if input_x > 0 else 0
                    max_offset_x = 1 if input_x < len(input_array[input_x]) else 0
                    for offset_x in range(min_offset_x, max_offset_x + 1):
                        if offset_x == 0 and offset_y == 0:
                            continue
                        try:
                            offset_val = input_array[input_y + offset_y][input_x + offset_x]
                            if not offset_val.isnumeric() and offset_val != '.':
                                curr_part_id_valid = True
                        except IndexError:
                            pass
            end_of_line = input_x + 1 == len(input_array[input_y])
            if not curr_val.isnumeric() or end_of_line:
                if curr_part_id_valid and (not curr_val.isnumeric() or end_of_line):
                    print(f"{curr_part_id} is valid")
                    res += int(curr_part_id)
                    curr_part_id = ""
                    curr_part_id_valid = False
                elif not curr_val.isnumeric() and curr_part_id:
                    print(f"{curr_part_id} is not valid")
                    curr_part_id = ""
print(f"Result is {res}")
