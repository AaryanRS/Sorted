print('This is bubble sort')

def Bubble(arr) :
    n = len(arr)

    for i in range(n):
        for j in range(0 , n - i - 1):
            if arr[j] > arr[j +1]:
                arr[j] ,arr[j + 1] = arr[j + 1] , arr[j] #swapping


arr = [7,8,4,5,9,2,3,1,6]
Bubble(arr)
print(arr)