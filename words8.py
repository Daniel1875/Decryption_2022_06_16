with open("words8.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# fzmaetaj
# practice
checked = []
for word in lines:
    check = True
    if word[3] != word[6]:
        check = False
    s = set(word)
    if len(s) != 7:
        check = False
    if check:
        checked.append(word)

print(checked)
