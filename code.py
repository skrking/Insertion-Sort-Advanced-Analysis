def mergeSort(array):
    global count
    length = len(array)
    mid = length / 2
    if length == 1:
        return array
    array1 = mergeSort(array[0:mid])
    array2 = mergeSort(array[mid:length])
    temp_count = count
    temp = []
    array1.append(1000001)
    array2.append(1000001)
    ptr1 = 0
    ptr2 = 0
    for i in range(length):
        if array1[ptr1] > array2[ptr2]:
            temp.append(array2[ptr2])
            count += (mid - ptr1)
            ptr2+=1
        else:
            temp.append(array1[ptr1])
            ptr1+=1
    array = temp
    return array

T = input()
count = 0
for i in range(T):
    count = 0
    N = input()
    array = map(int, raw_input().split())
    mergeSort(array)
    print count