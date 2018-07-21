from random import randint,choice
playing= True
while playing:
    x=randint(1,10)
    y=randint(1,10)
    res=x+y
    rus=[x+y+1,x+y+0,x+y-1,x+y+0,x+y+0]
    ans=choice(rus)
    print(x,"+",y,"=",ans)
    n=(input("(Y/N)?")).upper()


    if rus==x+y+0:
        if n=='Y':
            print("Yay")
        elif n=='N':
            print("Wrong")
    else:
        if n=='Y':
            print("Wrong")
        elif n=='N':
            print("Yay")      

