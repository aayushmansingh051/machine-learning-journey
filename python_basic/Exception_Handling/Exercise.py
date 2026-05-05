#Q1 You have the following python code.
try:
    lst = [int(x) for x in input().split()]
    i = int(input("Enter Index: "))
    print(lst[i])
except Exception as e:
    print("Exception occured",e)
     
#Q2 You have certain employee records as a list of dictionaries. The dictionary contains the following information.
employees = [
    {"id": 1, "first_name": "Virat", "middle_name": "Kumar", "last_name": "Kohli"},
    {"id": 2, "first_name": "Rohit", "last_name": "Sharma"},
    {"id": 3, "first_name": "MS", "middle_name": "Singh", "last_name": "Dhoni"}
]

for employee in employees:

    try:
        full_name = (
            employee['first_name'] + " " +
            employee['middle_name'] + " " +
            employee['last_name']
        )

    except Exception as e:
        print("exception is: ",e)

    print(full_name)