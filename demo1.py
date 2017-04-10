
l = [1,2,3,5,6,4,4,11,21,5,21,0,1]

n =2
temp = n
for index, item in enumerate(l):

    # print temp
    if index == n:
        print item
        n = n + temp

