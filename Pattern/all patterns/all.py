n=int(input("ENter the number of rows: "))
'''
1. Square of stars

* * * * * 
* * * * * 
* * * * * 
* * * * * 

for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end=" ")
    print()

2. Right-angled triangle

* 
* *
* * *
* * * *
* * * * *

stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars+=1

3. Inverted right-angled triangle

* * * * * 
* * * *
* * *
* *
*

stars=n
for row in range(1,n+1):
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars-=1

4. Pyramid

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars+=2
    spaces-=1

5. Inverted pyramid

  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *

stars=n*2-1
spaces=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars-=2
    spaces+=1

6. Right-angled triangle with numbers

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

stars=1
for row in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars+=1

7. Inverted right-angled triangle with numbers

1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1  

stars=n
for row in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars-=1

8. Hollow square

* * * * * 
*       *
*       *
*       *
* * * * *

stars=n
for row in range(1,n+1):
    for st in range(1,stars+1):
        if (row==1 or st==1) or (row==n or st==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

9. Diamond

    * 
  * * *
* * * * *
  * * *
    *

stars=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    if row<=n//2:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1

10. Right-angled triangle with numbers in reverse

        1 
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5


stars=1
spaces=n-1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        dummy+=1
    print()
    stars+=1
    spaces-=1

11. Pascal’s triangle

        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1


for i in range(n):
    num = 1
    print(' ' * (n - i), end='')
    
    for j in range(i + 1):
        print(num, end=' ')
        num = num * (i - j) // (j + 1)
    print()  
12.Hallow Traingle

* 
* *
*   *
*     *
* * * * *

for row in range(1,n+1):
    for col in range(1,row+1):
        if col==row or col==1 or row==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
13.Hourglass Pattern

  * * * * * * * * * 
    * * * * * * *
      * * * * *
        * * *
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *

stars=n
spaces=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    if row<=n//2:
        spaces+=1
        stars-=2
    else:
        spaces-=1
        stars+=2

14.Pattern

        1 
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1

spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(dummy,end=" ")
        if st<=stars//2:
            dummy+=1
        else:
            dummy-=1


    print()
    stars+=2
    spaces-=1
      
15.Zig-Zag Pattern

*       * 
  *   *
    *
  *   *
*       *

for row in range(1,n+1):
    for col in range(1,n+1):
        if col==row or col+row==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''

for row in range(1,n+1):
    for col in range(1,n+1):
        if (row==1  or col==1) or (row==n or col==n) :
            print("*",end="  ")
        else:
            print("  ",end=" ")
    print()
        
