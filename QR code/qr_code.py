import qrcode

url=input("Enter the URL: ").strip()
file=input("Enter the file name: ").strip()
qr=qrcode.QRCode(border=1,box_size=10,version=1)
qr.add_data(url)
image=qr.make_image(fill_color="black",back_color="white")
image.save(file+".png")
print("QR code generated and saved as",file+".png")