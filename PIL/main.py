from PIL import Image

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except FileNotFoundError:
            print('Файл не знайдено!')
        if self.original:
            self.original.show()

    def do_bw(self):
        if self.original:
            gray = self.original.convert("L")
            self.changed.append(gray)
            gray.save('gray1.jpg')

my_image = ImageEditor('cat.jpg')
my_image.open()
my_image.do_bw()

for i in my_image.changed:
    i.show()
