sum:int=0

with open("input.txt","r") as f:
    for line in f.readlines():
        numbers=[]
        for char in line:
            if char.isnumeric():
                numbers.append(int(char))
        sum+=int(f"{numbers[0]}{numbers[len(numbers)-1]}")

print(sum)
