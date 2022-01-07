import imagesize
from PaPDF.PaPDF import PaPDF


class Convert:
    def __init__(self):
        super(Convert, self).__init__()

    def texttopdf(self, filename, text, x, y):
        with PaPDF(filename) as pdf:
            pdf.addText(x, y, text)
            return True

    def imgtopdf(self, filename, imgs, x, y, w, h):
        with PaPDF(filename) as pdf:
            for img in imgs:
                pdf.addImage(img, x, y, w, h)
                pdf.addPage()
            return True

    def imgtopdfautosize(self, filename, imgs):
        with PaPDF(filename) as pdf:
            for img in imgs:
                w, h = imagesize.get(img)
                if w < 190 and h < 280:
                    pdf.addImage(img, pdf.h_mm/4, pdf.w_mm/1.9, w, h)
                    pdf.addPage()
                else:
                    pdf.addImage(img, 10, 10, 190, 280)
                    pdf.addPage()
            return True