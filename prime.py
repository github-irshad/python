# def prime(num):
#     if num > 1:
#         for i in range(2, int(num/2)+1):
#             if (num % i) == 0:
#                 return f"{num} is not a prime"
#             else:
#                 return f"{num} is a prime"
#     else:
#         return (num, "is not a prime number")


# # prime(int(input("Enter your number: ")))
# print(prime(int(input("Enter your number: "))))

while True:
    def prime(num):
        if num > 1:
            if num == 2:
                return "2 is prime"
            for i in range(2, num):
                if (num % i) == 0:
                    return f"{num} is not a prime"

                else:
                    return f"{num} is a prime"

        else:
            return f"{num} is not a prime"
    print(prime(int(input("Enter your number: "))))


# prime(int(input("Enter your number: ")))
