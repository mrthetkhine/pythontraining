def div(a,b):
    if b == 0:
        return ('Division by zero',None)
    else:
        return (None,a/b)

err,result = div(10,0)
if(err):
    print("Error ",err)
else:
    print("Result ",result)