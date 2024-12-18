import tkinter as tk

from tkinter import ttk

root = tk.Tk()
root.title("My Levelling")
root.geometry("300x200")

my_tree = ttk.Treeview(root)
my_tree["columns"] = ('Backsight','Intersight','Foresight','Rise/Fall',)

my_tree.column('#0',width=120,minwidth=25)
for i in my_tree['columns']:
    my_tree.column(i,width=120,anchor='w')

my_tree.heading('#0',text="ID",anchor='w')
my_tree.heading('Backsight',text='Backsight',anchor='w')
my_tree.heading('Intersight',text='Intersight',anchor='w')
my_tree.heading('Foresight',text='Foresight',anchor='w')
my_tree.heading('Rise/Fall',text='Rise/Fall',anchor='w')

my_tree.pack(pady=20)

my_tree.column('#0',width=120,minwidth=25)

root.mainloop()