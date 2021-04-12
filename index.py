userBudget = float(input("Please enter your budget for the month: "))
moreExpenses = "Y"
totalExpenses = 0

while moreExpenses == "Y":
    userExpense = float( input("Enter an expense: ") )
    totalExpenses = totalExpenses + userExpense
    moreExpenses = input("Do you have more expense? Y for yes, any key for no: "

if totalExpenses > userBudget:
    print("You were over your budget of", userBudget, " by ", totalExpenses - \
        userBudget)
elif totalExpenses < userBudget:
    print("You were under your budget of," , userBudget, " by "), userBudget - \
        totalExpenses)
else:
    print("You used exactly your budget of", userBudget)




