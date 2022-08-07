from datetime import date


def agecalculate(birthdate):
    today1 = date.today()
    age = today1.year - birthdate.year
    return age


while True:
    year = int(input("Enter year : "))
    month = int(input("Enter month : "))
    day = int(input("Enter day : "))
    birthdate = date(year, month, day)

    print(agecalculate(birthdate), "years")
    print("**************** \n ///////////////")
