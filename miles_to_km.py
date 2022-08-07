# convert miles to km
choose = int(input("Choose an option : \n 1. Km to mile \n 2. mile to Km \n"))
conversion_factor = 0.62137
if choose == 1:
    kilometer = float(input("Enter kilometer = "))
    miles = kilometer*conversion_factor
    print(f'{kilometer} km is {miles} miles')
else:
    miles = float(input("Enter miles = "))
    kilometer = miles/conversion_factor
    # print(f'{miles} miles is {kilometer} kilometers')
    print('%0.3f miles is equal to %0.3f Kms' % (miles, kilometer))
    print('% 0.2f miles is %0.4f Kms' % (miles, kilometer))
