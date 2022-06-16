text1 = "xmenjxmefagfgudemvdseusxvjzgjwSmefdugadxfsemefdwgdzmckdzfenxgfefgmvdsesupjzgemuptuklfccfmxtmscenszgedu"
text2 = "gezjukemjumpjupztejgjchwstigfmajdsefzmaetajazjmejmxjemfndzytgsmctxmkjdzujxdutaxmbjaduvjaetdugymzqqdszfzmaetajfzdvcjxg"


quadgrams = {}

for i in range(len(text1) - 3):
    sub = text1[i:i+4]
    if sub in quadgrams:
        quadgrams[sub] = quadgrams[sub] + 1
    else:
        quadgrams[sub] = 1

for i in range(len(text2) - 3):
    sub = text2[i:i+4]
    if sub in quadgrams:
        quadgrams[sub] = quadgrams[sub] + 1
    else:
        quadgrams[sub] = 1

sort_orders = sorted(quadgrams.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
    if i[1] > 1:
        print(i[0], i[1])
