from random import randint
number=randint(1,100)
print(number)

playing = True
count = 0
while playing:
    n= int(input("guess my number(1,100):"))

    if n== number:
        print("correct")
        playing= False

    elif n>number:
        print("too big")
    else:
        print("too small")

    count+=1
    if count==7:
        print("you lose")
        playing= False