# simple inetrest
# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.


# def simple_interest(p, t, r):
# 	print('The principal is', p)
# 	print('The time period is', t)
# 	print('The rate of interest is', r)

# 	si = (p * t * r)/100

# 	print('The Simple Interest is', si)
# 	return si


# # Driver code
# simple_interest(8, 6, 8)


def simp_interest(p, t, r):
    print(f'principal = {p} \n time = {t} \nrate = {r}\n')
    interest = (p*t*r)/100
    print(f"interest  = {interest}")
    return interest


simp_interest(10000, 3, 8)
