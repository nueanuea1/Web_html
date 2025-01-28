import qrcode

data = 'http://127.0.0.1:5500/chompu.html'
qr = qrcode.QRCode(version = 1, box_size= 10, border=5)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save('chompu.png')