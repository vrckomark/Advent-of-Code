from re import sub
from re import split

max_cubes = {
    "red":12,
    "green":13,
    "blue":14
}

sum=0

with open("input.txt","r") as f:
    for line in f.readlines():
        game_id= int(sub(r"\D", "",line.split(":")[0]))
        draws = line.split(":")[1].replace(";",",").split(",")
        possible=True
        for draw in draws:
            drawList = draw[1:].strip("\n").split(" ")
            if int(drawList[0]) > max_cubes[drawList[1]]:
                possible=False
        if possible:
            sum+=game_id
print(sum)