num=int(input("Num: "))
while num>0:
    j=num%10
    if j!=1 and j!=0:
        print("Not a binary")
        break
    num//=10
    if num==0:
        print("Binary")
