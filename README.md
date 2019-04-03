# HumiditySensorWithRealtimeGraph
Code I used with Raspberry Pi + SHT31D humidity sensor to display real time graph

This awfully formatted not-quite-sure-how-i-got-this-working code somehow
managed to draw a graph in realtime of humidity and temperature that I used
in a youtube video here: https://youtu.be/2OoqQHAcpSQ
on our youtube channel here: https://www.youtube.com/channel/UCD9Y6a-JI4xpaT0f2KiuPZg
our == Roots Kitchens Bedrooms Bathrooms, https://www.rkbb.co.uk
we're a small family run retail business designing, supplying and installing
Kitchens Bedrooms and Bathrooms.

The code ran on a raspberry pi with an attached temperature and humidity
sensor, and Adafruit SHT31-D
https://shop.pimoroni.com/products/adafruit-sensiron-sht31-d-temperature-humidity-sensor-breakout
https://www.adafruit.com/product/2857 Adafruit Sensirion SHT31-D - Temperature & Humidity Sensor

If you're looking to use this you may be better to look at the manufacturers
guides here rather than rely on untangling my spagetti code.
https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout
besides, that will also tell you which pins you need to wire to.  This github page
was also useful:
https://github.com/adafruit/Adafruit_SHT31

So once I had correctly soldered the Sensor and connected it to the Raspberry
Pi I modified code from this page to get a realtime graph working
https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time

The graph was running on the raspbery pi display, so to view it on my laptop
I used VNC for a remote desktop connection an I then recorded the laptop
display to edit into the video.
