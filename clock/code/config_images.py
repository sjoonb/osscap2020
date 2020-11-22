from PIL import Image

# -----------------------------------------------------------------------------
# Images
# -----------------------------------------------------------------------------
imagepath = '../PiClock/images/'

# The 'position' dictionaries show the top left and bottom right positions of
# each image within the image

# Small font used for temperature
imagename_smallfont = 'smallfont.png'
image_smallfont = Image.open(imagepath + imagename_smallfont)
imagepositions_smallfont = {'1': (0, 0, 4, 7),
                            '2': (5, 0, 9, 7),
                            '3': (10, 0, 14, 7),
                            '4': (15, 0, 19, 7),
                            '5': (20, 0, 24, 7),
                            '6': (25, 0, 29, 7),
                            '7': (30, 0, 34, 7),
                            '8': (35, 0, 39, 7),
                            '9': (40, 0, 44, 7),
                            '0': (45, 0, 49, 7),
                            'max': (50, 0, 54, 7),
                            'min': (55, 0, 59, 7),
                            'C': (60, 0, 64, 7),
                            'F': (65, 0, 69, 7),
                            '.': (70, 0, 72, 7),
                            ':': (73, 0, 75, 7),
                            '-': (76, 0, 78, 7),
                            'sp': (80, 0, 84, 7),
                            'ssp': (80, 0, 82, 7)}

# Clock Font
# The clock needs to contain the following characters:
# 0123456789 :12 ap -
# There is a full space (same size as digits) between 9 and :
# and a small space between 2 and a which is the same width as the 1
imagename_clockfont = 'clockfont.png'
image_clockfont = Image.open(imagepath + imagename_clockfont)
imagepositions_clockfont = {0: (0, 0, 6, 15),
                            1: (8, 0, 14, 15),
                            2: (16, 0, 22, 15),
                            3: (24, 0, 30, 15),
                            4: (32, 0, 38, 15),
                            5: (40, 0, 46, 15),
                            6: (48, 0, 54, 15),
                            7: (56, 0, 62, 15),
                            8: (64, 0, 70, 15),
                            9: (72, 0, 78, 15),
                            ' ': (80, 0, 86, 15),
                            ':': (88, 0, 90, 15),
                            ': ': (92, 0, 94, 15),
                            'am': (95, 0, 99, 15),
                            'pm': (100, 0, 104, 15)}

# Small version (16x16) of the weather icons
#imagename_weather16 = 'OWMweather16.png'
#image_weather16 = Image.open(imagepath + imagename_weather16)
#imagepositions_weather16 = {'01d': (0, 0, 15, 15),
#                            '02d': (16, 0, 31, 15),
#                            '03d': (32, 0, 47, 15),
#                            '04d': (48, 0, 63, 15),
#                            '09d': (64, 0, 79, 15),
#                            '10d': (80, 0, 95, 15),
#                            '11d': (96, 0, 111, 15),
#                            '13d': (112, 0, 127, 15),
#                            '50d': (128, 0, 143, 15),
#                            '01n': (0, 16, 15, 31),
#                            '02n': (16, 16, 31, 31),
#                            '03n': (32, 16, 47, 31),
#                            '04n': (48, 16, 63, 31),
#                            '09n': (64, 16, 79, 31),
#                            '10n': (80, 16, 95, 31),
#                            '11n': (96, 16, 111, 31),
#                            '13n': (112, 16, 127, 31),
#                            '50n': (128, 16, 143, 31)}

