
'''
Problem Name: Pythagorean's Challenge

Problem Difficulty: 1
Problem Constraints: A<=1000
Problem Description:
Given a non negative integer A, print all the pairs of integers(a,b) such that

a and b are positive integers

a<=b and
a^2 + b^2 = A
0 <= A

Input Format: First line contains T , number of test cases. Next T lines contain a single integer A each.
Sample Input: 3
1
9
25
Output Format: T lines each containing a pair (a,b) in sorted order.
Sample Output: (0,1)
(0,3)
(0,5) (3,4)
'''


def pythagoras(c):
    a = 0
    while a*a <= c:
        b = a
        while b*b <= c:

            if a*a + b*b == c:
                print("( {0} , {1} )".format(a,b), end=" ")
            b += 1

        a += 1

print("Enter numbers < 1000>")
lst = [int(x) for x in input().split()]

for i in range(0, len(lst), 1):
    print("\n {0} : ".format(lst[i]), end=" ")
    pythagoras(lst[i])

