n=int(input("Enter the range:"))
space=n-1                   
for i in range(n):          #for range
    for j in range(space):  #to give spaces 
        print(end=" ")
    space-=1                #for every iteration decreased spaces 
    for k in range(i+1):    #to print *
        print("*",end=" ")
    print("\r")