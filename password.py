import re
import random
import string
import getpass
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    points = 0
    
    if len(password) >= 8:
        points += 1
        
    if re.search(r'[A-Z]', password):
        points += 1
    
    if re.search(r'[a-z]', password):
        points += 1
    
    if re.search(r'[0-9]', password):
        points += 1
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        points += 1
        
    if points <= 2:
        return "Weak"   
    elif points == 3:
        return "Moderate"
    else:
        return "Strong"
    
def suggestPassword():
    characters = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
    return ''.join(random.choice(characters) for _ in range(12))
      

def checkStrength():
    password = entry.get()
    strength = check_password_strength(password)
    
    result_label.pack(pady=5)
    suggestion_label.pack()
    
    if strength == "Weak":
        result_label.config(text="🔴 Weak Password", fg="red")
        suggestion_label.config(text=f"💡 Try: {suggestPassword()}")
    elif strength == "Medium":
        result_label.config(text="🟡 Medium Password", fg="orange")
        suggestion_label.config(text=f"💡 Improve: {suggestPassword()}")
    else:
        result_label.config(text="🟢 Strong Password 💪", fg="green")
        suggestion_label.config(text="✅ Good to go!")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="#ffffff")

tk.Label(root, text="🔐 Password Strength Checker",
         font=("Segoe UI Emoji", 16, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=15)

entry = tk.Entry(root, show="*", font=("Segoe UI", 12), width=30)
entry.pack(pady=10)

tk.Button(root, text="Check Strength",
          font=("Segoe UI", 11, "bold"),
          bg="#007acc", fg="white",
          command=checkStrength).pack(pady=10)


result_label = tk.Label(root, text="",
                        font=("Segoe UI Emoji", 12, "bold"),
                        bg="#1e1e1e")
result_label.pack(pady=5)
result_label.pack_forget()

suggestion_label = tk.Label(root, text="",
                           font=("Segoe UI Emoji", 10),
                           bg="#1e1e1e", fg="lightgray")
suggestion_label.pack()
suggestion_label.pack_forget()

root.mainloop()