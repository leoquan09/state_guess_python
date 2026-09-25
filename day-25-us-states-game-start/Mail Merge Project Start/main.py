names = []
template = ""

with open('./input/names/invited_names.txt', 'r') as file:
    for line in file:
        clean_line = line.strip() 
        names.append(clean_line)

with open("./input/letters/starting_letter.txt") as file:
    template = file.read()

print(template)
for name in names:
    with open(f"./output/readyToSend/{name}.txt", "w") as file:
        file.write(template.replace("[name]", name))