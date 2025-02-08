mylist = [5, 4, 3, 2, 1]
for j in range(4, 0, -1):
    if mylist[j] < mylist[j - 1]:
        mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
    else:
        break
print(mylist)
