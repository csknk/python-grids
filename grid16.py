#!/usr/bin/env python3

from PIL import Image, ImageDraw

if __name__ == '__main__':
    height = 200
    width = 200
#    image = Image.new(mode='L', size=(height, width), color=255)
    image = Image.new(mode='P', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / 4)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)


    for x in range(0, 4):
        for y in range(0, 4):
            x_coord = (x * step_size) + 3
            y_coord = (y * step_size) + 3
            t = x + (y * 4)
            t_mod = (t % 6) + 1
            text_color = (0, 0, 255) 
            draw.text((x_coord, y_coord), str(t), fill='black')
            draw.text((x_coord + 30, y_coord + 28), str(t_mod), fill=text_color)

    del draw

    image.show()

