import os
#
# import board
# import neopixel
# import config

# Change to the number of LEDs you are using
# Uses GPIO Pin 18. if you want to use another pin, change the D18 to some other pin
# pixels = neopixel.NeoPixel(board.D18, config.LED_COUNT)


def update_led(red, green, blue):
    os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py  ' + red + ' ' + green + ' ' + blue)
    # for x in range(0, config.LED_COUNT):
    #     pixels[x] = (red, green, blue)
