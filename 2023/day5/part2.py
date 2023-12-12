from time import perf_counter

start = perf_counter()

seeds_ranges=[]
maps=[]
with open("input.txt","r") as f:
    current_map=[]
    seed_index=0
    lines = f.readlines()
    for i,line in enumerate(lines):
        if "seeds" in line:
            seeds=[int(i) for i in list(filter(None, line.strip("\n").split(":")[1].split(" ")))]
            for j,seed in enumerate(seeds):
                if j%2==0:
                    seeds_ranges.append({
                        "min":seed,
                        "max":seed
                    })
                else:
                    seeds_ranges[seed_index]["max"] = seeds_ranges[seed_index]["min"]+seed
                    seed_index+=1
        if line[0].isnumeric():
            current_row=[int(i) for i in line.strip("\n").split(" ")]
            current_map.append(current_row)
        if line=="\n" or i==len(lines)-1:
            maps.append(current_map)
            current_map=[]

locations=[]

print(seeds_ranges)



# print(f"MIN:\n\n{min(locations)}")


end = perf_counter()


print(f"{round(((end-start)*1000),2)}ms")

