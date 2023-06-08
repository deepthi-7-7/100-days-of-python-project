print("Welcome to the  tip calculator \n")
bill=float(input('What is the total bill? '))
print("\n")
persons=int(input("Among how many persons you wanted to share the bill? "))
print("\n")
tip=int(input("What percentage of tip you wanted to give? "))
print("\n")
tip_perc=tip/100

should_pay=(bill+(bill*tip_perc))/persons
# final_amount=round(should_pay,2)
print(f"So the amount of money each person should pay is: {should_pay:.2f}")
