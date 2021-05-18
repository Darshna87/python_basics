'''
Problem Name: Pattern Numbers & Stars - 1
Problem Difficulty: None
Problem Constraints:
Problem Description:
Take as input N, a number. Print the pattern as given in output section for corresponding input.

Input Format: Enter value of N
Sample Input: 5
Output Format: All numbers and stars are Space separated
Sample Output:
1 2 3 4 5
1 2 3 4 *
1 2 3 * * *
1 2 * * * * *
1 * * * * * * *
'''


print("Enter a number")
n = int(input())

for i in range(1, n+1, 1):
    for j in range(1, n-i+2):
        print(j, end=" ")

    for k in range(1, (2*i-1)-1):
        print("*", end=" ")

    print("\n")
