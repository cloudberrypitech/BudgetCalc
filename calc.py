from tkinter import *
from tkinter import messagebox

main = Tk()
main.title("BudgetCalc v1.0")
main.geometry("500x500")

ttle = Label(main, text="BudgetCalc", font=("Copperplate Gothic Bold", 25))
ttle.pack()

def public_event():
    main.withdraw()

    root = Toplevel(main)
    root.title("BudgetCalc")
    root.geometry("500x500")
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

    output_frame = Frame(root)
    output_frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

    scrollbar = Scrollbar(output_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    output = Text(
        output_frame,
        height=10,
        width=50,
        yscrollcommand=scrollbar.set
    )
    output.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=output.yview)

    def submit():
        try:
            dce = int(decoration_cost_entry.get())
            gil = int(ganpati_idol_entry.get())
            lcl = int(lighting_cost_entry.get())
            fe = int(food_entry.get())
            re = int(refreshment_entry.get())
        except ValueError:
            messagebox.showerror(
                "Error",
                "Please enter valid numbers only."
            )
            return

        expenses.clear()
        expenses.extend([dce, gil, lcl, fe, re])

        maxval = max(expenses)
        minval = min(expenses)
        total = sum(expenses)
        max_allowed = 25000

        if total < max_allowed:
            messagebox.showinfo(
                "Success",
                f"Total Expenses {total}"
            )

            output.insert(END, f"\nTotal Expenses {total}")
            output.insert(END, f"\nPeak Expense Value {maxval}")
            output.insert(END, f"\nMinimum Expense Value {minval}")
            output.see(END)

            expenses.clear()

        else:
            messagebox.showerror(
                "Error",
                f"Total Expenses: {total} is greater than the max value: {max_allowed}"
            )

            expenses.clear()

    Button(root, text="Submit", command=submit).pack(pady=10, padx=10)

Button(
    main,
    text="Public Event Budget Calculator",
    command=public_event
).pack()

main.mainloop()