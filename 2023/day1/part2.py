sum:int=0

alphanumericNumbers=["one","two","three","four","five","six","seven","eight","nine"]

def find(string, char):
    return [i for i in range(len(string)) if string.startswith(char, i)]


with open("input.txt","r") as f:
    for line in f.readlines():
        indexes=[]
        for i,number in enumerate(alphanumericNumbers):
            if number in line:
                for occurrence in find(line,number):
                    indexes.append({"index": occurrence, "value": i+1})

        for i,char in enumerate(line):
            if char.isnumeric():
                indexes.append({"index": i, "value": int(char)}) 

        sortedIndexes = sorted(indexes, key=lambda d: d['index'])
        first_number = str(sortedIndexes[0]["value"])
        last_number = str(sortedIndexes[len(sortedIndexes)-1]["value"])
        sum+=int(f"{first_number}{last_number}")

print(sum)

