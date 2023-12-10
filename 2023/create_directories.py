import os

for i in range(3,30):
    name = f"day{i}"
    os.makedirs(name)
    path = os.path.join(name,"input.txt")
    with open(path,"x") as f:
        print()
    path = os.path.join(name,"part1.py")
    with open(path,"x") as f:
        print()
    path = os.path.join(name,"part2.py")
    with open(path,"x") as f:
        print()