import qrcode

# ข้อมูลที่ต้องการใส่ใน QR Code
data = 'for u'

# สร้าง QR Code
img = qrcode.make(data)

# บันทึกภาพเป็นไฟล์ PNG
img.save('u.png')

print("QR Code saved as u.png")
