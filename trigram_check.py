text1 = "xmenjxmefagfgudemvdseusxvjzgjwSmefdugadxfsemefdwgdzmckdzfenxgfefgmvdsesupjzgemuptuklfccfmxtmscenszgedu"
text2 = "gezjukemjumpjupztejgjchwstigfmajdsefzmaetajazjmejmxjemfndzytgsmctxmkjdzujxdutaxmbjaduvjaetdugymzqqdszfzmaetajfzdvcjxg"


trigrams = {}

for i in range(len(text1) - 2):
    sub = text1[i:i+3]
    if sub in trigrams:
        trigrams[sub] = trigrams[sub] + 1
    else:
        trigrams[sub] = 1

for i in range(len(text2) - 2):
    sub = text2[i:i+3]
    if sub in trigrams:
        trigrams[sub] = trigrams[sub] + 1
    else:
        trigrams[sub] = 1

sort_orders = sorted(trigrams.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
    if i[1] > 1:
        print(i[0], i[1])
