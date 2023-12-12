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

locations=[]

# for seed in seeds:
#     seed_result=seed
#     for map_ in maps:
#         current_src=seed_result
#         for row in map_:
#             dst_min=row[0]
#             src_min = row[1]
#             map_range=row[2]
#             if current_src<src_min:
#                 continue
#             if current_src <= (current_src+map_range) and current_src>=src_min:
#                 seed_result= dst_min+ current_src-src_min
#     locations.append(seed_result)

# print(f"MIN:\n\n{min(locations)}")

for i in maps:
    for row in i:
        print(i)

end = perf_counter()

print(f"{round(((end-start)*1000),2)}ms")
# for map_ in maps:
#     for row in map_:
#         print(row)
#     print("\n\n")