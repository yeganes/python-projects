#phase_1 : asking for inputs
expenses_numbers = int(input("how many expenses did you have ? "))

expenses_dic = {}
# an empty dictioanry so we can store in later.
for i in range(expenses_numbers):

    expenses_name = str(input("what did you buy tell me one by one: "))

    expenses_amount = int(input(f"how much did you buy {expenses_name} ? "))

    expenses_dic[expenses_name] = expenses_amount
#dictionary has got values and keys
print(expenses_dic)

#phase_2  : calculating the final result
lowest_name = min(expenses_dic, key=expenses_dic.get)

lowest = expenses_dic[lowest_name]

highest_name = max(expenses_dic, key=expenses_dic.get)

highest = expenses_dic[highest_name]

total_spending = sum(expenses_dic.values())

average_spending = total_spending / expenses_numbers

print("the lowest spending is:", lowest, "for", lowest_name)

print("the highest spending is:", highest, "for", highest_name)
print("your total expenses is:", total_spending,
      "and your average spending is", average_spending)