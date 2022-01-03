import random
e = "Empty"
j = "Jail"
t = "Treasure"
h = "Hotel"

c_p = {1:e,2:e,3:j,4:h,5:e,6:t,7:j,8:t,9:e,10:e,11:h,12:j,13:t,14:h,15:e,
16:e,17:j,18:h,19:e,20:t,21:j,22:t,23:e,24:e,25:h,26:j,27:t,28:h,29:j,30:e,
31:e,32:j,33:h,34:e,35:t,36:j,37:t,38:e,39:e,40:h,41:j,42:t,43:e,44:h,45:e,
46:t,47:e,48:e,49:h,50:j,51:t,52:h,53:e,54:e,55:j,56:h,57:e,58:t,59:j,60:t,
61:e,62:e,63:h,64:j,65:t,66:h,67:j,68:e,69:e,70:j,71:h,72:e,73:t,74:j,75:t,
76:e,77:e,78:h,79:j,80:t,81:e,82:e,83:e,84:t,85:h,86:e,87:h,88:j,89:t,90:j,
91:e,92:e,93:j,94:h,95:e,96:t,97:j,98:e,99:t,100:e,101:j,102:h,103:e,104:t,105:j,106:t,
107:e,108:e,109:h,110:j,111:t,112:h,113:j,114:e,115:e,116:j,117:h,118:e,119:t,120:j}

l = {'point1':0,'point2':0,'point3':0}
players = {'player1':1000,'player2':1000,'player3':1000}
hotel_check = []
for H in c_p:
    if (c_p[H] == "Hotel"):
        hotel_check.append(H)
        
hotel_owner = {}
chances = 1
hotel_worth = 200
hotel_rent = 50
jail_fine = 150
treasure_value = 200
empty = 0

print("There are 3 players in this game and each player has money 1000 and 10 chances  :) ")
for i in range(1,11):
    dice = input("Player1's turn, chance no. " + str(chances)+ ", enter your chance no. : ")
    n = random.randint(2,12)
    l['point1'] += n
    if c_p[l['point1']] == "Hotel":
        if l['point1'] in hotel_check:
            players['player1'] -= hotel_worth
            hotel_owner.update({l['point1']:'player1'})
            hotel_check.remove(l['point1'])
        else:
            players['player1'] -= hotel_rent
            players[hotel_owner[l['point1']]] += hotel_rent
            print('Hotel owner',hotel_owner[l['point1']])
    elif c_p[l['point1']] == "Jail":
        players['player1'] -= jail_fine
    elif c_p[l['point1']] == "Treasure":
        players['player1'] += treasure_value
    else:
        players['player1'] += empty
    print(f"You get :- {n} points \nYour total points are :- {l['point1']}",
      "\n"f"And you get :- {c_p[l['point1']]} \nPlayer1 has {players['player1']} money remaining \n ")

    dice = input("Player2's turn, chance no. "+str(chances)+", enter your chance no. : ")
    n1 = random.randint(2,12)
    l['point2'] += n1
    if c_p[l['point2']] == "Hotel":
        if l['point2'] in hotel_check:
            players['player2'] -= hotel_worth
            hotel_owner.update({l['point2']:'player2'})
            hotel_check.remove(l['point2'])
        else:
            players['player2'] -= hotel_rent
            players[hotel_owner[l['point2']]] += hotel_rent
            print('Hotel owner',hotel_owner[l['point2']])
    elif c_p[l['point2']] == "Jail":
        players['player2'] -= jail_fine
    elif c_p[l['point2']] == "Treasure":
        players['player2'] += treasure_value
    else:
        players['player2'] += empty
    print(f"You get :- {n1} points \nYour total points are :- {l['point2']}",
      "\n"f"And you get :- {c_p[l['point2']]} \nPlayer2 has {players['player2']} money remaining \n")

    dice = input("Player3's turn, chance no. "+str(chances)+", enter your chance no. : ")
    n2 = random.randint(2,12)
    l['point3'] += n2
    if c_p[l['point3']] == "Hotel":
        if l['point3'] in hotel_check:
            players['player3'] -= hotel_worth
            hotel_owner.update({l['point3']:'player3'})
            hotel_check.remove(l['point3'])
        else:
            players['player3'] -= hotel_rent
            players[hotel_owner[l['point3']]] += hotel_rent
            print('Hotel owner',hotel_owner[l['point3']])
    elif c_p[l['point3']] == "Jail":
        players['player3'] -= jail_fine
    elif c_p[l['point3']] == "Treasure":
        players['player3'] += treasure_value
    else:
        players['player3'] += empty
    print(f"You get :- {n2} points \nYour total points are :- {l['point3']}",
      "\n"f"And you get :- {c_p[l['point3']]} \nPlayer3 has {players['player3']} money remaining \n \n")
    chances += 1



print(hotel_owner)
H_O_list = list(hotel_owner.values())
for x in players:
    y = H_O_list.count(x)
    players[x] += (hotel_worth*y)
    print(y)

print(H_O_list)
#print("*Total worth = money remaining at end + valur of all hotel bought by player*").
a = sorted(players.values())
b  = {}
for i in  range(len(a)):
    for j in players:
        if a[i] == players[j]:
            b.update({j:players[j]})
c = list(b.items())
c.reverse()
d = dict(c)
for i in d:
    print(i,"has total worth",d[i])