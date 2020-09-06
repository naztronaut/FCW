import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rpi_ws281x import PixelStrip, Color
import config as c


strip = PixelStrip(c.LED_COUNT, c.LED_PIN, c.LED_FREQ_HZ, c.LED_DMA, c.LED_INVERT, c.LED_BRIGHTNESS, c.LED_CHANNEL)
strip.begin()


# Define functions which animate LEDs in various ways.
# functions below are from the strandtest example: https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py
def color_wipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        # with open("file/status.txt", "a") as f:
        #     f.write(str(color) + "\r\n")
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def smooth(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        # with open("file/status.txt", "a") as f:
        #     f.write(str(color) + "\r\n")
    strip.show()


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "./file/status.txt":
            with open("./file/status.txt", "r") as f:
                try:
                    colors = f.read().strip().split(',')
                    if colors[0] == 'wipe':
                        color_wipe(strip, Color(int(colors[1]), int(colors[2]), int(colors[3])))
                    elif colors[0] == 'chase':
                        theaterChase(strip, Color(int(colors[1]), int(colors[2]), int(colors[3])))
                    elif colors[0] == 'smooth':
                        color_wipe(strip, Color(int(colors[1]), int(colors[2]), int(colors[3])))
                    else:
                        color_wipe(strip, Color(int(colors[1]), int(colors[2]), int(colors[3])))
                except:
                    print("could not read file, trying again")
                    MyHandler()
            # colorWipe(strip, Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='./file', recursive=False)
observer.start()

observer.join()


