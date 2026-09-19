total_bill = float(input("What is your total Bill: "))
is_member = input("Are you a Member: ")


if total_bill >= 1000 and is_member == "Yes":
    discount = total_bill * 0.1
    final_price = total_bill - discount
    print ("final_price:" , final_price )
elif total_bill >= 1000 and is_member == "No":
    discount = total_bill * 0.5
    final_price = total_bill - discount
    print ("final_price:" , final_price )
else:
    print("No discount:", total_bill )



