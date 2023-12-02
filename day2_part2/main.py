with open('input.txt', 'r') as f:
    lines = f.readlines()
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
        g_power = 0
        for k, v in g_max.items():
            g_power = v if g_power == 0 else g_power * v
        res += g_power

print(res)
