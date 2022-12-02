import qrcode

class QRGen:
    def __init__(self):
        self.version = 3
        self.box_size = 10
        self.border = 1

    def qr_generator(self):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self.box_size,
            border=self.border
        )

        qr.add_data(self.ask_user(1, 'Enter a valid URL to create a QR code - https://'))
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.set_bg(1), back_color=self.set_bg(2))
        img.save(self.ask_user(2, 'Save image as: '))


    def ask_user(self,tag, question):
        val = ''
        ans = input(question)
        if tag == 1:
            header = 'https://'
            val = header + ans
        elif tag == 2:
            extension = '.png'
            val = ans + extension
        else:
            val = ans
        print(val)
        return val


    def set_version(self):
        return self.ask_user(4, 'Set Version value between 1 - 40: ')

    def set_bg(self, tag):
        color = ''
        if tag == 1:
            mode = 'QR Code'
        elif tag == 2:
            mode = 'Background'
        print(f"Set {mode} Color.\n1 - Black\n2 - White\n3 - Blue\n4 - Red"
              "\n5 - Green\n6 - Yellow\n7 - Cyan\n8 - Magenta")
        ans = self.ask_user(3, 'Select Color: ')
        if ans == '1':
            color = 'black'
        elif ans == '2':
            color = 'white'
        elif ans == '3':
            color = 'blue'
        elif ans == '4':
            color = 'red'
        elif ans == '5':
            color = 'green'
        elif ans == '6':
            color = 'yellow'
        elif ans == '7':
            color = 'cyan'
        elif ans == '8':
            color = 'magenta'
        else:
            print("Error.")
        return color


def main():
    a = QRGen()
    a.qr_generator()


if __name__ == '__main__':
    main()
