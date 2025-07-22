import json
import tkinter as tk
from tkinter import messagebox

# ---------- JSON File Functions ----------

def load_user_data():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

# ---------- Expense Tracker Functions ----------

def add_expense(username, expense):
    users = load_user_data()
    if username in users:
        users[username]["expenses"].append(expense)
        save_user_data(users)
        messagebox.showinfo("Success", "Expense added successfully!")
    else:
        messagebox.showerror("Error", "User not found.")

def display_expenses(username):
    users = load_user_data()
    if username in users:
        expenses = users[username]["expenses"]
        if expenses:
            messagebox.showinfo("Your Expenses", "\n".join(expenses))
        else:
            messagebox.showinfo("Expenses", "No expenses recorded.")
    else:
        messagebox.showerror("Error", "User not found.")

def open_expense_tracker(username):
    window = tk.Toplevel()
    window.title("Expense Tracker")

    tk.Label(window, text="Expense:").pack()
    expense_entry = tk.Entry(window)
    expense_entry.pack()

    tk.Button(window, text="Add Expense", command=lambda: add_expense(username, expense_entry.get())).pack()
    tk.Button(window, text="Display Expenses", command=lambda: display_expenses(username)).pack()

# ---------- Currency Converter Functions ----------

def convert_currency(from_currency_entry, to_currency_entry, amount_entry, result_label):
    exchange_rates = {
        "USD": 1.0,  # US Dollar
        "EUR": 0.85,  # Euro
        "GBP": 0.73,  # British Pound
        "JPY": 110.0,  # Japanese Yen
        "INR": 74.22,  # Indian Rupee
        "AUD": 1.34,  # Australian Dollar
        "CAD": 1.25,  # Canadian Dollar
        "CNY": 6.45,  # Chinese Yuan
        "SGD": 1.35,  # Singapore Dollar
        "CHF": 0.92,  # Swiss Franc
        "HKD": 7.77,  # Hong Kong Dollar
        "KRW": 1160.0,  # South Korean Won
        "MXN": 20.25,  # Mexican Peso
        "NZD": 1.42,  # New Zealand Dollar
        "ZAR": 14.65,  # South African Rand
        "SEK": 8.63,  # Swedish Krona
        "NOK": 8.85,  # Norwegian Krone
        "DKK": 6.32,  # Danish Krone
        "RUB": 73.5,  # Russian Ruble
        "BRL": 5.25,  # Brazilian Real
        "AED": 3.67,  # UAE Dirham
        "SAR": 3.75,  # Saudi Riyal
        "TRY": 8.5,  # Turkish Lira
        "THB": 32.8,  # Thai Baht
        "IDR": 14300.0,  # Indonesian Rupiah
        "MYR": 4.18,  # Malaysian Ringgit
        "PHP": 50.1,  # Philippine Peso
        "VND": 23000.0,  # Vietnamese Dong
        "PKR": 160.0,  # Pakistani Rupee
        "BDT": 85.0,  # Bangladeshi Taka
        "EGP": 15.7,  # Egyptian Pound
        "NGN": 410.0,  # Nigerian Naira
        "KWD": 0.30,  # Kuwaiti Dinar
        "BHD": 0.38,  # Bahraini Dinar
        "OMR": 0.39,  # Omani Rial
        "QAR": 3.64,  # Qatari Riyal
        "LKR": 200.0,  # Sri Lankan Rupee
        "NPR": 118.0,  # Nepalese Rupee
        "ISK": 125.0,  # Icelandic Krona
        "PLN": 3.85,  # Polish Zloty
        "CZK": 21.7,  # Czech Koruna
        "HUF": 295.0,  # Hungarian Forint
        "ILS": 3.25,  # Israeli Shekel
    }

    try:
        from_currency = from_currency_entry.get().upper()
        to_currency = to_currency_entry.get().upper()
        amount = float(amount_entry.get())

        if from_currency in exchange_rates and to_currency in exchange_rates:
            rate = exchange_rates[to_currency] / exchange_rates[from_currency]
            result = amount * rate
            result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            result_label.config(text="Invalid currency code(s)")
    except ValueError:
        result_label.config(text="Invalid amount")

def open_currency_converter():
    window = tk.Toplevel()
    window.title("Currency Converter")

    tk.Label(window, text="From Currency:").pack()
    from_entry = tk.Entry(window)
    from_entry.pack()

    tk.Label(window, text="To Currency:").pack()
    to_entry = tk.Entry(window)
    to_entry.pack()

    tk.Label(window, text="Amount:").pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    tk.Button(window, text="Convert", command=lambda: convert_currency(from_entry, to_entry, amount_entry, result_label)).pack()

# ---------- Authentication Functions ----------

def login_button_click():
    username = username_entry.get()
    password = password_entry.get()
    users = load_user_data()
    if username in users and users[username]["password"] == password:
        messagebox.showinfo("Login", "Login successful!")
        login_window.destroy()
        main_menu(username)
    else:
        messagebox.showerror("Login Error", "Invalid credentials.")

def create_account_button_click():
    username = create_username_entry.get()
    password = create_password_entry.get()
    users = load_user_data()
    if username in users:
        messagebox.showerror("Error", "Username already exists.")
    else:
        users[username] = {"password": password, "expenses": []}
        save_user_data(users)
        messagebox.showinfo("Success", "Account created successfully!")

# ---------- Main Menu ----------

def main_menu(username):
    window = tk.Tk()
    window.title("Main Menu")

    tk.Label(window, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=10)

    tk.Button(window, text="Expense Tracker", width=20, command=lambda: open_expense_tracker(username)).pack(pady=5)
    tk.Button(window, text="Currency Converter", width=20, command=open_currency_converter).pack(pady=5)

    window.mainloop()

# ---------- Login UI ----------

login_window = tk.Tk()
login_window.title("Login Portal")

tk.Label(login_window, text="Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login_button_click).pack(pady=5)

tk.Label(login_window, text="Or Create an Account").pack(pady=5)

tk.Label(login_window, text="New Username:").pack()
create_username_entry = tk.Entry(login_window)
create_username_entry.pack()

tk.Label(login_window, text="New Password:").pack()
create_password_entry = tk.Entry(login_window, show="*")
create_password_entry.pack()

tk.Button(login_window, text="Create Account", command=create_account_button_click).pack(pady=5)

login_window.mainloop()
