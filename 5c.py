text1 = "xmenjxmefagfgudemvdseusxvjzgjwSmefdugadxfsemefdwgdzmckdzfenxgfefgmvdsesupjzgemuptuklfccfmxtmscenszgedu"
text2 = "gezjukemjumpjupztejgjchwstigfmajdsefzmaetajazjmejmxjemfndzytgsmctxmkjdzujxdutaxmbjaduvjaetdugymzqqdszfzmaetajfzdvcjxg"


c5 = {}

for i in range(len(text1) - 4):
    sub = text1[i:i+5]
    if sub in c5:
        c5[sub] = c5[sub] + 1
    else:
        c5[sub] = 1

for i in range(len(text2) - 4):
    sub = text2[i:i+5]
    if sub in c5:
        c5[sub] = c5[sub] + 1
    else:
        c5[sub] = 1

sort_orders = sorted(c5.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
    if i[1] > 1:
        print(i[0], i[1])
