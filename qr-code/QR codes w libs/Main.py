import qrcode

whatVersion = int(input('input version (number): '))
data = input('input your data: ')

qr = qrcode.QRCode(
    version=whatVersion,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

img.save('output/output.png')
