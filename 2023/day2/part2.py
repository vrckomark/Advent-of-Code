from re import sub
from re import split


sum=0

with open("input.txt","r") as f:
    for line in f.readlines():
        game_id= int(sub(r"\D", "",line.split(":")[0]))
        draws = line.split(":")[1].replace(";",",").strip("\n").split(",")
        
        highestRed=1
        highestGreen=1
        highestBlue = 1
        for draw in draws:
            hand = draw[1:].split(" ")
            if hand[1]=="red" and int(hand[0])>highestRed:
                highestRed = int(hand[0])
            if hand[1]=="green" and int(hand[0])>highestGreen:
                highestGreen = int(hand[0])
            if hand[1]=="blue" and int(hand[0])>highestBlue:
                highestBlue = int(hand[0])
        sum+= highestRed*highestGreen*highestBlue


print(sum)


        # min_draws = [ {"color":None,"value":None}]
        
        # for i,draw in enumerate(draws):
        #     drawList = draw[1:].split(" ")
        #     current_obj ={"color":drawList[1],"min_value":int(drawList[0])}
        #     print(draws)
        #     if i==0:
        #         min_draws[0]=current_obj
        #     colorChecked=False
        #     for j,min_draw in enumerate(min_draws):
                # if min_draw["color"]
                # if not min_draw["color"]:
                #     min_draws.append(current_obj)
                #     continue
                # if min_draw["color"]==current_obj["color"] and current_obj["min_value"]<min_draw["min_value"]:
                #     min_draws[j]["min_value"]=current_obj["min_value"]
                #     continue