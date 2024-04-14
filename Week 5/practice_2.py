def changeme(myList):
    # This changes a passed list
    myList.append([1,2,3,4])
    print("Values inside the function: ", myList)
    return

myList = [10, 20, 30]
changeme(myList)
print("Values outside the function: ", myList)