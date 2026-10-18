import sys
import requests

#####DATA#####

class WeeklyFinance():
    def __init__ (self, currency_code, currency):
        self.currency_code = currency_code
        self.currency = currency
        self.income = []
        self.expense_amounts = []

    def earn(self, money):
        self.income.append(money)

#####INPUT#####

def ask_number(prompt, number_type=float):
    while True:
        try:
            value = number_type(input(prompt).replace(",", "."))
            if value < 0:
                print("The number can't be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Try again.")

income_sources = ask_number("Enter the number of income sources: ", int)

#####CURRENCY#####

while True:
    print("1.$\n"
      "2.€\n"
      "3.zł")
    try:
        currency_select = int(input("Select your currency: "))
        if currency_select == 1:
            currency_code = "USD"
            currency = "$"
            break
        elif currency_select == 2:
            currency_code = "EUR"
            currency = "€"
            break
        elif currency_select == 3:
            currency_code = "PLN"
            currency = "zł"
            break
        else:
            print("Try again.")
    except ValueError:
        print("Try again.")

week  = WeeklyFinance(currency_code, currency)

#####API#####

try:
    if currency_code != "EUR":
        url = f"https://api.frankfurter.app/latest?from={currency_code}&to=EUR"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"]["EUR"]
except Exception as e:
    print(e)
    sys.exit()

#####INCOME#####

for i in range(income_sources):
    i += 1
    earned = ask_number(f"Enter the profit amount source{i} {currency}: ")
    week.earn(earned)

#####INFO EARNED#####

if week.income:
    print(f"total income: {sum(week.income):.2f} {currency}\n"
        f"minimum income: {min(week.income):.2f} {currency}\n"
        f"maximum income: {max(week.income):.2f} {currency}\n")
else:
    print(f"total income: 0.00 {currency}\n")

#####EXPENSES#####

expenses = ask_number("Enter the number of expenses: ", int)
for n in range(expenses):
    amount = ask_number(f"Enter expense {n + 1} amount {currency}: ")
    week.expense_amounts.append(amount)

#####TOTAL PROFIT#####

total = sum(week.income) - sum(week.expense_amounts)
print(f"total: {total:.2f} {currency}")

#####rate#####

if currency_code != "EUR":
    euro_currency = total * rate
    print(f"{euro_currency:.2f} €")

#####WEEKS#####

week_number = 1
separator = "| ================================"

try:
    with open("database.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        if line.strip() == separator:
            week_number += 1

except FileNotFoundError:
    pass

#####DATA#####

if currency_code == "EUR":
    rate = 1

income_for_file = sum(week.income) * rate
expenses_for_file = sum(week.expense_amounts) * rate
total_for_file = total * rate

with open("database.txt", "a", encoding="utf-8") as file:
    file.write(
        f"{separator}\n"
        f"| {week_number} week:\n"
        f"| Income: {income_for_file:.2f} €\n"
        f"| Expenses: {expenses_for_file:.2f} €\n"
        f"| Total: {total_for_file:.2f} €\n"
    )
