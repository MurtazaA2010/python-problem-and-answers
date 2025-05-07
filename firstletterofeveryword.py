"""
this code can be used to print the first letter of every word of a sentence or string for custom test cases
codeforces div4
"""


t = int(input())

for i in range(t):
    n = input()
    for s in n.split():
        print(s[0], end='')
    print() 
