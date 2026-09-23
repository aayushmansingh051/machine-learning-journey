friends=['Aayushman','Aditya','kunal']
result=[]
for name in friends:
 result.append((name,len(name)))

print(result)
yours={
'Clothes': 1100,
'Shoes'  : 1000,
'Watch'  : 900,
'Mobile_Recharge' : 699,
'Petrol' : 1980,
}  

wife_expenses = {
'Mobile Recharge': 799,
'DTH recharge': 999,
'Clothes': 2310,
'Makeup': 3670,
'Shoes': 999
}

total_yours=sum(yours.values())
total_wife=sum(wife_expenses.values())

print("total value of your expense is: ", total_yours)
print("total value of wife expense is: ", total_wife)

if total_wife>total_yours:
  print("wife spends more")

else:
  print("you spends more")
#find common_item

common_items=set(yours.keys()) & set(wife_expenses.keys())
  #Find out which thing you and your wife spending more

for item in common_items:
    if yours[item] > wife_expenses[item]:
        print(f"You spend more on {item}.")
    elif wife_expenses[item] > yours[item]:
        print(f"Your wife spends more on {item}.")
    else:
        print(f"Both spend equally on {item}.")

