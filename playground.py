import copy

count = 4
inputList = [1,3,1,1]

totalList = []

for t in range(1, len(inputList)):

    g1 = copy.copy(inputList[0:t])
    g2 = copy.copy(inputList[t:len(inputList)-1])

    g1_total = 0
    g2_total = 0

    total = 0

    for j in range(len(g1)):
        g1_total += g1[j]
    for h in range(len(g2)):
        g2_total += g2[h]

    total = abs(g1_total - g2_total)

    totalList.append(total)

print(min(totalList))
