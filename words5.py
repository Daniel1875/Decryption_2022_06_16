with open("words5.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

# mvdse
checked = []
for word in lines:
    check = True
    if word[0] != 'a':
        check = False
    if word[4] != 't':
        check = False
    # p, r, c, i, e
    if 'p' in word:
        check = False
    if 'r' in word:
        check = False
    if 'c' in word:
        check = False
    if 'i' in word:
        check = False
    if 'e' in word:
        check = False
    s = set(word)
    if len(s) != 5:
        check = False
    if check:
        checked.append(word)

print(checked)