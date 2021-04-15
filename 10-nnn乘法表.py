def printnn(ilist,start=1,max=9):
    for x in range(start,max):
        total = 1
        for x in range(len(ilist)):
            total = total * ilist[x]
            print(str(ilist[x]) + " *  ", end="")
        print(" = ", total)
    print("")


def kernel(ilist,start=1,cur=2,max=9):
    while True:
        # 印出所有的相乘字串
        printnn(ilist,start=start,max=max)
        ilist[cur]=ilist[cur]+1
        if ilist[cur]>max:
            return cur
        else:
            cur=kernel(list1, start=start, cur=cur, max=max)






def nnmul(level=3,start=1,max=9):
    list1 = []
    for x in range(level):
        list1.append(start)
    print(list1)
    kernel(list1,start=1, cur=level-1,max=9)


nnmul(level=3,start=1,max=9)