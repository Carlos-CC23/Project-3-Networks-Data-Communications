import socket
import tkinter as tk
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 65432

def show_overview():
    overview = (
        "Special Encoding Scheme:\n"
        "- Takes an integer between -121 and 121 (non-zero)\n"
        "- Encodes it using coefficients of powers of 3: (81, 27, 9, 3, 1)\n"
        "- Coefficients can be -1, 0, or 1\n"
        "- Uses client-server socket communication\n"
        "- The server sends the encoded 5-element tuple back to the client"
    )
    messagebox.showinfo("Project Overview", overview)

def run_encoding():
    user_input = entry.get()
    try:
        number = int(user_input)
        if number == 0 or not -121 <= number <= 121:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a non-zero integer between -121 and 121.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.send(str(number).encode())
            data = s.recv(1024).decode()
            messagebox.showinfo("Encoded Result", f"Encoded tuple from server: {data}")
    except ConnectionRefusedError:
        messagebox.showerror("Connection Error", "Could not connect to the server.\nIs it running?")

def exit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Special Encoding Scheme Client")
root.geometry("400x200")

label = tk.Label(root, text="Enter an integer (-121 to 121, excluding 0):")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack()

btn_overview = tk.Button(root, text="Overview", width=20, command=show_overview)
btn_overview.pack(pady=5)

btn_run = tk.Button(root, text="Run Program", width=20, command=run_encoding)
btn_run.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", width=20, command=exit_app)
btn_exit.pack(pady=5)

root.mainloop()
