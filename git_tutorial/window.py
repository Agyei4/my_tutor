import tkinter as tk
from tkinter import ttk

def add_row():
    tree.insert("", "end", values=[""] * len(columns))

def remove_row():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

app = tk.Tk()
app.title("Leveling Computation")

columns = ["Backsight", "Intersight", "Foresight", "Rise", "Fall", "Initial Reduced Level", "Adjustment", "Final Reduced Level", "Remarks"]
tree = ttk.Treeview(app, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

for _ in range(7):  # Adding 7 initial rows
    add_row()

tree.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(app)
frame.pack()

add_button = tk.Button(frame, text="Add Row", command=add_row)
add_button.grid(row=0, column=0)

remove_button = tk.Button(frame, text="Remove Selected Row", command=remove_row)
remove_button.grid(row=0, column=1)

calculate_button = tk.Button(app, text="Calculate", )#command = calculate level
calculate_button.pack()

app.mainloop()