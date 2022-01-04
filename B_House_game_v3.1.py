import random

rules = {'e':"Empty",'j' :"Jail",'t':"Treasure",'h' : "Hotel"}
c_p = ['e','e','e','j','h','e','t','j','t','e','e','h','j','t','h','e','e','j','h','e','t','j','t','e','e','h','j','t','h','j','e','e','j',
'h','e','t','j','t','e','e','h','j','t','e','h','e','t','e','e','h','j','t','h','e','e','j','h','e','t','j','t','e','e','h','j','t','h','j',
'e','e','j','h','e','t','j','t','e','e','h','j','t','e','e','e','t','h','e','h','j','t','j','e','e','j','h','e','t','j','e','t','e']
points = {1:0,2:0,3:0}
players = {'player1':1000,'player2':1000,'player3':1000}
r = {'hotel_owner':{},'chances':1,'hotel_worth':200,'hotel_rent':50,'jail_fine':150,'treasure_value':200,'hotel_check': [H for H in range(len(c_p)) if (rules[c_p[H]]== "Hotel")]}
print("There are 3 players in this game, each player has money 1000 and 10 chances  :) ")
for i in range(1,11):
    m = 1
    for j in players:
        dice = input(f"{j} turn, chance no. {r['chances']} enter your chance no. : ")
        n = random.randint(2,12)
        points[m] += n
        if rules[c_p[points[m]]] == "Hotel":
            if points[m] in r['hotel_check']:
                players[j] -= r['hotel_worth']
                r['hotel_owner'].update({points[m]:j})
                r['hotel_check'].remove(points[m])
            else:
                players[j] -= r['hotel_rent']
                players[r['hotel_owner'][points[m]]] += r['hotel_rent']
        elif rules[c_p[points[m]]] == "Jail":
            players[j] -= r['jail_fine']
        elif rules[c_p[points[m]]] == "Treasure":
            players[j] += r['treasure_value']
        print(f"You get :- {n} points \nYour total points are :- {points[m]}","\n"f"And you get :- {rules[c_p[points[m]]]} \n{j} has {players[j]} money remaining \n ")
        m += 1
    r['chances'] += 1
H_O_list = list(r['hotel_owner'].values())
for x in players:
    y = H_O_list.count(x)
    players[x] += (r['hotel_worth']*y)
d  = sorted(players.items(), key=lambda x:x[1])
d.reverse()
p_dict = dict(d)
for i in p_dict:
    print(i,'has total worth rs',p_dict[i])