e = "empty"
j = "jail"
t = "treasure"
h = "hotel"
c_p = {1:e,2:e,3:j,4:h,5:e,6:t,7:j,8:t,9:e,10:e,11:h,12:j,13:t,14:h,15:e,16:e,17:j,18:h,19:e,20:t,21:j,22:t,
23:e,24:e,25:h,26:j,27:t,28:h,29:j,30:e,31:e,32:j,33:h,34:e,35:t,36:j,37:t,38:e,39:e,40:h,41:j,42:t,43:e,44:h,45:e}

D_O = {1:4,2:4,3:4,4:6,5:7,6:8,7:5,8:11,9:10,10:12,11:2,12:3,13:5,14:6,15:7,
16:8,17:5,18:11,19:10,20:12,21:2,22:3,23:5,24:6,25:7,26:8,27:5,28:11,29:10,30:12}
l = {'point1':0,'point2':0,'point3':0}
players = {'player1':1000,'player2':1000,'player3':1000}
hotel_check = [4,11,14,18,25,28,33,40,44]
hotel_owner = {}
p = 1
chances = 1

hotel_worth = 200
hotel_rent = 50
jail_fine = 150
treasure_value = 200

print("All 3 players have 6 chances   :) ")
for i in range(1,7):
    dice = input("Player1's turn, chance no " + str(chances)+ ", enter your chance no. : ")
    l['point1'] += D_O[p]
    print("Your got "+str(D_O[p])+" points, and your total points are ",l['point1'])
    if c_p[l['point1']] == "hotel":
        print("c_p",c_p[l['point1']])
        if l['point1'] in hotel_check:
            print("You buy :",c_p[l['point1']])
            players['player1'] -= 200
            hotel_owner.update({l['point1']:'player1'})
            hotel_check.remove(l['point1'])
        else:
            players['player1'] -= 50
            players[hotel_owner[l['point1']]] += 50
            print('hotel owner',hotel_owner[l['point1']])
    elif c_p[l['point1']] == "jail":
        print("you got",c_p[l['point1']])
        players['player1'] -= jail_fine
    elif c_p[l['point1']] == "treasure":
        print("you got",c_p[l['point1']])
        players['player1'] += treasure_value
    else:
        print("you got",c_p[l['point1']])
        players['player1'] += 0
    print("player1 has money ",players['player1'])
    p += 1

    dice = input("Player2's turn, chance no. "+str(chances)+", enter your chance no. : ")
    l['point2'] += D_O[p]
    print("Your got "+str(D_O[p])+" points, and your total points are ", l['point2'])
    if c_p[l['point2']] == "hotel":
        print("c_p",c_p[l['point2']])
        if l['point2'] in hotel_check:
            print("You buy :",c_p[l['point2']])
            players['player2'] -= 200
            hotel_owner.update({l['point2']:'player2'})
            hotel_check.remove(l['point2'])
        else:
            players['player2'] -= 50
            players[hotel_owner[l['point2']]] += 50
            print('hotel owner',hotel_owner[l['point2']])
    elif c_p[l['point2']] == "jail":
        print("you got",c_p[l['point2']])
        players['player2'] -= jail_fine
    elif c_p[l['point2']] == "treasure":
        print("you got",c_p[l['point2']])
        players['player2'] += treasure_value
    else:
        print("you got",c_p[l['point2']])
        players['player2'] += 0
    print("player2 has money ",players['player2'])
    p += 1


    dice = input("Player3's turn, chance no. "+str(chances)+", enter  your chance no. : ")
    l['point3'] += D_O[p]
    print("Your got "+str(D_O[p])+" points, and your total points are ", l['point3'])
    if c_p[l['point3']] == "hotel":
        print("c_p",c_p[l['point3']])
        if l['point3'] in hotel_check:
            print("You buy :",c_p[l['point3']])
            players['player3'] -= 200
            hotel_owner.update({l['point3']:'player3'})
            hotel_check.remove(l['point3'])
        else:
            players['player3'] -= 50
            players[hotel_owner[l['point3']]] += 50
            print('hotel owner',hotel_owner[l['point3']])
    elif c_p[l['point3']] == "jail":
        print("you got",c_p[l['point3']])
        players['player3'] -= jail_fine
    elif c_p[l['point3']] == "treasure":
        print("you got",c_p[l['point3']])
        players['player3'] += treasure_value
    else:
        print("you got",c_p[l['point3']])
        players['player3'] += 0
    print("player3 has money ",players['player3'])
    p += 1
    chances += 1

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
