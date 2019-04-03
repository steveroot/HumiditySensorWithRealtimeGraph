import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import smbus
import time

# This awfully formatted not-quite-sure-how-i-got-this-working code somehow
# managed to draw a graph in realtime of humidity and temperature that I used
# in a youtube video here: https://youtu.be/2OoqQHAcpSQ
# on our youtube channel here: https://www.youtube.com/channel/UCD9Y6a-JI4xpaT0f2KiuPZg
# our == Roots Kitchens Bedrooms Bathrooms, https://www.rkbb.co.uk
# we're a small family run retail business designing, supplying and installing
# Kitchens Bedrooms and Bathrooms.
#
# The code ran on a raspberry pi with an attached temperature and humidity
# sensor, and Adafruit SHT31-D
# https://shop.pimoroni.com/products/adafruit-sensiron-sht31-d-temperature-humidity-sensor-breakout
# https://www.adafruit.com/product/2857 Adafruit Sensirion SHT31-D - Temperature & Humidity Sensor
#
# If you're looking to use this you may be better to look at the manufacturers
# guides here rather than rely on untangling my spagetti code.
# https://learn.adafruit.com/adafruit-sht31-d-temperature-and-humidity-sensor-breakout
# besides, that will also tell you which pins you need to wire to.  This github page
# was also useful:
# https://github.com/adafruit/Adafruit_SHT31
#
# So once I had correctly soldered the Sensor and connected it to the Raspberry
# Pi I modified code from this page to get a realtime graph working
# https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time
#
# The graph was running on the raspbery pi display, so to view it on my laptop
# I used VNC for a remote desktop connection an I then recorded the laptop
# display to edit into the video.



# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
ys1 = []


def readsensor():
  # Get I2C bus
  bus = smbus.SMBus(1)

  #  SHT31 address, 0x44(68)
  bus.write_i2c_block_data(0x44, 0x2C, [0x06])

  time.sleep(0.5)

  # SHT31 address, 0x44(68)
  # Read data back from 0x00(00), 6 bytes
  # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
  data = bus.read_i2c_block_data(0x44, 0x00, 6)

  # Convert the data
  temp = data[0] * 256 + data[1]
  cTemp = -45 + (175 * temp / 65535.0)
  humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

  #  Output data to screen
  print ("Temperature in Celsius is : %.2f C" %cTemp)
  print ("Relative Humidity is : %.2f %%RH" %humidity)
  thistuple = (cTemp, humidity)
  return (thistuple)



# This function is called periodically from FuncAnimation
def animate(i, xs, ys, ys1):


    gettuple = readsensor()

    cTemp = (gettuple[0])
    cHum = (gettuple[1])
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(cTemp)
    ys1.append(cHum)


    # Limit x and y lists to 40 items
    xs = xs[-40:]
    ys = ys[-40:]
    ys1 = ys1[-40:]

    # Draw x and y lists
    ax.clear()

    ax.plot(xs, ys, 'r')
    ax.plot(xs, ys1, 'b')


    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.ylim([0, 100])
    plt.title('Humidity RH% = Blue      Temperture Deg C = Red')
    plt.ylabel('Scale 0 - 100')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, ys1), interval=1000)
plt.show()
