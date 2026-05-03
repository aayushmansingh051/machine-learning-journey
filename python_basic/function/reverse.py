def master_yoda(sentence):
    words=sentence.split()
    reversed_words=words[::-1]
    return "".join(reversed_words)

print(master_yoda("I am learning python"))

def pay_bill(expenses, percent_commission=9.8, special_offer_amount=None):
    total = sum(expenses)

    # Check for special offer
    if special_offer_amount is not None and total > special_offer_amount:
        percent_commission += 1.2

    # Calculate final bill
    final_amount = total + (total * percent_commission / 100)

    return final_amount


# Example 1
print(pay_bill([100, 200, 300]))

# Example 2
print(pay_bill([100, 200, 300], 10))

# Example 3
print(pay_bill([100, 200, 300], 10, 500))