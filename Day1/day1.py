def part1():
    list1 = []
    list2 = []
    with open("s1.txt",'r') as myfile:
        for i,line in enumerate(myfile):
            list1 = [list1, int(line.split()[0])]
            list2 = [list2, int(line.split()[1])]
    list1.sort()
    list2.sort()
    _sum = 0
    for i in range(len(list1)):
        _sum+=abs(list1[i]-list2[i])
    return _sum

def part2():
    list1 = []
    list2 = []
    with open("s2.txt",'r') as myfile:
        for line in myfile:
            list1 = [list1, int(line.split()[0])]
            list2 = [list2, int(line.split()[1])]
    _sum = 0
    for i in range(len(list1)):
        if list2.count(list1[i]):
            _sum+=list1[i]*list2.count(list1[i])
    return _sum

