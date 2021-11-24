print("This is Insertion sort")

arr = [5 , 7 ,2 ,0 ,56, 34 , 89 , 10 , 4]

def insertion(arr) :
    for i in range (1,  len (arr)) :
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j-=1

        arr[j + 1] = key

insertion(arr)
print(arr)
