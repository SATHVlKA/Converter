import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        amount_label = tk.Label(self.root, text="Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        amount_entry = tk.Entry(self.root, textvariable=self.amount_var)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        from_currency_label = tk.Label(self.root, text="From Currency:")
        from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        from_currency_combobox = ttk.Combobox(self.root, textvariable=self.from_currency_var)
        from_currency_combobox['values'] = self.get_currency_list()
        from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

        to_currency_label = tk.Label(self.root, text="To Currency:")
        to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        to_currency_combobox = ttk.Combobox(self.root, textvariable=self.to_currency_var)
        to_currency_combobox['values'] = self.get_currency_list()
        to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

        convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        convert_button.grid(row=3, column=0, columnspan=2, pady=20)

        result_label = tk.Label(self.root, textvariable=self.result_var, font=('Helvetica', 12, 'bold'))
        result_label.grid(row=4, column=0, columnspan=2)

    def convert_currency(self):
        try:
            amount = self.amount_var.get()
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            if not amount or not from_currency or not to_currency:
                raise ValueError("Please enter valid values for amount and currencies.")

            exchange_rate = self.get_exchange_rate(from_currency, to_currency)
            converted_amount = amount * exchange_rate

            result_str = f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
            self.result_var.set(result_str)
        except Exception as e:
            self.result_var.set(f"Error: {e}")

    def get_exchange_rate(self, from_currency, to_currency):
        c = CurrencyRates()
        return c.get_rate(from_currency, to_currency)

    def get_currency_list(self):
        c = CurrencyRates()
        return list(c.get_rates("").keys())

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
