num=int(input("Num: "))
reverse=0
temp = num
while temp!=0:
    reverse=reverse*10+temp%10
    temp=temp//10



if num==reverse:
    print("pallindrome")
else:
    print("Not pallindrome")