from PIL import Image, ImageFilter

# Відкриваємо файл зображення 'cat.jpg'
with Image.open('cat.jpg') as original:
    print('Розмір:', original.size)
    print('Формат:', original.format)
    print('Тип:', original.mode)
    original.show()

    # Розмиття зображення
    pic_blur = original.filter(ImageFilter.BLUR)

    # Зберігаємо розмите зображення
    pic_blur.save('blur.jpg')
    pic_blur.show()

    # Конвертуємо зображення в чорно-біле
    pic_grey = original.convert('L')
    pic_grey.save('gray.jpg')
    pic_grey.show()


    # Обертання зображення на 180 градусів
    pic_up = original.transpose(Image.ROTATE_180)
    pic_up.save('upside_down.jpg')
    pic_up.show()
