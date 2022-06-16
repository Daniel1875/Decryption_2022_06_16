text1 = "xmenjxmefagfgudemvdseusxvjzgjwSmefdugadxfsemefdwgdzmckdzfenxgfefgmvdsesupjzgemuptuklfccfmxtmscenszgedu"
text2 = "gezjukemjumpjupztejgjchwstigfmajdsefzmaetajazjmejmxjemfndzytgsmctxmkjdzujxdutaxmbjaduvjaetdugymzqqdszfzmaetajfzdvcjxg"


bigrams = {}

for i in range(len(text1) - 1):
    sub = text1[i:i+2]
    if sub in bigrams:
        bigrams[sub] = bigrams[sub] + 1
    else:
        bigrams[sub] = 1

for i in range(len(text2) - 1):
    sub = text2[i:i + 2]
    if sub in bigrams:
        bigrams[sub] = bigrams[sub] + 1
    else:
        bigrams[sub] = 1

sort_orders = sorted(bigrams.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
    if i[1] > 1:
        print(i[0], i[1])
