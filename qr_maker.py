import qrcode
import time


def qr_maker(content, file_path):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image()
    f = "{0}/qr_{1}.png".format(file_path, time.time())
    img.save(f)


if __name__ == '__main__':
    qr_maker(raw_input(),"")
