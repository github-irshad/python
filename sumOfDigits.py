import string


def getSum(n):
    sum = 0
    for digit in str(n):
        sum = sum + int(digit)
    return sum


n = 258
print(getSum(n))
print('***************************************')


a = "54664546"
c = "fgdfadfafsud"
# b = string(a).digit
b = string(c).digit
