'''
Problem Name: Check prime
Problem Difficulty: None
Problem Constraints: 2 < N <= 1000000000
Problem Description:
Take as input a number N, print "Prime" if it is prime if not Print "Not Prime".

Input Format:
Sample Input: 3
Output Format:
Sample Output: Prime

'''

print("Enter a number")
n = int(input())

prime= True

if n == 0 or n == 1:
    prime = True

else:
    for i in range(2, n, 1):

        if n % i == 0:
                prime = False
                break

        else:
            pass

if prime:
    print("Prime")
else:
    print("Not prime")
