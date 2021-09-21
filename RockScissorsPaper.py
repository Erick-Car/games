import random

should_countinue = True
# нужно ли продолжать игру)
while should_countinue:
    player_choice = input("Player choice: [R/S/P]").lower()
# некорректный ввод
    if player_choice not in ['r', 's', 'p']:
        print('Incorrect input. Try again')
        continue
# словарик со случайным ответом
    gen = {1: 'r', 2: 's', 3: 'p'}
    comp_choice = random.choice(['r', 's', 'p'])

    print(f'Comp choice = {comp_choice}')
# кто победил
    winning_combination = [('p', 'r'), ('r', 's'), ('s', 'p')]
#
    if player_choice == comp_choice:
        print("A draw")
    elif (player_choice, comp_choice) in winning_combination:
        print('Player wins')
    else:
        print('Comp wins')
# если ввели y should_continue = true
    should_countinue = input('Want to proceed? [y/n]').lower() == 'y'