from random import randint
numb=randint(0,100)

print(numb)
playing=True
count=0
 
while playing:
    o=int(input("Guuess my number(0-100): "))
    
    if o==numb:
        print("correct")
        playing=False

    elif o>numb:
        print("too big")

    else:
        print("too small")

    count+=1
