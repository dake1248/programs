def tax1(income):
    if income>10000:
        pay=3000*0.005+2000*0.01+5000*0.015+(income-10000)*0.02
        return pay
    else:
        if income>5000:
            pay=3000*0.005+2000*0.01+(income-5000)*0.015
            return pay
        else:
            if income>3000:
                pay=3000*0.005+(income-3000)*0.01
                return pay
            else:
                pay=income*0.005
                return pay
        
        
while True:
    inc=int(input("input your income:"))
    print("your pay("+str(inc)+"the tax is:  ",tax1(inc))

