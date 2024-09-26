import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from collections import defaultdict
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def on_enter(e):
    e.widget['background'] = '#003d7a'  
    e.widget['foreground'] = 'white'
    e.widget['borderwidth'] = 2
    e.widget['relief'] = 'raised'

def on_leave(e):
    e.widget['background'] = e.widget.original_bg
    e.widget['foreground'] = 'white'
    e.widget['borderwidth'] = 1
    e.widget['relief'] = 'flat'

class CreateToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text, background="#333", fg="#fff", relief="solid", borderwidth=1, font=("Arial", 10))
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
        self.tooltip = None

def show_frame(frame, title):
    # Hide all frames
    for widget in content_frame.winfo_children():
        widget.pack_forget()
    # Show the requested frame
    frame.pack(fill='both', expand=True)
    # Update the title
    title_label.config(text=title)

data = []  # Initialize the global data list

def add_item():
    def save_item():
        name = name_entry.get()
        prix = prix_entry.get()
        quantity = quantity_entry.get()
        category = category_combo.get()
        date = date_entry.get_date()
        unit = unit_combo.get()

        # Add the item to the global data list
        data.append((name, "Add", date.strftime("%d/%m/%Y"), prix, quantity))

        print(f"Saved: {name}, {prix}, {quantity}, {category}, {date}, {unit}")
        messagebox.showinfo("Info", "Item added successfully!")
        add_frame.pack_forget()
        view_items()  # Refresh the view to show the new item

    def cancel_item():
        add_frame.pack_forget()
        show_frame(operations_frame, "Operations")

    def on_enter(event):
        event.widget.config(bg="darkgreen")  # Change to a darker green on hover for Save button
        event.widget.config(fg="white")

    def on_leave(event):
        event.widget.config(bg=event.widget.original_bg)  # Restore original background color
        event.widget.config(fg="white")

    global add_frame
    add_frame = tk.Frame(content_frame, bg="#ffffff", padx=20, pady=20, bd=2, relief="flat")
    add_frame.place(relx=0.5, rely=0.5, anchor='center')

    label_font = ('Arial', 12, 'bold')
    entry_font = ('Arial', 12)
    entry_bg = "#f0f0f0"
    button_font = ('Arial', 12, 'bold')
    button_height = 2

    # title
    title_label = tk.Label(add_frame, text="Add New Item", bg="#ffffff", font=("Arial", 18, 'bold'))
    title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    # Row 1: Name & Category
    tk.Label(add_frame, text="Name:", bg="#ffffff", font=label_font).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    name_entry = tk.Entry(add_frame, font=entry_font, width=30, bg=entry_bg, bd=1, relief="solid")
    name_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    tk.Label(add_frame, text="Category:", bg="#ffffff", font=label_font).grid(row=1, column=4, padx=10, pady=10, sticky="e")
    category_combo = ttk.Combobox(add_frame, values=["Food", "Electronic", "Toys", "Clothes"], font=entry_font, width=25)
    category_combo.grid(row=1, column=5, padx=10, pady=10)
    category_combo.current(0)

    # Row 2: Quantity & Unit
    tk.Label(add_frame, text="Quantity:", bg="#ffffff", font=label_font).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    quantity_entry = tk.Entry(add_frame, font=entry_font, width=30, bg=entry_bg, bd=1, relief="solid")
    quantity_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

    tk.Label(add_frame, text="Unit:", bg="#ffffff", font=label_font).grid(row=2, column=4, padx=10, pady=10, sticky="e")
    unit_combo = ttk.Combobox(add_frame, values=["Piece", "Kg", "L"], font=entry_font, width=25)
    unit_combo.grid(row=2, column=5, padx=10, pady=10)
    unit_combo.current(0)

    # Row 3: Prix & Date
    tk.Label(add_frame, text="Prix:", bg="#ffffff", font=label_font).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    prix_entry = tk.Entry(add_frame, font=entry_font, width=30, bg=entry_bg, bd=1, relief="solid")
    prix_entry.grid(row=3, column=1, padx=10, pady=10, columnspan=3)

    tk.Label(add_frame, text="Date:", bg="#ffffff", font=label_font).grid(row=3, column=4, padx=10, pady=10, sticky="e")
    date_entry = DateEntry(add_frame, width=28, background="lightblue", foreground="black", borderwidth=1, font=entry_font)
    date_entry.grid(row=3, column=5, padx=10, pady=10)

    # Row 4: Buttons (Save & Cancel)
    save_button = tk.Button(add_frame, text="Save", command=save_item, bg="#28a745", fg="white", font=button_font, width=15, height=button_height, relief="flat")
    save_button.original_bg = "#28a745"
    save_button.grid(row=4, column=2, padx=10, pady=20)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

    cancel_button = tk.Button(add_frame, text="Cancel", command=cancel_item, bg="#dc3545", fg="white", font=button_font, width=15, height=button_height, relief="flat")
    cancel_button.original_bg = "#dc3545"
    cancel_button.grid(row=4, column=3, padx=10, pady=20)
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    advice_label = tk.Label(add_frame, text="Fill in all details and click Save to add the item. Click Cancel to discard changes.", bg="#ffffff", font=("Arial", 10), wraplength=400)
    advice_label.grid(row=5, column=0, columnspan=6, padx=10, pady=10)

    add_frame.grid_columnconfigure(0, weight=1)
    add_frame.grid_columnconfigure(1, weight=2)
    add_frame.grid_columnconfigure(2, weight=2)
    add_frame.grid_columnconfigure(3, weight=2)
    add_frame.grid_columnconfigure(4, weight=1)
    add_frame.grid_columnconfigure(5, weight=2)

    show_frame(add_frame, "Add Item")

