# Code modified from original by @BlitzCityDIY via
# Adafruit tutorial at:
# https://learn.adafruit.com/iot-twitter-listener-party-parrot/coding-the-iot-party-parrot
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
 
#  create matrix display
#  I also added a bit_depth to make more colors pop out
matrix = Matrix(width=32, height=32, bit_depth=4)
display = matrix.display
 
#  load in bitmap (image_bit), and colors into a pallet (image_pal)
#  The file you are loading in is in the quotation marks
#  Make sure it's a .bmp with 8 bit format, otherwise it won't work
#  number_of_images for my files: 
# number_of_images = 29 # raspberry-adafruit-animated
number_of_images = 11 # swift
# number_of_images = 11 # animated_arduino
# number_of_images = 8 # animated_Excel
# number_of_images = 54 # combined-animation
image_bit, image_pal = adafruit_imageload.load("/swift.bmp",
                                                 bitmap=displayio.Bitmap,
                                                 palette=displayio.Palette)
# bitmap & pallet above are used to create the grid of individual
# tiles, 32 x 32, cut from the long bitmap image named in the
# quotes, above
image_grid = displayio.TileGrid(image_bit, pixel_shader=image_pal,
                                 width=1, height=1,
                                 tile_height=32, tile_width=32,
                                 default_tile=0,
                                 x=0, y=0)                                 
# make a group of sprites (sliced up images) from the grid
# created above
group = displayio.Group(max_size=60)
group.append(image_grid)
 
display.show(group)
 
# time.monotonic() is an internal clock value returned in fractional seconds
time_value = 0 #  time.monotonic() holder
grid_index = 0 #  index for tilegrid
# party_count = 0 #  count for animation cycles
 
while True:
    #  every 0.2 seconds...
    if (time_value + 0.2) < time.monotonic():
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

