import sys
import board
import neopixel
import config

# Uses GPIO Pin 18. if you want to use another pin, change the D18 to some other pin
pixels = neopixel.NeoPixel(board.D18, config.LED_COUNT)

red = sys.argv[1]
green = sys.argv[2]
blue = sys.argv[3]

pixels.fill((int(red), int(green), int(blue)))
# for x in range(0, config.LED_COUNT):
#     pixels[x] = (int(red), int(green), int(blue))
