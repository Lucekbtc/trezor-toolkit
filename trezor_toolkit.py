import tkinter as tk
from tkinter import messagebox
import subprocess

def sd_protect(action: str):
    command = ["trezorctl", "device", "sd-protect", action]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        messagebox.showinfo("Success", f"SD protection '{action}' executed successfully:\n{result.stdout}")
    else:
        messagebox.showerror("Error", f"Failed to execute SD protection '{action}':\n{result.stderr}")

def set_passphrase(action: str):
    # action must be either "enable-passphrase" or "disable-passphrase"
    command = ["trezorctl", action]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        messagebox.showinfo("Success", f"Passphrase '{action}' executed successfully:\n{result.stdout}")
    else:
        messagebox.showerror("Error", f"Failed to execute passphrase '{action}':\n{result.stderr}")

root = tk.Tk()
root.title("Trezor Toolkit")

# SD Protection Buttons
btn_sd_on = tk.Button(root, text="Enable SD Protection", command=lambda: sd_protect("on"))
btn_sd_on.pack(padx=20, pady=10)

btn_sd_off = tk.Button(root, text="Disable SD Protection", command=lambda: sd_protect("off"))
btn_sd_off.pack(padx=20, pady=10)

btn_sd_refresh = tk.Button(root, text="Refresh SD Protection", command=lambda: sd_protect("refresh"))
btn_sd_refresh.pack(padx=20, pady=10)

# Passphrase Protection Buttons
btn_disable_passphrase = tk.Button(root, text="Disable Passphrase", command=lambda: set_passphrase("disable-passphrase"))
btn_disable_passphrase.pack(padx=20, pady=10)

btn_enable_passphrase = tk.Button(root, text="Enable Passphrase", command=lambda: set_passphrase("enable-passphrase"))
btn_enable_passphrase.pack(padx=20, pady=10)

root.mainloop()
