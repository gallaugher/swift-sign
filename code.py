# Build by Prof. John Gallaugher @gallaugher, https://gallaugher.com
# YouTube: bit.ly/GallaugherYouTube
# Project Repo: https://github.com/gallaugher/swift-sign
# Build Video available in MakerSnack playlist at: http://bit.ly/makersnack
# Code modified from original by @BlitzCityDIY via
# Adafruit tutorial at:
# https://learn.adafruit.com/iot-twitter-listener-party-parrot/coding-the-iot-party-parrot
# BlitzCityDIY / Liz also provided the cool partyParrotsMatrix.bmp, in this repo.
# This code cuts out all of the networking above and treats the image as
# a continuously-cycling animation.

# Developed using CircuitPython v.6
# The following libraries are in the lib folder
# (May include more than is needed - I haven't double-checked)
# Folders:
#      adafruit_bitmap_font
#      adafruit_bus_device
#      adafruit_display_text
#      adafruit_esp32spi
#      adafruit_imageload
#      adafruit_io
#      adafruit_matrixportal
# Files:
#      adafruit_requests.mpy
#      neopixel.mpy
#      simpleio.mpy

import time
import board
import displayio
from adafruit_matrixportal.matrix import Matrix
import adafruit_imageload

# What are the dimensions of your LED Matrix?
matrix_width = 32
matrix_height = 32

# How fast should we flip between images?
animation_speed = 0.1 # speed between frames in fractional seconds

#  create matrix display
#  I also added a bit_depth to make more colors pop out
matrix = Matrix(width=matrix_width, height=matrix_height, bit_depth=6)
display = matrix.display

#  load in bitmap (image_bit), and colors into a pallet (image_pal)
#  The file you are loading in is in the quotation marks
#  Make sure it's a .bmp with 8 bit format, otherwise it won't work
#  I edited mine in Photoshop. Settings:
#  Image > Mode > Indexed Color
#  Save As: Format BMP, (next screen) File Format: Windows, Depth: 8 bit

# All bitmaps for this project assume 32 x 32 LED Display.
# Some of the bitmaps in the GitHub repo for this project:
# "swift", "full-animation",
# "raspberry-adafruit-animated", "animated_arduino",
# "swift-maker-animation", "animated-excel",
# "partyParrotsMatrix", "ghost-animation"
# Got other fun ones? Tweet 'em at me! @gallaugher

bitmap_name = "full-animation"
bitmap = displayio.OnDiskBitmap(open("/"+bitmap_name+".bmp", "rb"))
# Below assumes you have a single horizontal strip of images
# If you have a single vertical strip, swap out matrix_height for matrix_width
number_of_images = bitmap.width / matrix_width
print("number_of_images:", number_of_images)
image_bit, image_pal = adafruit_imageload.load("/"+bitmap_name+".bmp",
                                                 bitmap=displayio.Bitmap,
                                                 palette=displayio.Palette)
# bitmap & pallet above are used to create the grid of individual
# tiles, 32 x 32, cut from the long bitmap image named in the
# quotes, above
image_grid = displayio.TileGrid(image_bit, pixel_shader=image_pal,
                                 width=1, height=1,
                                 tile_height=matrix_height, tile_width=matrix_width,
                                 default_tile=0,
                                 x=0, y=0)
# make a group of sprites (sliced up images) from the grid
# created above
# I removed the max_size= parameter that was between the parens.
# It didn't seem necessary, but advise if I have this wrong.
group = displayio.Group()
group.append(image_grid)

# deprecated method, only use with CircuitPython 8 or older
# display.show(group)
# new property to be used with CircuitPyhton 9 and newer
display.root_group = group

# time.monotonic() is an internal clock value returned in fractional seconds
time_value = 0 #  time.monotonic() holder
grid_index = 0 #  index for tilegrid

while True:
    #  every animation_speed seconds...
    if (time_value + animation_speed) < time.monotonic():
        #  the animation cycles
        image_grid[0] = grid_index
        #  grid_index is the tilegrid index location
        time_value = time.monotonic()
        # below isn't needed, but if you open "Serial"
        # it's sometimes nice to see all images in the
        # grid_index are showing, then resetting to 0.
        # This can be useful for debugging
        print("Now Showing grid_index #:", grid_index)
        # increase grid_index by one so next loop shows
        # next frame/tile in the animation
        grid_index += 1
        #  if an animation cycle ends
        if grid_index > number_of_images-1:
            #  index is reset
            grid_index = 0
