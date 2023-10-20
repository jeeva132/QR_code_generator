import pyqrcode
from tkinter import *
from PIL import Image, ImageTk

def generate_qr_code():
    data = text_entry.get()
    name = name_entry.get()

    if data and name:
        qr = pyqrcode.create(data, error='L') 
        qr.png(f"{name}.png", scale=5)
        qr_code_image = Image.open(f"{name}.png")
        qr_code_photo = ImageTk.PhotoImage(qr_code_image)

        qr_code_canvas.create_image(125, 87, anchor=CENTER, image=qr_code_photo)
        qr_code_canvas.image = qr_code_photo
    else:
        info_label.config(text="Please enter both data and name.")

root = Tk()
root.title("QR Generator")

frame = Frame(root, bg="green")
frame.pack(expand=True, fill="both")

info_label = Label(frame, text="", font=("Arial", 15), bg="green", fg="white")
info_label.pack(pady=10)

text_label = Label(frame, text="Enter the text/URL:", font=("Arial", 13), bg="green", fg="white")
text_label.pack(pady=10)
text_entry = Entry(frame, font=("Arial", 12))
text_entry.pack(pady=10)

name_label = Label(frame, text="Enter the name of the QR Code:", font=("Arial", 13), bg="green", fg="white")
name_label.pack(pady=10)
name_entry = Entry(frame, font=("Arial", 12))
name_entry.pack(pady=10)

generate_button = Button(frame, text="Generate Code", font=("Arial", 15), command=generate_qr_code)
generate_button.pack(pady=10)

qr_code_canvas = Canvas(frame, relief=RIDGE, bd=2, bg="green")
qr_code_canvas.pack(pady=10)

root.geometry("600x600")
root.mainloop()