def sales_item():
    def save_item():
        name = name_entry.get()
        prix = prix_entry.get()
        quantity = quantity_entry.get()
        category = category_combo.get()
        date = date_entry.get_date()
        unit = unit_combo.get()

        # Add the item to the global data list
        data.append((name, "Sales", date.strftime("%d/%m/%Y"), prix, quantity))

        print(f"Saved: {name}, {prix}, {quantity}, {category}, {date}, {unit}")
        messagebox.showinfo("Info", "Item sold successfully!")
        sales_frame.pack_forget()
        view_items()  # Refresh the view to show the new sale

    def cancel_item():
        sales_frame.pack_forget()
        show_frame(operations_frame, "Operations")

    def on_enter(event):
        event.widget.config(bg="darkgreen")  # Change to a darker green on hover for Save button
        event.widget.config(fg="white")

    def on_leave(event):
        event.widget.config(bg=event.widget.original_bg)  # Restore original background color
        event.widget.config(fg="white")

    global sales_frame
    sales_frame = tk.Frame(content_frame, bg="#ffffff", padx=20, pady=20, bd=2, relief="flat")
    sales_frame.place(relx=0.5, rely=0.5, anchor='center')

    label_font = ('Arial', 12, 'bold')
    entry_font = ('Arial', 12)
    entry_bg = "#f0f0f0"
    button_font = ('Arial', 12, 'bold')
    button_height = 2

    # title
    title_label = tk.Label(sales_frame, text="Sales", bg="#ffffff", font=("Arial", 18, 'bold'))
    title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    # Row 1: Name & Category
    tk.Label(sales_frame, text="Name:", bg="#ffffff", font=label_font).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    name_entry = tk.Entry(sales_frame, font=entry_font, width=30, bg=entry_bg, bd=1, relief="solid")
    name_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    tk.Label(sales_frame, text="Category:", bg="#ffffff", font=label_font).grid(row=1, column=4, padx=10, pady=10, sticky="e")
    category_combo = ttk.Combobox(sales_frame, values=["Food", "Electronic", "Toys", "Clothes"], font=entry_font, width=25)
    category_combo.grid(row=1, column=5, padx=10, pady=10)
    category_combo.current(0)

    # Row 2: Quantity & Unit
    tk.Label(sales_frame, text="Quantity:", bg="#ffffff", font=label_font).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    quantity_entry = tk.Entry(sales_frame, font=entry_font, width=30, bg=entry_bg, bd=1, relief="solid")
    quantity_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

    tk.Label(sales_frame, text="Unit:", bg="#ffffff", font=label_font).grid(row=2, column=4, padx=10, pady=10, sticky="e")
    unit_combo = ttk.Combobox(sales_frame, values=["Piece", "Kg", "L"], font=entry_font, width=25)
    unit_combo.grid(row=2, column=5, padx=10, pady=10)
    unit_combo.current(0)

    # Row 3: Prix & Date
    tk.Label(sales_frame, text="Prix:", bg="#ffffff", font=label_font).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    prix_entry = tk.Entry(sales_frame, font=entry_font, width=30, bg=entry_bg, bd=1, relief="solid")
    prix_entry.grid(row=3, column=1, padx=10, pady=10, columnspan=3)

    tk.Label(sales_frame, text="Date:", bg="#ffffff", font=label_font).grid(row=3, column=4, padx=10, pady=10, sticky="e")
    date_entry = DateEntry(sales_frame, width=28, background="lightblue", foreground="black", borderwidth=1, font=entry_font)
    date_entry.grid(row=3, column=5, padx=10, pady=10)

    # Row 4: Buttons (Save & Cancel)
    save_button = tk.Button(sales_frame, text="Save", command=save_item, bg="#28a745", fg="white", font=button_font, width=15, height=button_height, relief="flat")
    save_button.original_bg = "#28a745"
    save_button.grid(row=4, column=2, padx=10, pady=20)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)

    cancel_button = tk.Button(sales_frame, text="Cancel", command=cancel_item, bg="#dc3545", fg="white", font=button_font, width=15, height=button_height, relief="flat")
    cancel_button.original_bg = "#dc3545"
    cancel_button.grid(row=4, column=3, padx=10, pady=20)
    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    advice_label = tk.Label(sales_frame, text="Fill in all details and click Save to register the sale. Click Cancel to discard changes.", bg="#ffffff", font=("Arial", 10), wraplength=400)
    advice_label.grid(row=5, column=0, columnspan=6, padx=10, pady=10)

    sales_frame.grid_columnconfigure(0, weight=1)
    sales_frame.grid_columnconfigure(1, weight=2)
    sales_frame.grid_columnconfigure(2, weight=2)
    sales_frame.grid_columnconfigure(3, weight=2)
    sales_frame.grid_columnconfigure(4, weight=1)
    sales_frame.grid_columnconfigure(5, weight=2)

    show_frame(sales_frame, "Sales")

