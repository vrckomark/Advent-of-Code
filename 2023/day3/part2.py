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

def getHorizontalAdjacentNumbers(row,index):
    if not row[index+1].isnumeric() and not row[index-1].isnumeric():
        return []
    adjacent_numbers=[]

    right_adjacent=row[index+1:index+4]
    left_adjacent=row[index-3:index]
    left_adjacent.reverse()

    number=""
    for char in left_adjacent:
        if char.isnumeric():
            number+=char
        if char==".":
            break
    if len(number)>0:
        adjacent_numbers.append(int(number[::-1]))
    number=""
    for char in right_adjacent:
        if char.isnumeric():
            number+=char
        if char==".":
            break
    if len(number)>0:
        adjacent_numbers.append(int(number))

    
    return adjacent_numbers

def getVerticalRow(wholeRow,index):
    row = wholeRow[index-3:index+4]
    numbers=[]
    number=""

    for i,char in enumerate(row):
        if char.isnumeric():
            number+=char
       
        if not char.isnumeric() and len(number)>0 or i==len(row)-1 and len(number)>0:
            
            span = len(number)
            number_indexes=[]
            for idx in range(span):
                if i==len(row)-1 and char.isnumeric():
                    number_indexes.append(i-span+idx+1)
                else:
                    number_indexes.append(i-span+idx)
            if len(list(set(number_indexes) & set([2,3,4])))>0:
                numbers.append(int(number))
            number=""

    return numbers


def getVerticalAdjacentNumbers(rows,index):
    return [
        *getVerticalRow(rows[0],index),
        *getVerticalRow(rows[1],index)
    ]    



sum=0
for i,row in enumerate(grid):
    for j,cell in enumerate(row):
        if cell=="*":
            horizontal =getHorizontalAdjacentNumbers(row,j)
            vertical=getVerticalAdjacentNumbers([grid[i-1],grid[i+1]],j)
            adjacent_numbers=[
                *horizontal,
                *vertical
            ]
            # print(grid[i-1][j-3:j+4])
            # print(row[j-3:j+4])
            # print(grid[i+1][j-3:j+4])
            # print(adjacent_numbers)
            if len(adjacent_numbers)==2:
                sum+=adjacent_numbers[0]*adjacent_numbers[1]



print(sum)