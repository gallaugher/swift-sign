# swift-sign
Use an Adafruit LED Matrix Portal + 32x32 LED display to create a sign showing an animation of the Swift language logo.

Same code also works on a 64x32 LED display (that's the one I use for Baby Yoda). All you need to do is modify the 
matrix_width = 32 line so that it reads
matrix_width = 64

Then also be sure to use properly sized .bmps

You can find examples of the 32x32 and 64x32 in the Build Video for this project that I've posted to YouTube:
https://YouTube.com/@BuildWithProfG

Hardware used:
While I used the Matrix Portal M4, I recommend this version instead. It's cheapter, faster, and newer. The code & setup should otherwise be identical.
Adafruit Matrix Portal S3: https://www.adafruit.com/product/5778
If you're curious, this is the older board I'm using:
Adafruit Matrix Portal M4: https://www.adafruit.com/product/4745

You'll also need an LED Matrix Panel:
32 x 32 RGB LED Matrix Panel (I used a 5mm, but you can use any of the other mm sizes): https://www.adafruit.com/product/2026

And the Baby Yoda uses 64 x 32 (I used the 4mm pitch, but any pitch size should work): https://www.adafruit.com/product/2278 

You'll also need a USB-C data (not just power/charging) cable to connect your Matrix Portal to your Mac or PC for programming, and to a standard USB power supply - like the small one that you might use to charge most mobile phones - to independently run this.

Also: In the video above, my sign is attached to my magnetic white board. The 32 x 32 panels used to come with magnetic feet. I think this is the separate product you can buy if you want to attach your sign to a magnetic surface: https://www.adafruit.com/product/4631

I'd welcome suggestions for better bmp creation / editing software.
I just modified a 352 width x 32 height box in Photoshop.
Make sure mode is set to Index Color using the menu:
  Image > Mode > Indexed Color

Image must also be no greater than 8-bits, so also select the menu:
  Image > Mode > 8 Bits/Channel
  
When editing, treat every 32 bits (or 64 bits for the 64 bit panel) as if it's a frame in the grid that's animated by the python code.
the swift.bmp has 10 images, so you'll note while loop resets to grid_index = 0 after the 10th image is displayed.

NOTE: Since Adabox 016 added a 64 x 32, you can use the code above, just change the matrix_width = 32 to 64.
Also make sure you use images that support 64 bit width. Only one up here so far is 
yoda_sip.bmp
which is baby yoda sipping soup.