def view_items():
    def filter_data():
        search_term = search_entry.get().lower()
        selected_type = type_var.get()
        selected_month = month_var.get()
        selected_year = year_var.get()

        filtered_data = []

        for item in data:
            name, type_, date, prix, quantity = item
            date_obj = datetime.strptime(date, "%d/%m/%Y")
            item_month = date_obj.month
            item_year = date_obj.year

            if (selected_type in [type_, "All"] and
                (selected_month == "" or selected_month == str(item_month)) and
                (selected_year == "" or selected_year == str(item_year)) and
                (search_term in name.lower() or search_term == "")):

                filtered_data.append(item)

        update_table(filtered_data)

    def update_table(data_to_display):
        for row in tree.get_children():
            tree.delete(row)

        cumulative_sum = 0
        cum_croissant = 0
        for item in data_to_display:
            name, type_, date, prix, quantity = item
            amount = float(prix) * float(quantity)
            if type_ == "Add":
                amount = -amount
            cum_croissant += amount
            cumulative_sum += cum_croissant
            tree.insert("", tk.END, values=(name, type_, date, prix, quantity, amount, cum_croissant))

        # Update cumulative totals
        total_cumulative_label.config(text=f"Total Cumulative: {cumulative_sum:.2f}")

    def delete_selected():
        selected_item = tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this item?")
            if confirm:
                item_values = tree.item(selected_item, 'values')
                # Remove the item from data list
                for i, item in enumerate(data):
                    if item[0] == item_values[0] and item[2] == item_values[2]:
                        data.pop(i)  # Remove item from data list
                        break
                # Remove from treeview
                tree.delete(selected_item)
                messagebox.showinfo("Info", "Item deleted successfully!")

    def edit_selected():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to edit!")
            return

        item = tree.item(selected_item, 'values')

        # Open edit window
        edit_window = tk.Toplevel(view_frame)
        edit_window.title("Edit Item")

        # Fields for editing
        tk.Label(edit_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        name_entry.insert(0, item[0])

        tk.Label(edit_window, text="Date (dd/mm/yyyy):").grid(row=1, column=0, padx=10, pady=5)
        date_entry = tk.Entry(edit_window)
        date_entry.grid(row=1, column=1, padx=10, pady=5)
        date_entry.insert(0, item[2])

        tk.Label(edit_window, text="Prix:").grid(row=2, column=0, padx=10, pady=5)
        prix_entry = tk.Entry(edit_window)
        prix_entry.grid(row=2, column=1, padx=10, pady=5)
        prix_entry.insert(0, item[3])

        tk.Label(edit_window, text="Quantity:").grid(row=3, column=0, padx=10, pady=5)
        quantity_entry = tk.Entry(edit_window)
        quantity_entry.grid(row=3, column=1, padx=10, pady=5)
        quantity_entry.insert(0, item[4])

        tk.Label(edit_window, text="Category:").grid(row=4, column=0, padx=10, pady=5)
        category_entry = tk.Entry(edit_window)
        category_entry.grid(row=4, column=1, padx=10, pady=5)
        category_entry.insert(0, item[1])

        # Save changes
        def save_changes():
            new_name = name_entry.get()
            new_date = date_entry.get()
            new_prix = prix_entry.get()
            new_quantity = quantity_entry.get()
            new_category = category_entry.get()

            # Update the item in the data list
            for i, data_item in enumerate(data):
                if data_item[0] == item[0] and data_item[2] == item[2]:
                    data[i] = (new_name, new_category, new_date, new_prix, new_quantity)
                    break

            # Update the treeview item
            tree.item(selected_item, values=(new_name, new_category, new_date, new_prix, new_quantity, item[5], item[6]))
            messagebox.showinfo("Info", "Item updated successfully!")
            edit_window.destroy()

        tk.Button(edit_window, text="Save", command=save_changes, bg="#007bff", fg="white", font=("Arial", 12, "bold")).grid(row=5, column=0, columnspan=2, pady=10)

    # Create view_frame
    global view_frame
    view_frame = tk.Frame(content_frame, bg="#f0f0f0")

    # Filter Frame (includes search, filter, delete, and edit buttons)
    filter_frame = tk.Frame(view_frame, bg="#ffffff", padx=10, pady=10)
    filter_frame.pack(fill=tk.X)

    # Search and Filter Inputs
    tk.Label(filter_frame, text="Search:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
    search_entry = tk.Entry(filter_frame, font=("Arial", 12))
    search_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(filter_frame, text="Type:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
    type_var = tk.StringVar(value="All")
    type_options = ttk.Combobox(filter_frame, textvariable=type_var, values=["All", "Add", "Remove"], font=("Arial", 12))
    type_options.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(filter_frame, text="Month:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=4, padx=5, pady=5, sticky="e")
    month_var = tk.StringVar(value="")
    month_options = ttk.Combobox(filter_frame, textvariable=month_var, values=["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], font=("Arial", 12))
    month_options.grid(row=0, column=5, padx=5, pady=5)

    tk.Label(filter_frame, text="Year:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=6, padx=5, pady=5, sticky="e")
    year_var = tk.StringVar(value="")
    year_options = ttk.Combobox(filter_frame, textvariable=year_var, values=[str(year) for year in range(2000, datetime.now().year + 1)], font=("Arial", 12))
    year_options.grid(row=0, column=7, padx=5, pady=5)

    # Filter button
    tk.Button(filter_frame, text="Filter", command=filter_data, bg="#007bff", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=8, padx=5, pady=5)

    # Delete and Edit buttons on the same row
    tk.Button(filter_frame, text="Delete", command=delete_selected, bg="#dc3545", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=9, padx=5, pady=5)
    tk.Button(filter_frame, text="Edit", command=edit_selected, bg="#ffc107", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=10, padx=5, pady=5)

    # Data Table
    table_frame = tk.Frame(view_frame, bg="#ffffff", padx=10, pady=10)
    table_frame.pack(fill=tk.BOTH, expand=True)

    columns = ("Name", "Type", "Date", "Prix", "Quantity", "Amount", "Cumulative")
    tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    # Scrollbars
    y_scroll = tk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=y_scroll.set)

    x_scroll = tk.Scrollbar(view_frame, orient=tk.HORIZONTAL, command=tree.xview)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
    tree.configure(xscrollcommand=x_scroll.set)

    # Cumulative Total Label
    total_cumulative_label = tk.Label(view_frame, text="Total Cumulative: 0.00", bg="#ffffff", font=("Arial", 12, "bold"))
    total_cumulative_label.pack(side=tk.BOTTOM, padx=10, pady=10, anchor="e")

    # Update table with the current data
    update_table(data)

    show_frame(view_frame, "View Items")

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def is_valid_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def draw_pie_chart(frame):
    high_count = sum(1 for item in data if is_valid_number(item[4]) and int(item[4]) > 2000)
    medium_count = sum(1 for item in data if is_valid_number(item[4]) and 1000 < int(item[4]) <= 2000)
    low_count = sum(1 for item in data if is_valid_number(item[4]) and int(item[4]) <= 1000)

    labels = ['High', 'Medium', 'Low']
    sizes = [high_count, medium_count, low_count]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal') 

    for widget in frame.winfo_children():
        widget.destroy()

    chart = FigureCanvasTkAgg(fig, master=frame)
    chart.draw()
    chart.get_tk_widget().pack(fill=tk.BOTH, expand=True)  

def update_report_table(tree):
    for row in tree.get_children():
        tree.delete(row)

    for item in data:
        name, category, _, _, quantity = item
        if is_valid_number(quantity):
            quantity = int(quantity)
            status = "High" if quantity > 2000 else "Medium" if quantity > 1000 else "Low"
            tree.insert("", tk.END, values=(name, category, quantity, status, "unit"))

def inventory_report():
    global report_frame
    report_frame = tk.Frame(content_frame, bg="#f0f0f0")
    report_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(report_frame, text="Inventory Report", bg="#f0f0f0", font=("Arial", 20, "bold")).pack(pady=20)

    table_frame = tk.Frame(report_frame, bg="#ffffff", padx=10, pady=10)
    table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    columns = ("Name", "Category", "Quantity", "Status", "Unit")
    report_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    report_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for col in columns:
        report_tree.heading(col, text=col)
        report_tree.column(col, anchor="center", width=100)

    style = ttk.Style()
    style.configure("Treeview", highlightthickness=0, bd=0, font=("Arial", 12))
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

    def on_enter(event):
        item = report_tree.identify_row(event.y)
        if item:
            report_tree.item(item, tags=("hover",))

    def on_leave(event):
        item = report_tree.identify_row(event.y)
        if item:
            report_tree.item(item, tags=(""))

    report_tree.tag_configure("hover", background="#e0e0e0")
    report_tree.bind("<Motion>", on_enter)
    report_tree.bind("<Leave>", on_leave)

    update_report_table(report_tree)

    chart_frame = tk.Frame(report_frame, bg="#ffffff", padx=10, pady=10)
    chart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    draw_pie_chart(chart_frame)

    show_frame(report_frame, "Inventory Report")



def settings():
    global settings_frame
    settings_frame = tk.Frame(content_frame, bg="#f0f0f0")

    tk.Label(settings_frame, text="Settings: Not Available", bg="#f0f0f0", font=("Arial", 16)).pack(pady=20)

    show_frame(settings_frame, "Settings")

def logout():
    root.quit()

root = tk.Tk()
root.title("Inventory Management System")
root.geometry("1024x768")
root.configure(bg="#f0f0f0") 

button_bg = "#007bff" 

buttons = [
    {"name": "Add", "color": "#28a745", "command": add_item, "tooltip": "Add new items to inventory"},
    {"name": "View", "color": "#007aff", "command": view_items, "tooltip": "View existing inventory"},
    {"name": "Sales", "color": "#dc3545", "command": sales_item, "tooltip": "Manage sales"},
    {"name": "Inventory Report", "color": "#17a2b8", "command": inventory_report, "tooltip": "View inventory reports"},
    {"name": "Settings", "color": "#ffc107", "command": settings, "tooltip": "Adjust application settings"},
    {"name": "Logout", "color": "#dc3545", "command": logout, "tooltip": "Log out of the system"}
]
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

style = ttk.Style()
style.configure('TNotebook', tabposition='n', background='#e3f2fd', padding=0)
style.configure('TNotebook.Tab', background='#b3e5fc', padding=[10, 5], font=('Arial', 12))
style.map('TNotebook.Tab', background=[('selected', '#81d4fa')], foreground=[('selected', '#000000')])

operations_tab = ttk.Frame(notebook)
notebook.add(operations_tab, text='Operations')

reports_tab = ttk.Frame(notebook)
notebook.add(reports_tab, text='Reports')

settings_tab = ttk.Frame(notebook)
notebook.add(settings_tab, text='Settings/Logout')

header_frame = tk.Frame(root, bg="#e3f2fd", height=50)
header_frame.pack(fill='x', side='bottom')

header_label = tk.Label(header_frame, text="Inventory Management System", bg="#e3f2fd", fg="#000000", font=("Arial", 20, 'bold'))
header_label.pack(pady=10)

button_frame_ops = tk.Frame(operations_tab, bg="#f0f0f0")
button_frame_ops.pack(fill=tk.X, pady=20)

button_frame_reports = tk.Frame(reports_tab, bg="#f0f0f0")
button_frame_reports.pack(fill=tk.X, pady=20)

button_frame_settings = tk.Frame(settings_tab, bg="#f0f0f0")
button_frame_settings.pack(fill=tk.X, pady=20)

for button in buttons:
    btn = tk.Button(
        button_frame_ops if button["name"] in ["Add", "View", "Delete", "Update", "Sales"] else
        button_frame_reports if button["name"] in ["Inventory Report", "Sales Report", "General Report"] else
        button_frame_settings,
        text=button["name"], 
        bg=button["color"], 
        fg="white", 
        width=20, 
        height=2,
        borderwidth=1,
        relief='flat',
        font=('Arial', 10, 'bold'),
        command=button["command"]
    )
    
    btn.original_bg = button["color"]
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    btn.pack(side=tk.LEFT, padx=10, pady=10)

    btn.configure(highlightbackground='#0056b3', highlightcolor='#0056b3', highlightthickness=1)

    CreateToolTip(btn, button["tooltip"])

content_frame = tk.Frame(root, bg="#f0f0f0")
content_frame.pack(fill='both', expand=True)

title_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 16, 'bold'))
title_label.pack(side=tk.BOTTOM, pady=10)

global operations_frame
operations_frame = tk.Frame(content_frame, bg="#f0f0f0")

root.mainloop()