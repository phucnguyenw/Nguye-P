diict={
    "hc":"hoc",
    "ng":"ngu",
    "pt":"ph tr",
    "eny":"em nguoi yeu",
    "any":"anh nguoi yeu",
    "ngta":"nguoi ta",
    

}
loop=True
while loop:
    for key in diict.keys():
        print(key,end="\t")
    print()
    n=input("Your code?")
    if n in diict:
        print(diict[n])
    else:
        print("NOt found")
        contribute=input("Do you want to contribute word translation?(Y/N)").lower
        if contribute=="y":
            print("tks")
        else:
            print("Bye")
            loop=False
        