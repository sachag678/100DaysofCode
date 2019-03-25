import numpy as np

tie = 0
win = 0
loss = 0

actions = ['R', 'P', 'S']

opp = [0.4, 0.3, 0.3]
pla = [0, 1, 0]
games = 100000
for i in range(games):
    opp_choice = np.random.choice(actions, p = opp)
    my_choice = np.random.choice(actions, p = pla)

    if opp_choice == my_choice:
        tie+=1

    if opp_choice == 'R':
        if my_choice == 'P':
            win +=1
        if my_choice == 'S':
            loss+=1
    if opp_choice == 'P':
        if my_choice == 'R':
            loss +=1
        if my_choice == 'S':
            win+=1
    if opp_choice == 'S':
        if my_choice == 'R':
            win +=1
        if my_choice == 'P':
            loss+=1

print('Wins {}, Loss {}, Ties {}'.format(win/games, loss/games, tie/games))
