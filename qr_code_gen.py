import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import qrcode

# Function to generate QR code
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some text or URL!")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert PIL image to ImageTk format
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep a reference

#clear entry and QR code
def clear_entry():
    entry.delete(0, tk.END)
    qr_label.config(image='')
    qr_label.image = None

# Create main window
root = tk.Tk()
root.title("QR Code URL Generator")
root.geometry("300x400")

# Input field
tk.Label(root, text="Enter URL to make QR Code:").pack(pady=20)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Buttons
tk.Button(root, text="Click to make QR Code", command=generate_qr).pack(pady=10)
tk.Button(root, text="Clear Entry", command=clear_entry).pack(pady=5)

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()




