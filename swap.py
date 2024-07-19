def swaplist(list):

    start,*middle,end = list
    list = [end, *middle, start]
    return list

newlist = [10,15,30,45]

print(swaplist(newlist))

