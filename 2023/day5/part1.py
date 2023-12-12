from time import perf_counter

start = perf_counter()

seeds=[]
maps=[]
with open("input.txt","r") as f:
    current_map=[]
    lines = f.readlines()
    for i,line in enumerate(lines):
        if "seeds" in line:
            seeds=[int(i) for i in list(filter(None, line.strip("\n").split(":")[1].split(" ")))]
        if line[0].isnumeric():
            current_row=[int(i) for i in line.strip("\n").split(" ")]
            current_map.append(current_row)
        if line=="\n" or i==len(lines)-1:
            maps.append(current_map)
            current_map=[]

locations=[]


for seed in seeds:
    destination=seed
    for map_ in maps:
        source=destination
        for row in map_:
            destination_min=row[0]
            source_min = row[1]
            map_range=row[2]
            if source >= source_min and source < source_min+map_range:
                destination = source - source_min + destination_min
                break
            else:
                destination=source
    locations.append(destination)

print(locations)

print(f"MIN:\n\n{min(locations)}")


end = perf_counter()


print(f"{round(((end-start)*1000),2)}ms")

