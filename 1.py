def bubbleSortasc(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
#arr = [64, 34, 25, 12, 22, 11, 90]
arr = []
elem = int(input("Number of elements you want:"))
for i in range(0, elem):
    arr.append(int(input("Enter number :"))) #raw_input() does not work in python3. Use input()

bubbleSortasc(arr)

print ("Array sorted in ascending order is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), #trailing comma for Python2 to avoid newline
    						#print(arr[i],end=' ') for Python3, space-separated

#in Python3, each element is printed on a new line. In Python2, on the same line.
