import time
start_time = time.time()

with open('input.txt', 'r') as f:
    # initialize a list of numbers, each number being the number of the corresponding card in the position
    cards_list = [1 for x in f.readlines()]
    # moving back cursor the the beginning of the file
    f.seek(0)

    current_card = 0
    for card in f.readlines():
        num = card.split(':')[1]
        my_num, win_num = num.split('|')
        my_num = set(my_num.split())
        win_num = set(win_num.split())
        card_res = 0
        print(f"Card {card} winning numbers: {my_num.intersection(win_num)}")
        # iterate the number of times the current card exists (multiple ones can have been won)
        won_points = len(my_num.intersection(win_num))
        if won_points:
            print(f"Has {won_points} win numbers and has {cards_list[current_card]} copies. Card id is {current_card}. Adding {cards_list[current_card]} points to the next {won_points} cards ({current_card + 1} to {current_card + won_points})")
        else:
            print(f"Has no win numbers and has {cards_list[current_card]} copies. Card id is {current_card}. Not adding points to next cards")
        for win in range(won_points):
            # make sure we are not trying to add copies of cards outside of the existing range of cards (len(cards_list))
            if current_card + win + 1 < len(cards_list):
                cards_list[current_card + 1 + win] += cards_list[current_card]
        current_card += 1

print("\n\n")
res = 0
# add the number of copies of each card we have to get the result
for c in cards_list:
    res += c
print(f"Result is {res}")

print("--- %s seconds ---" % (time.time() - start_time))