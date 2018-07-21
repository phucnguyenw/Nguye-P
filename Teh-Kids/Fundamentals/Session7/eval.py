def calc(x,y,op):
    if op=="+":
        res=x+y
    elif op=="-":
        res=x-y
    elif op=="*":
        res=x*y
    elif op=="/":
        res=x/y
    return res

res = calc(10,2,"*")
print(res)

    