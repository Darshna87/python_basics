'''
Problem Name: MERGESORT
Problem Difficulty: None
Problem Constraints: 1<=N<=2*10^5<br>
|Ai|<=10^9

Problem Description:
Given an array *A*, of *N* elements. Sort the array using mergesort algorithm.

Input Format: A single integer, *N*, denoting the number of elements in array. Next line contains *N* integers, denoting the elements of array.
Sample Input: 5
3 6 4 1 2

Output Format: Print in a single line, *N* spaced integers, denoting the elements of array *A* in sorted order.
Sample Output: 1 2 3 4 6

'''


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
#if __name__ == '__main__':
print("Enter numbers between 0 and 1000")
arr = [int(x) for x in input().split()]

 #   print("Given array is", end="\n")
printList(arr)
mergeSort(arr)
print("Sorted array is: ", end="\n")
printList(arr)
