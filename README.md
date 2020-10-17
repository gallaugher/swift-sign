# swift-sign
Use an Adafruit LED Matrix Portal + 32x32 LED display to create a sign showing an animation of the Swift language logo.

An example of the project in action can be see in this Tweet:
https://twitter.com/gallaugher/status/1317206066770399232?s=20

Hardware used:
Adafruit Matrix Portal: https://www.adafruit.com/product/4745
32 x 32 RGB LED Matrix Panel (I used a 5mm, but you can use any of the other mm sizes): https://www.adafruit.com/product/2026
You'll also need a microUSB DATA (not just power/charging) cable to connect your Matrix Portal to your Mac or PC for programming, and to a standard USB power supply - like the small one that you might use to charge most mobile phones - to independently run this.

Also: In the tweet above, my sign is attached to my magnetic white board. The 32 x 32 panels used to come with magnetic feet. I think this is the separate product you can buy if you want to attach your sign to a magnetic surface: https://www.adafruit.com/product/4631

I'd welcome suggestions for better bmp creation / editing software.
I just modified a 352 width x 32 height box in Photoshop.
Make sure mode is set to Index Color using the menu:
  Image > Mode > Indexed Color

Image must also be no greater than 8-bits, so also select the menu:
  Image > Mode > 8 Bits/Channel
  
When editing, treat every 32 bits as if it's a frame in the grid that's animated by the python code.
the swift.bmp has 10 images, so you'll note while loop resets to grid_index = 0 after the 10th image is displayed.
