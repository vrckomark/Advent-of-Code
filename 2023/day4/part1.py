sum=0

with open("input.txt","r") as f:
    for line in f.readlines():
        line=line[line.index(":")+1:].strip("\n").split("|")
        winning_numbers = [int(i) for i in list(filter(len,line[0].split(" ")))]
        my_numbers =[int(i) for i in list(filter(len,line[1].split(" ")))]

        correct_guesses = list(set(winning_numbers) & set(my_numbers))
        if len(correct_guesses):
            sum+=2**(len(correct_guesses)-1)
    

print(sum)
