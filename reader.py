import qrcode
from tkinter import *
from tkinter import messagebox
from functools import partial

def main():
    root = Tk()
    root.title('QR Code Creator')
    frame = Frame(root, padx=10, pady=10)
    frame.grid()

    link = StringVar()

    Label(frame, text='Link:').grid(column=0, row=0, pady=5)
    Entry(frame, width=30, textvariable=link).grid(column=1, row=0, pady=5)
    Button(frame, text='Create and Save QR Code', command=partial(create_code, link, 'QRCode')).grid(column=0, row=1, pady=5, columnspan=2, sticky='NEWSW')
    Button(frame, text='Quit', command=root.destroy).grid(column=0, row=2, columnspan=2, sticky='NEWSW')

    root.mainloop()
    
def create_code(link, name):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=15,
        border=5
    )

    qr.add_data(link.get())
    qr.make(fit=True)

    final = qr.make_image(fill_color='black', back_color='white')
    
    final.save(f'{name}.png')
    messagebox.showinfo('QR code saved!', f'Qr code was saved as: {name}.png')

if __name__ == '__main__':
    main()