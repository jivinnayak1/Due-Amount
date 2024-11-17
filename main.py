def calculate_change(total_amount, amount_given):
    if amount_given < total_amount:
        return "Amount given is less than the total amount. No change needed."
    change = amount_given - total_amount
    return change

# Example usage:
total_amount = float(input("Enter the total amount: "))
amount_given = float(input("Enter the amount given: "))
change = calculate_change(total_amount, amount_given)
print(f"Change required: {change}")
