sum=0
cards:list

with open("input.txt","r") as f:
    cards = [1 for _ in range(len(f.readlines()))]

with open("input.txt","r") as f:
    for i,line in enumerate(f.readlines()):
        line=line[line.index(":")+1:].strip("\n").split("|")
        winning_numbers = [int(i) for i in list(filter(len,line[0].split(" ")))]
        my_numbers =[int(i) for i in list(filter(len,line[1].split(" ")))]

        correct_guesses = len(list(set(winning_numbers) & set(my_numbers)))

        for index in range(correct_guesses):
            try:
                cards[i+index+1]+=cards[i]
            except:
                break
                

for card in cards:
    sum+=card

print(sum)
