def sort(num):
    biggest = num[0]
    for i in range(len(num)):
        if biggest < num[i]:
            biggest = num[i]
    return biggest
print(sort([1010,-10,1,2,3,4,1,12,5,50,50,100]))