with open("input/day_02.txt","r") as f:
    data = f.read()

#parse data
data = data.split("\n")
games={}
for d in data:
    id = d.split(" ")[1][:-1] #Remove the "Game" and :
    play = d.split(": ")[1] #Split the data to a game

    sets = play.split("; ")#Split the data into sets of a game
    r,g,b=0,0,0 #set max value of spotted color in a game
    for set in sets:
        draws = set.split(", ")
        for draw in draws:
            if "red" in draw:
                r=max(int(draw.split(" ")[0]),r)
            elif "green" in draw:
                g=max(int(draw.split(" ")[0]),g)
            elif "blue" in draw:
                b=max(int(draw.split(" ")[0]),b)
        
    games[id] = {"red":r,"green":g,"blue":b}

r_lim, g_lim, b_lim = 12,13,14

sum_games =0
for k,v in games.items():
    if games[k]["red"]<=r_lim and games[k]["green"]<=g_lim and games[k]["blue"]<=b_lim:
        #print(game)
        sum_games+= int(k)

print(sum_games)

#Part II
sum_power = 0
for k,v in games.items():
    power = games[k]["red"]*games[k]["green"]*games[k]["blue"]