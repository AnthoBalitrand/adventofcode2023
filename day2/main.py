class BadGame(Exception): pass

with open('input.txt', 'r') as f:
    lines = f.readlines()
    target = {'red': 12, 'green': 13, 'blue': 14}
    res = 0

    for game in lines:
        game_n, results = game.split(':')
        g_max = dict()
        g_id = int(game_n.split()[1])
       
        for game_res in results.split(';'):
            for color_count in game_res.split(','):
                num, color = color_count.split()
                if color not in g_max:
                    g_max[color] = int(num)
                else:
                    if int(num) > g_max[color]:
                        g_max[color] = int(num)
        try:
            for k, v in target.items():
                if g_max.get(k, 0) > target[k]:
                    raise BadGame
            print(f"{game} is OK")
            res += g_id
        except BadGame:
            pass

print(res)
