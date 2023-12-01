with open('input.txt', 'r') as f: 
    res = 0
    lines = f.readlines()

    for l in lines:
        c = ""
        c += (x for x in l if x.isnumeric()).__next__()
        c += (y for y in l[::-1] if y.isnumeric()).__next__()
        res += int(c)
print(res)
