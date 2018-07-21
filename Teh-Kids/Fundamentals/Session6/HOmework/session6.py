numb=int(input("Enter a number:"))
sum=0
for i in range(1,numb):
    if (numb % i)==0:
        sum=sum+i
if sum==numb:
    print(" It is a perfect number")
else :
    print(" It is not a perfect number")
