import pywhatkit
number = []
send_hour = []
send_minute = []

n = int(input("How many numbers : "))
for x in range(0, n):
    number.append(int(input(f"enter {x+1}th element : ")))
    send_hour.append(int(input(f"schedule hour for {number[x]} :")))
    send_minute.append(int(input(f"schedule minute for {number[x]} :")))

print('\n')
print(
    f"list of numbers :{number} \nlist of hour :{send_hour} \nlist of minutes :{send_minute}")
print('\n')
pywhatkit.sendwhatmsg_to_group

i = 0
while(i < n):

    whatsnum = '+91' + str(number[i])
    print(
        f"{whatsnum} will send at {send_hour[i]} hour {send_minute[i]} minutes")
    i = i+1
    pywhatkit.sendwhatmsg(whatsnum, 'happy coding', int(
        send_hour[i]), int(send_minute[i]))
