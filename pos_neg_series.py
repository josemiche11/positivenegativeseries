num= int(input("Enter the length: "))
i=1
k=1
m=2
while i!=num+1:
    for j in range(k):
        if i!=num+1:
            print( ( (-1)**m )* i, end=" ")
            i=i+1
    m= m+1
    k= k+1
