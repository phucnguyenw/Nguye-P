map={
    "size_x":5,
    "size_y":5


}

player={"x":2, "y":4}

boxes=[
    {"x":1,"y":1},
    {"x":2,"y":2},
    {"x":3,"y":3},
]

destion=[
    {"x":2,"y":1},
    {"x":3,"y":2},
    {"x":4,"y":3},


]



playing=True

while playing:
    



    for y in range (map["size_y"]):
        for x in range(map["size_x"]):
            destio_is_here=False
            player_is_here=False
            box_is_here=False
            for box in boxes:
                if box['x']== x and box['y']==y:
                    box_is_here=True
            
            if x==player['x'] and y ==player['y']:
                player_is_here=True
            for des in destion:
                if x==des['x'] and des['y'] == y:
                    destio_is_here=True
            if player_is_here==True:
                print("P ",end="")
            elif box_is_here==True:
                print("B ",end="")
            elif destio_is_here==True:
                print("D ",end="")    
            else:
                print("- ",end="")




            
            
        print()
    win=True
        

    for box in boxes:
        if box not in destion:
            win=False
    
    if win==True:
        print('You win!!')
        break
    move= input("Your move: ").lower()
    dx=0
    dy=0


    if move== 'w':
        dy=-1
    elif move=='s':
        dy=1
    
    elif move=='a':
        dx=-1
        
    elif move=='d':
        dx=1
    else:
        print("Ezzzzz")
        playing=False
    if 0<=player['x']+dx<=4 and 0<=player['y']+dy<=4:
        player['x']+=dx
        player['y']+=dy
    for box in boxes:
        if box['x']==player['x']and box['y']==player['y']:
            box['x']+=dx
            box['y']+=dy
    for box in boxes:
        
    for obs in obstacle:
         if obs['x'] == box['x'] and obs['y'] == box['y']:
            obs['x'] -= dx
            obs['y'] -= dy
             print("Oops, Obstacle")

        

  
