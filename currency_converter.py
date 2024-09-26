import tkinter as tk
import requests

class CurrencyConverter(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.root = tk.Toplevel(master)
        self.root.title("Currency Converter")
        self.root.geometry("400x350")
        
        self.currencies = self.get_currencies()
        self.from_currency = tk.StringVar()
        self.to_currency = tk.StringVar()
        self.from_currency.set("USD")
        self.to_currency.set("INR")
        
        from_currency_label = tk.Label(self.root, text="From Currency:", font=("Arial", 12))
        from_currency_label.grid(row=0, column=0, padx=10, pady=10)
        
        from_currency_option = tk.OptionMenu(self.root, self.from_currency, *self.currencies)
        from_currency_option.config(width=10, font=("Arial", 12))
        from_currency_option.grid(row=0, column=1, padx=10, pady=10)
        
        to_currency_label = tk.Label(self.root, text="To Currency:", font=("Arial", 12))
        to_currency_label.grid(row=1, column=0, padx=10, pady=10)
        
        to_currency_option = tk.OptionMenu(self.root, self.to_currency, *self.currencies)
        to_currency_option.config(width=10, font=("Arial", 12))
        to_currency_option.grid(row=1, column=1, padx=10, pady=10)
        
        amount_label = tk.Label(self.root, text="Amount:", font=("Arial", 12))
        amount_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.amount_entry = tk.Entry(self.root, font=("Arial", 12))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)
        
        convert_button = tk.Button(self.root, text="Convert", font=("Arial", 12), command=self.convert)
        convert_button.grid(row=3, column=1, padx=10, pady=10)
        
        self.result_label = tk.Label(self.root, font=("Arial", 12))
        self.result_label.grid(row=4, column=1, padx=10, pady=10)
        
        self.date_label = tk.Label(self.root, font=("Arial", 12))
        self.date_label.grid(row=5, column=1, padx=10, pady=10)
        
        self.refresh_button = tk.Button(self.root, text="Refresh", font=("Arial", 12), command=self.refresh)
        self.refresh_button.grid(row=6, column=1, padx=10, pady=10)
        
        self.exit_button = tk.Button(self.root, text="Exit", font=("arial", 12), command=lambda: self.root.destroy())
        self.exit_button.grid(row=6, column=2, padx=10, pady=10)
        
        self.root.mainloop()
        
    def get_currencies(self):
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        currencies = list(data["rates"].keys())
        return currencies
        
    def convert(self):
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid amount entered.")
            return
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        exchange_rate = data["rates"].get(to_currency)
        if exchange_rate is None:
            self.result_label.config(text="Invalid currency selected.")
        else:
            converted_amount = amount * exchange_rate
            self.result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}", fg="blue")
            self.date_label.config(text=f"Conversion rate as of {data['date']}")
            
    def refresh(self):
        self.currencies = self.get_currencies()
        from_currency_option = tk.OptionMenu(self.root, self.from_currency, *self.currencies)
        from_currency_option.config(width=10, font=("Arial", 12))
        from_currency_option.grid(row=0, column=1, padx=10, pady=10)
        
        to_currency_option = tk.OptionMenu(self.root, self.to_currency, *self.currencies)
        to_currency_option.config(width=10, font=("Arial", 12))
        to_currency_option.grid(row=1, column=1, padx=10, pady=10)
        
        self.result_label.config(text="")
        self.date_label.config(text="")
        self.amount_entry.delete(0, tk.END)