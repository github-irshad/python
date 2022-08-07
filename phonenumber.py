from phonenumbers import carrier, geocoder, phonenumber, timezone
import phonenumbers

numx = int(input("enter mobile number \n"))
numy = "+91" + str(numx)
mobNo = phonenumbers.parse(numy)

print(f"timezone : {timezone.time_zones_for_number(mobNo)}")

print(f"carrier: {carrier.name_for_number(mobNo,'en')}")

print(f"geo: {geocoder.description_for_number(mobNo,'en')}")

print(f"valid: {phonenumbers.is_valid_number(mobNo)}")
