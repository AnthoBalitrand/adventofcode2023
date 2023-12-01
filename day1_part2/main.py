class Found(Exception): pass

with open('input.txt', 'r') as f: 
    res = 0
    lines = f.readlines()
    str_to_int_map = {
            'one': '1', 
            'two': '2', 
            'three': '3', 
            'four': '4', 
            'five': '5', 
            'six': '6', 
            'seven': '7', 
            'eight': '8', 
            'nine': '9'
            }

    for l in lines:
        c = ""
        for r in [range(len(l)), reversed(range(len(l)))]:
            try:
                for a in r:
                    if l[a].isnumeric():
                        c += l[a]
                        raise Found
                    else:
                        for k, v in str_to_int_map.items():
                            if l[a:a+len(k)] == k:
                                c += v
                                raise Found
            except Found:
                pass
        res += int(c)

print(res)
