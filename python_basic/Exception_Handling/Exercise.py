#Q1 You have the following python code.
try:
    lst = [int(x) for x in input().split()]
    i = int(input("Enter Index: "))
    print(lst[i])
except Exception as e:
    print("Exception occured",e)
     

