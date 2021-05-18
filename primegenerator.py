'''
Problem Name: Prime Generator
Problem Difficulty: 1
Problem Constraints: 1 <= m <= n <= 1000000000
 n-m<=100000
Problem Description:
Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!

Input Format: The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines, there are two numbers m and n separated by a space.
Sample Input: 2
1 10
3 5
Output Format: For every test case print all prime numbers p such that m <= p <= n, all primes per line, test cases separated by an empty line.
Sample Output: 2 3 5 7
3 5
'''


def checkPrime(n):
    
    if n == 1 or n == 0:
        return False

    for i in range(2, n, 1):

        if n % i == 0:
            return False

        else:
            pass

    return True


print("How many sequence you wnt to generate: ")
t = int(input())


for i in range(0, t, 1):

    print("\n Enter range:")
    a,b = [int(x) for x in input().split()]

    for j in range(a, b+1, 1):
        if checkPrime(j):
            print(j, end=" ")





    

    
