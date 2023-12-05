import time
start_time = time.time()

with open('input.txt', 'r') as f:
    res = 0
    for card in f.readlines():
        num = card.split(':')[1]
        my_num, win_num = num.split('|')
        my_num = set(my_num.split())
        win_num = set(win_num.split())
        card_res = 0
        for win in range(len(my_num.intersection(win_num))):
            if card_res == 0:
                card_res = 1
            else:
                card_res *=2
        res += card_res
print(f"Result is {res}")

print("--- %s seconds ---" % (time.time() - start_time))
