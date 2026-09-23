expenses=[1200,1300,1500,1700]
total_expense=0

for i, expense in enumerate(expenses):
 print(f"Month{i+1},expenses:{expense}")
total_expense=total_expense+expense
print("total_expence: ",total_expense)

for i in range(1,11):
 if i%2==1:
  print("odd Nos are: ",i)

for i in range(1,11):
 if i%2==0:
  continue
 print("odd Nos are: 2nd method",i)

 for n in range(1, -6, -2):
    print(n, end=', ')