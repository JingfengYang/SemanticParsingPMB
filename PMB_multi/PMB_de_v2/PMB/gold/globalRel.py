globals=['EQ(','CLOCK_TIME(','CARD_REL(']
rel=[]
sdrsrel=[]
with open('train_input.txt', 'r', encoding='utf-8') as r:
    while True:
        l1 = r.readline()
        l2 = r.readline().strip().split()
        l3 = r.readline()
        l4 = r.readline()
        l5 = r.readline()
        l6 = r.readline().strip().split()
        l7 = r.readline()
        if l1 == "":
            break
        for i in range(len(l6)-1):
            if l6[i][-1]=='(' and l6[i+1][-1].isdigit() and not l6[i][:-1] in l2:
                if  not l6[i] in rel and not l6[i] == 'EQ(' and not '~' in l6[i]:
                    rel+=[l6[i]]
        for i in range(len(l6)-1):
            if l6[i]=='SDRS(':
                assert(l6[i+1][-1]=='(')
                if not l6[i+1] in sdrsrel:
                    sdrsrel += [l6[i + 1]]
rel+=['UNK-GLO(']
with open('tag.txt', 'w', encoding='utf-8') as w:
    for x in rel:
        w.write(x+'\n')
print(sdrsrel)
