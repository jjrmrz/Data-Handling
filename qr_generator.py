import qrcode


def qr_generator():
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )

    qr.add_data(ask_user('Enter a valid URL to create a QR code: '))
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue", back_color="white")
    type(img)
    img.save(ask_user('Save image as: '))


def ask_user(question):
    ans = input(question)
    return ans


def main():
    qr_generator()


if __name__ == '__main__':
    main()
