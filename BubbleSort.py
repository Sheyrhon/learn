def Bubblesort(mlist):
    for passnum in range(len(mlist)-1,0,-1):
        for j in range(passnum):
            if mlist[j]>mlist[j+1]:
                mlist[j], mlist[j+1] = mlist[j+1],mlist[j]
                
mlist = [23,14,27,18,9,48,29,7,39]
Bubblesort(mlist)
print(mlist)