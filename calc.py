from tkinter import *
from tkinter import messagebox, filedialog
import os

main = Tk()
main.title("BudgetCalc")
ttle = Label(main, text="BudgetCalc", font=("Copperplate Gothic Bold", 25))

def ganpati():
    root = Toplevel
    root.title("BudgetCalc")
    root.geometry("1920x1080")
    root.resizable(width=False, height=False)
    title = Label(root, text="BudgetCalc", font=("Copperplate Gothic Bold", 25))
    title.pack()
    expenses = []
    minval = 0
    total = 0
    maxval = 0
    messagebox.showinfo("BudgetCalc Info", "It is suggested to put this window into fullscreen mode.")
    decoration_cost_label = Label(root, text="Budget for Sports")
    decoration_cost_label.pack(pady=10, padx=10)
    decoration_cost_entry = Entry(root)
    decoration_cost_entry.pack(pady=10, padx=10)
    ganpati_idol_label = Label(root, text="Budget for Food")
    ganpati_idol_label.pack(pady=10, padx=10)
    ganpati_idol_entry = Entry(root)
    ganpati_idol_entry.pack(pady=10, padx=10)
    lighting_cost_label = Label(root, text="Lighting Cost")
    lighting_cost_label.pack(pady=10, padx=10)
    lighting_cost_entry = Entry(root)
    lighting_cost_entry.pack(pady=10, padx=10)
    food_label = Label(root, text="Food Cost")
    food_label.pack(pady=10, padx=10)
    food_entry = Entry(root)
    food_entry.pack(pady=10, padx=10)
    refreshment_label = Label(root, text="Refreshment Cost")
    refreshment_label.pack(pady=10, padx=10)
    refreshment_entry = Entry(root)
    refreshment_entry.pack(pady=10, padx=10)
    output = Text(root)
    output.pack()
    def submit():
        global expenses
        global output
        global minval
        global maxval
        global total
        dce = int(decoration_cost_entry.get())
        gil = int(ganpati_idol_entry.get())
        lcl = int(lighting_cost_entry.get())
        fe = int(food_entry.get())
        re = int(refreshment_entry.get())
        expenses.append(dce)
        expenses.append(gil)
        expenses.append(lcl)
        expenses.append(fe)
        expenses.append(re)
        maxval = max(expenses)
        minval = min(expenses)
        error_max_value = 25000
        print(expenses)
        total = sum(expenses)
        if total < error_max_value:
            messagebox.showinfo("Success", str(f"Total Expenses {str(total)}"))
            output.insert(END, str(f"\nTotal Expenses {str(total)}"))
            output.insert(END, f"\nPeak Expense Value {str(maxval)}")
            output.insert(END, f"\nMinimum Expense Value {str(minval)}")
            def reset_var_values():
                expenses.clear()
                minval = 0
                maxval = 0
                total = 0
            reset_var_values()
        else:
            messagebox.showerror("Error", str(f"Total Expenses:{total} is greater than the max value: {error_max_value}"))
            def reset_var_values():
                expenses.clear()
                minval = 0
                maxval = 0
                total = 0
            reset_var_values()
    Button(root, text="Submit", command=submit).pack(pady=10, padx=10)

Button(main, text="India - Ganpati-Festival Budget Calculator")
main.mainloop()