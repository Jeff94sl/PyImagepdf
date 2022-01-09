import unittest
from PDF.pdfimage import Convert


class MyTestCase(unittest.TestCase):

    def test_imagensize(self):
        c = Convert()
        imgs = ['icon.png']
        result = c.imgtopdfautosize("testimgauto.pdf", imgs)
        self.assertEqual(result, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
