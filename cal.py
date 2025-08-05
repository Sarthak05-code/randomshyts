import tkinter as tk
from tkinter import messagebox
import json, os, hashlib, re

user_file = "file.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.isfile(user_file):
        try:
            with open(user_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_users(users):
    with open(user_file, "w") as f:
        json.dump(users, f, indent=4)

# ---------------- Register ----------------
def register_user(email, password, confirm_password, frame, switch_to_login):
    pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    email = email.get().strip()
    password = password.get()
    confirm = confirm_password.get()

    if not email or not password or not confirm:
        messagebox.showerror("Error", "All fields are required")
        return
    if not re.match(pattern, email):
        messagebox.showerror("Error", "Invalid Gmail address")
        return
    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters")
        return
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match")
        return

    users = load_users()
    if any(user["username"] == email for user in users):
        messagebox.showerror("Error", "Email already registered")
        return

    users.append({"username": email, "password": hash_password(password)})
    save_users(users)
    messagebox.showinfo("Success", "Registration successful! You can now log in.")
    switch_to_login()

# ---------------- Login ----------------
def login_user(email, password, frame):
    email = email.get().strip()
    password = password.get()

    if not email or not password:
        messagebox.showerror("Error", "Both fields are required")
        return

    users = load_users()
    for user in users:
        if user["username"] == email and user["password"] == hash_password(password):
            messagebox.showinfo("Success", f"Welcome back, {email}!")
            return

    messagebox.showerror("Error", "Invalid credentials")

# ---------------- Show/Hide Password ----------------
def toggle_password(entry, var):
    entry.config(show="" if var.get() else "*")

# ---------------- Register UI ----------------
def register_ui(root):
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root, bg="#333333")
    frame.pack()

    tk.Label(frame, text="Sign Up", font=("Arial", 25), bg="#333333", fg="white").grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(frame, text="Email", font=("Arial", 15), bg="#333333", fg="white").grid(row=1, column=0, sticky="e", padx=10)
    email_entry = tk.Entry(frame, bg="#555555", fg="white", insertbackground="white")
    email_entry.grid(row=1, column=1, pady=10)

    tk.Label(frame, text="Password", font=("Arial", 15), bg="#333333", fg="white").grid(row=2, column=0, sticky="e", padx=10)
    password_entry = tk.Entry(frame, show="*", bg="#555555", fg="white", insertbackground="white")
    password_entry.grid(row=2, column=1, pady=10)

    tk.Label(frame, text="Confirm Password", font=("Arial", 15), bg="#333333", fg="white").grid(row=3, column=0, sticky="e", padx=10)
    confirm_entry = tk.Entry(frame, show="*", bg="#555555", fg="white", insertbackground="white")
    confirm_entry.grid(row=3, column=1, pady=10)

    show_pass_var = tk.BooleanVar()
    show_check = tk.Checkbutton(frame, text="Show Password", variable=show_pass_var,
                                command=lambda: [toggle_password(password_entry, show_pass_var), toggle_password(confirm_entry, show_pass_var)],
                                bg="#333333", fg="white", selectcolor="#333333", activebackground="#333333")
    show_check.grid(row=4, column=1, sticky="w")

    signup_btn = tk.Button(frame, text="Register", bg="#555555", fg="white",
                           command=lambda: register_user(email_entry, password_entry, confirm_entry, frame, lambda: login_ui(root)))
    signup_btn.grid(row=5, column=0, columnspan=2, pady=20)

    switch_btn = tk.Button(frame, text="Already have an account? Sign In", bg="#333333", fg="cyan",
                           command=lambda: login_ui(root), borderwidth=0)
    switch_btn.grid(row=6, column=0, columnspan=2)

# ---------------- Login UI ----------------
def login_ui(root):
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root, bg="#333333")
    frame.pack()

    tk.Label(frame, text="Sign In", font=("Arial", 25), bg="#333333", fg="white").grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(frame, text="Email", font=("Arial", 15), bg="#333333", fg="white").grid(row=1, column=0, sticky="e", padx=10)
    email_entry = tk.Entry(frame, bg="#555555", fg="white", insertbackground="white")
    email_entry.grid(row=1, column=1, pady=10)

    tk.Label(frame, text="Password", font=("Arial", 15), bg="#333333", fg="white").grid(row=2, column=0, sticky="e", padx=10)
    password_entry = tk.Entry(frame, show="*", bg="#555555", fg="white", insertbackground="white")
    password_entry.grid(row=2, column=1, pady=10)

    show_pass_var = tk.BooleanVar()
    show_check = tk.Checkbutton(frame, text="Show Password", variable=show_pass_var,
                                command=lambda: toggle_password(password_entry, show_pass_var),
                                bg="#333333", fg="white", selectcolor="#333333", activebackground="#333333")
    show_check.grid(row=3, column=1, sticky="w")

    login_btn = tk.Button(frame, text="Login", bg="#555555", fg="white",
                          command=lambda: login_user(email_entry, password_entry, frame))
    login_btn.grid(row=4, column=0, columnspan=2, pady=20)

    switch_btn = tk.Button(frame, text="Don't have an account? Sign Up", bg="#333333", fg="cyan",
                           command=lambda: register_ui(root), borderwidth=0)
    switch_btn.grid(row=5, column=0, columnspan=2)

# ---------------- Main ----------------
def main():
    root = tk.Tk()
    root.title("User Auth System")
    root.geometry("370x480")
    root.config(bg="#333333")
    register_ui(root)
    root.mainloop()

main()
