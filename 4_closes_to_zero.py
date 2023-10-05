def takeClosest(myList):
    myNumber = 0
    newlst = []
    for i in myList:
        newlst.append(i - myNumber)
    lstt = [abs(ele) for ele in newlst]
    print(myList.index(myList[lstt.index(min(lstt))]))
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element  
print(lst)
takeClosest(lst)
