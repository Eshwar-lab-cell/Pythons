#This program calculates prime numbers in a range between two numbers using python

a , b  = map(int,input().split())

for i in range(a,b+1) :
    c  = 0
    for j in range(1,i+1) :
        if i%j == 0 :
            c += 1
    if c == 2 :
        print(i)
