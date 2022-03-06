def invert_color(color):
    red, green, blue = color
    red = 255 - red
    green = 255 - green
    blue = 255 - blue

    return int(red), int(green), int(blue)


def color_lerp(color1, color2, factor): # L = v1+(v2-v1)*f

    red1, green1, blue1 = color1
    red2, green2, blue2 = color2

    red = red1 + (red2 - red1) * factor
    green = green1 + (green2 - green1) * factor
    blue = blue1 + (blue2 - blue1) * factor

    return int(red), int(green), int(blue)


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
