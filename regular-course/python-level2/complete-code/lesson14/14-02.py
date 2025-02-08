mylist = [1, 2, 4, 5, 3, 6]
for j in range(4, 0, -1):
    if mylist[j] < mylist[j - 1]:
        mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]
    else:
        break
print(mylist)
