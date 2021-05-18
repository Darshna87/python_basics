'''

Problem Name: QUICKSORT
Problem Difficulty: None
Problem Constraints: 1<=N<=2*10^5 <br>
|Ai|<=10^9
Problem Description:
Given an array *A*, of *N* elements. Sort the array using quicksort algorithm.(**Note :** Use randomized quicksort, otherwise worst case will not pass).

Input Format: A single integer, *N*, denoting the number of elements in array. Next line contains *N* integers, denoting the elements of array.
Sample Input: 5
3 6 4 1 2

Output Format: Print in a single line, *N* spaced integers, denoting the elements of array *A* in sorted order.
Sample Output: 1 2 3 4 6
'''


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

print("Enter numbers between 0 and 1000")
lst = [int(x) for x in input().split()]

print(quicksort(lst))
