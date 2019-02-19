print("Welcome, let's find how long you need to save for your new home!")

total_cost = int(input("How much is your dream home:"))
annual_salary = int(input("What is your annual salary:"))
current_savings = int(input("How much have you already saved for your dream home:"))
r = 0.04
savings_return = ((annual_salary / 12) * r)
percentage_down = float(total_cost * 0.25)



monthly_saving = (total_cost - ((annual_salary / 12) * r))

print(savings_return)

print("Your total cost is ", total_cost)
print("The amount you need to put down is ", percentage_down)
print("Each month you need to save ", str(monthly_saving))
(monthly_saving)



# monthlysaving_goal= (total_cost - current_savings)
# monthly salary = annual_salary / 12

#print("To buy a house for ", total_cost, "with a salary of ", annual_salary, "and " current_saved, "you will need to put down", percentage_down)
