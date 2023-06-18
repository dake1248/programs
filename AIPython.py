def function(k):
    print("int k is:  ",k)
def function1(k):
    print("return k*2 is :",k*2)
    return k*2


a=100
function(a)

b=200

while b<4000:
    function(b)
    b=function1(b)


