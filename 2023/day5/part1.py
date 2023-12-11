from time import perf_counter

seeds=[]
maps=[]
with open("input.txt","r") as f:
    current_map=[]

    start = perf_counter()
    for line in f.readlines():
        if "seeds" in line:
            seeds=[int(i) for i in list(filter(None, line.strip("\n").split(":")[1].split(" ")))]
        if line[0].isnumeric():
            current_row=[int(i) for i in line.strip("\n").split(" ")]
            current_map.append(current_row)
        if line=="\n":
            maps.append(current_map)
            current_map=[]



end = perf_counter()

print(f"{round(((end-start)*1000),2)}ms")
# for map_ in maps:
#     for row in map_:
#         print(row)
#     print("\n\n")