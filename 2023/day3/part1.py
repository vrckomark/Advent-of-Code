grid=[]
with open("input.txt","r") as f:
    for line in f.readlines():
        line=line.strip("\n")
        row = []
        for char in line:
            row.append(char)
        row.append(".")
        row.insert(0,".")
        grid.append(row)

blank_row = ["." for _ in range(142)]
grid.insert(0,blank_row)
grid.append(blank_row)

sum=0
for i,row in enumerate(grid):
    number=""
    for j,cell in enumerate(row):
        if cell.isnumeric():
            number+=cell
        if len(number)>0 and not cell.isnumeric():
            span = len(number)
            adjacent_chars = [
                row[j-(span+1)],
                cell,
                *grid[i-1][j-(span+1):j+1],
                *grid[i+1][j-(span+1):j+1],
            ]
            for char in adjacent_chars:
                if char!=".":
                    sum+=int(number)
            number=""
print(sum)