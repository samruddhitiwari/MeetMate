# gui.py
import tkinter as tk
from tkinter import messagebox
from meeting_handler import handle_meeting

def on_submit():
    link = entry.get()
    if link:
        handle_meeting(link)
        messagebox.showinfo("Success", "Meeting processed successfully!")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a meeting link.")

root = tk.Tk()
root.title("Meeting Assistant")
root.geometry("500x150")

label = tk.Label(root, text="Enter Meeting Link:")
label.pack(pady=5)

entry = tk.Entry(root, width=60)
entry.pack(pady=5)

submit_btn = tk.Button(root, text="Start & Process Meeting", command=on_submit)
submit_btn.pack(pady=10)

root.mainloop()
