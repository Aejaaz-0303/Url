import pyshorteners
import tkinter as tk
from tkinter import ttk

def shorturl():
    url = entry.get()
    urlobj = pyshorteners.Shortener()
    short_url = urlobj.tinyurl.short(url)
    result_label.config(text=f"Shortened URL: {short_url}")

def copy_to_clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))

root = tk.Tk()
root.title("URL Shortener")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Enter the URL you want to shorten:").grid(column=0, row=0, padx=5, pady=5)
entry = ttk.Entry(frm, width=50)
entry.grid(column=1, row=0, padx=5, pady=5)

ttk.Button(frm, text="Shorten URL", command=shorturl).grid(column=0, row=1, padx=5, pady=5)
result_label = ttk.Label(frm, text="", wraplength=300)
result_label.grid(column=1, row=1, padx=5, pady=5)

result_label.bind("<Button-1>", copy_to_clipboard)


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2, columnspan=2, pady=5)



root.mainloop()
