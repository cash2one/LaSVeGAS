''' Generates png (lossless) outputs for paragraphs.

References:
Image Module
https://pillow.readthedocs.io/en/3.4.x/reference/Image.html
ImageDraw Module
https://pillow.readthedocs.io/en/3.4.x/reference/ImageDraw.html
ImageFont
https://pillow.readthedocs.io/en/3.4.x/reference/ImageFont.html

'''

# TODO: Add support for splitting values over multiple images. Otherwise
#      we need to reject images larger than a given size.


import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import textwrap

MAX_W, MAX_H = 1920, 1080

# SHADOW_COLOR = "black"
TEXT_COLOR = "black"


def GenerateImage(text, output_path, bgcolor):
    print "Generating Image for the value: " + text

    # Create an image with a bg colour.
    img = Image.new("RGBA", (MAX_W, MAX_H), bgcolor)
    draw = ImageDraw.Draw(img)

    # Now add text to the image.
    # Convert to paragraph.
    para = textwrap.wrap(text, width=40)  # width = number of characters.

    font = ImageFont.truetype("Georgia.ttf", 100)  # fontsize

    # Determining the height at which we want to start the text.
    w_first, h_first = draw.textsize(para[0], font=font)
    current_h = (MAX_H / 2) - ((len(para) / 2) * h_first)

    pad = 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        x = (MAX_W - w) / 2
        y = current_h

        # Add shadow (Doesn't look good with smaller fonts.)
        # draw.text((x-2, y), line, font=font, fill=SHADOW_COLOR)
        # draw.text((x+2, y), line, font=font, fill=SHADOW_COLOR)
        # draw.text((x, y-2), line, font=font, fill=SHADOW_COLOR)
        # draw.text((x, y+2), line, font=font, fill=SHADOW_COLOR)

        # Add test
        draw.text((x, y), line, fill=TEXT_COLOR, font=font)

        current_h += h + pad

    img.save(output_path)
    # img.save("value.png")
