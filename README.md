# Income Tracker

A simple command-line program for tracking your weekly income and expenses.

## About

Income Tracker helps you keep track of your money week by week. Every week you enter your income and expenses, and the program calculates your total profit and saves the result to a text file (`database.txt`), so you can see your history over time.

I built this project to practice Python, working with APIs, object-oriented programming and file handling.

## Features

- Enter multiple income sources and expenses for each week
- Choose one of 3 currencies for the week: **USD**, **EUR** or **PLN**
- Converts the results to EUR using live exchange rates from the [Frankfurter API](https://www.frankfurter.app/)
- Shows total, minimum and maximum income
- Calculates the profit for the week
- Saves every week's report (in EUR) to `database.txt` and numbers the weeks automatically
- Handles invalid input (letters, negative numbers, `,` instead of `.`) and API errors without crashing

## Technologies

- **Python 3**
- **requests** — for getting exchange rates from an API
- **OOP** — weekly data is stored in a `WeeklyFinance` class
- **Exception handling** — for wrong input, API errors and a missing database file
- **Loops and conditional logic** (`if` / `else`)
- **Text file database** — data is stored in `database.txt`

## How to run

1. Install [Python 3](https://www.python.org/downloads/).
2. Install the required library:

   ```bash
   pip install requests
   ```

3. Clone the repository and run the program:

   ```bash
   git clone https://github.com/UserM0n/income-tracker.git
   cd income-tracker
   python main.py
   ```

## Usage

1. Start the program.
2. Enter the number of income sources.
3. Choose the currency for this week (USD, EUR or PLN).
4. Enter the amount for each income source.
5. Enter the number of expenses, then the amount of each one.
6. The program shows the totals and adds a new entry to `database.txt`.

Example of an entry in `database.txt`:

```
| ================================
| 1 week:
| Income: 250.00 €
| Expenses: 120.50 €
| Total: 129.50 €
```

## Project status

✅ **Version 1.0.0** — CLI version completed.

## Author

**Dzianis (Denis)** — [GitHub profile](https://github.com/UserM0n)

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
