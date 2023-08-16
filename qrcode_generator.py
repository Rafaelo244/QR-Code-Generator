import tkinter as tk
import qrcode
from PIL import ImageTk


class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator by Raph")
        self.root.geometry("500x500")

        self.label = tk.Label(root, text="Enter text:", font="Arial, 10")
        self.label.pack()

        self.text_entry = tk.Entry(root, width=60)
        self.text_entry.pack()

        self.generate_button = tk.Button(root, text="Generate QR Code", font="Arial, 15", width=20, height=1,
                                         command=self.generate_qr_code)
        self.generate_button.pack()

        self.qr_code_image_label = tk.Label(root)
        self.qr_code_image_label.pack()

    def generate_qr_code(self):
        text = self.text_entry.get()
        qr = qrcode.QRCode(
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        qr_code_img = qr.make_image(fill_color="black", back_color="white")

        qr_code_img = ImageTk.PhotoImage(qr_code_img)
        self.qr_code_image_label.config(image=qr_code_img)
        self.qr_code_image_label.image = qr_code_img


if __name__ == "__main__":
    root = tk.Tk()
    QRCodeGeneratorApp(root)
    root.mainloop()
