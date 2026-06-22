import tkinter as tk
from tkinter import messagebox

def read_file():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users

def write_file(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

def login():
    username = entry_username.get()
    password = entry_password.get()
    users = read_file()
    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

def signup():
    username = entry_username.get()
    password = entry_password.get()
    users = read_file()
    if username in users:
        messagebox.showerror("Signup", "Username already exists")
    else:
        write_file(username, password)
        messagebox.showinfo("Signup", "Account Created Successfully")

def main():
    global entry_username, entry_password
    tk.Label(root, text="Username").pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)
    tk.Label(root, text="Password").pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)
    tk.Button(root, text="Login", command=login).pack(pady=5)
    tk.Button(root, text="Signup", command=signup).pack(pady=5)

root = tk.Tk()
root.title("Login System")
root.geometry("300x250")
main()
root.mainloop()