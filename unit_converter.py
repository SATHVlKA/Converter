import tkinter as tk
from tkinter import ttk
from pint import UnitRegistry

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        self.amount_var = tk.DoubleVar()
        self.from_unit_var = tk.StringVar()
        self.to_unit_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        amount_label = tk.Label(self.root, text="Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        amount_entry = tk.Entry(self.root, textvariable=self.amount_var)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        from_unit_label = tk.Label(self.root, text="From Unit:")
        from_unit_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        from_unit_combobox = ttk.Combobox(self.root, textvariable=self.from_unit_var)
        from_unit_combobox['values'] = self.get_unit_list()
        from_unit_combobox.grid(row=1, column=1, padx=10, pady=10)

        to_unit_label = tk.Label(self.root, text="To Unit:")
        to_unit_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        to_unit_combobox = ttk.Combobox(self.root, textvariable=self.to_unit_var)
        to_unit_combobox['values'] = self.get_unit_list()
        to_unit_combobox.grid(row=2, column=1, padx=10, pady=10)

        convert_button = tk.Button(self.root, text="Convert", command=self.convert_units)
        convert_button.grid(row=3, column=0, columnspan=2, pady=20)

        result_label = tk.Label(self.root, textvariable=self.result_var, font=('Helvetica', 12, 'bold'))
        result_label.grid(row=4, column=0, columnspan=2)

    def convert_units(self):
        try:
            amount = self.amount_var.get()
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()

            if not amount or not from_unit or not to_unit:
                raise ValueError("Please enter valid values for amount and units.")

            ureg = UnitRegistry()
            quantity = amount * ureg(from_unit)
            converted_quantity = quantity.to(to_unit)

            result_str = f"{amount:.2f} {from_unit} is equal to {converted_quantity.magnitude:.2f} {to_unit}"
            self.result_var.set(result_str)
        except Exception as e:
            self.result_var.set(f"Error: {e}")

    def get_unit_list(self):
        ureg = UnitRegistry()
        return [str(unit) for unit in ureg]

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
