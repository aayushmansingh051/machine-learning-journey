def find_total(expenses):
    total=0
    for expense in expenses:
        total+=expense

        return total
    
    expense_sergery=[20,30,202,45]
    expence_sundar=[20,45,60.50]

    total=find_total(expense_sergery)
    print("the total_expense_salary is: ",total)

    total =find_total(expence_sundar)
    print("the total_sundar_salary is: ",total)

    return total
