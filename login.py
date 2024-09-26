import tkinter as tk
from tkinter import messagebox

# User data (username and password)
users = {}

# Function to check if passwords match
def passwords_match(password, confirm_password):
    return password == confirm_password

def create_account():
    # Hide login interface
    title_label.pack_forget()
    username_label.pack_forget()
    username_entry.pack_forget()
    password_label.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()
    create_account_button.pack_forget()
    logout_button.pack_forget()

    # Show account creation interface
    name_frame.pack(pady=10)
    username_label_create.pack(pady=5)
    username_entry_create.pack(pady=5)
    id_label.pack(pady=5)
    id_entry.pack(pady=5)
    location_frame.pack(pady=10)
    password_label_create.pack(pady=5)
    password_entry_create.pack(pady=5)
    confirm_password_label.pack(pady=5)
    confirm_password_entry.pack(pady=5)
    confirm_create_account_button.pack(pady=10)
    back_button.pack(pady=10)

# Function to confirm account creation
def confirm_create_account():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    username = username_entry_create.get()
    id_ = id_entry.get()
    country = country_entry.get()
    city = city_entry.get()
    password = password_entry_create.get()
    confirm_password = confirm_password_entry.get()

    if not passwords_match(password, confirm_password):
        messagebox.showerror("Error", "Passwords do not match!")
    elif username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        users[username] = {
            'first_name': first_name,
            'last_name': last_name,
            'id': id_,
            'country': country,
            'city': city,
            'password': password
        }
        messagebox.showinfo("Success", "Account created successfully!")
        # Reset to login interface
        reset_login_interface()

# Function to reset to the login interface
def reset_login_interface():
    # Show login elements
    title_label.pack(pady=20)
    username_label.pack(pady=5)
    username_entry.pack(pady=5)
    password_label.pack(pady=5)
    password_entry.pack(pady=5)
    login_button.pack(pady=10)
    create_account_button.pack(pady=10)
    logout_button.pack(pady=10)

    # Hide account creation elements
    name_frame.pack_forget()
    username_label_create.pack_forget()
    username_entry_create.pack_forget()
    id_label.pack_forget()
    id_entry.pack_forget()
    location_frame.pack_forget()
    password_label_create.pack_forget()
    password_entry_create.pack_forget()
    confirm_password_label.pack_forget()
    confirm_password_entry.pack_forget()
    confirm_create_account_button.pack_forget()
    back_button.pack_forget()

# Function to log in
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username]['password'] == password:
        messagebox.showinfo("Success", f"Welcome, {users[username]['first_name']}!")
        login_success()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Function to show success screen after login
def login_success():
    success_window = tk.Toplevel(root)
    success_window.title("Welcome")
    success_window.geometry("300x200")
    success_window.config(bg="#f0f0f0")

    tk.Label(success_window, text="Login Successful!", font=("Arial", 18), bg="#f0f0f0").pack(pady=20)

    def go_back():
        success_window.destroy()

    tk.Button(success_window, text="Back", font=("Arial", 12), width=10, bg="#2196F3", fg="white", command=go_back).pack(pady=20)

# Function to log out
def logout():
    if messagebox.askyesno("Logout", "Are you sure you want to log out?"):
        root.quit()

# Main application window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("600x400")  # Size suitable for computer
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Inventory Management System", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Login elements
username_label = tk.Label(root, text="Username:", font=("Arial", 12), bg="#f0f0f0")
username_label.pack(pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:", font=("Arial", 12), bg="#f0f0f0")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", font=("Arial", 12), width=20, bg="#2196F3", fg="white", command=login)
login_button.pack(pady=10)

# Create account button
create_account_button = tk.Button(root, text="Create Account", font=("Arial", 12), width=20, bg="#4CAF50", fg="white", command=create_account)
create_account_button.pack(pady=10)

# Logout button
logout_button = tk.Button(root, text="Logout", font=("Arial", 12), width=20, bg="#f44336", fg="white", command=logout)
logout_button.pack(pady=10)

# Description label
description_label = tk.Label(root, text="This is an Inventory Management System", font=("Arial", 10), bg="#f0f0f0")
description_label.pack(side="bottom", pady=20)

# Create account interface
name_frame = tk.Frame(root, bg="#f0f0f0")

tk.Label(name_frame, text="First Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5)
first_name_entry = tk.Entry(name_frame, width=15)
first_name_entry.grid(row=0, column=1, padx=5)

tk.Label(name_frame, text="Last Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=2, padx=5)
last_name_entry = tk.Entry(name_frame, width=15)
last_name_entry.grid(row=0, column=3, padx=5)

username_label_create = tk.Label(root, text="Username:", font=("Arial", 12), bg="#f0f0f0")
username_entry_create = tk.Entry(root, width=30)

id_label = tk.Label(root, text="ID:", font=("Arial", 12), bg="#f0f0f0")
id_entry = tk.Entry(root, width=30)

location_frame = tk.Frame(root, bg="#f0f0f0")
tk.Label(location_frame, text="Country:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5)
country_entry = tk.Entry(location_frame, width=15)
country_entry.grid(row=0, column=1, padx=5)

tk.Label(location_frame, text="City:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=2, padx=5)
city_entry = tk.Entry(location_frame, width=15)
city_entry.grid(row=0, column=3, padx=5)

password_label_create = tk.Label(root, text="Password:", font=("Arial", 12), bg="#f0f0f0")
password_entry_create = tk.Entry(root, show="*", width=30)

confirm_password_label = tk.Label(root, text="Confirm Password:", font=("Arial", 12), bg="#f0f0f0")
confirm_password_entry = tk.Entry(root, show="*", width=30)

confirm_create_account_button = tk.Button(root, text="Create Account", font=("Arial", 12), width=20, bg="#4CAF50", fg="white", command=confirm_create_account)
back_button = tk.Button(root, text="Back", font=("Arial", 12), width=20, bg="#FFC107", fg="black", command=reset_login_interface)

# Run the application
root.mainloop()


















