#asking user for the number of names to be sorted
nameList = []
n = int(input("Enter the total number of names you want to group "))

#storing the user input for the list of names and displaying it
for i in range(0, n):
    print("Enter name ", i + 1, )
    name = str(input())
    nameList.append(name)
print("User list is ", nameList)


groupList = []
for i in range(0, n, 6):
    group = nameList[i:(i+6)]
    if len(group) < 6:
        group = group + [""] * (6 - len(group))
    groupList.append(group)
print("Grouped list is ", groupList)