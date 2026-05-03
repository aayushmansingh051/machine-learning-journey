n=input("enter the number")
n=int(n)

if n%2==0:
    print("the number is even")
else:
    print("the number is odd")

    #EXERCISE
IND = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

city_name=input("enter the city name: ")
if city_name in IND:
    print(f"{city_name} present in INDIA")
elif city_name in USA:
    print(f"{city_name} present in USA")
else:
    print(f"{city_name} present in the UK")

county1=input("eneter first country name: ")
county2=input("eneter second country name: ")

if county1 in IND and county2 in IND:
    print("both city belongs to the same country")
elif county1 in USA and county2 in USA :
    print ("both the city belong to the same county")
elif county1 in UK and county2 in UK :
    print ("both the city  belong to the same county")
else:
    print ("both the city do not belong to the same county")