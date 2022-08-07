import pywhatkit


number = ['9567379500']
sendtimer = ['47']
whatsnum = '+91' + number[0]
pywhatkit.sendwhatmsg(whatsnum, 'Hello', 12, int(sendtimer[0]))
# print(f"{whatsnum} at {int(sendtimer[i])}")
