import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from rpi_ws281x import PixelStrip, Color
import config as c


strip = PixelStrip(c.LED_COUNT, c.LED_PIN, c.LED_FREQ_HZ, c.LED_DMA, c.LED_INVERT, c.LED_BRIGHTNESS, c.LED_CHANNEL)
strip.begin()


# Define functions which animate LEDs in various ways.
def color_wipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        # with open("file/status.txt", "a") as f:
        #     f.write(str(color) + "\r\n")
        strip.show()
        time.sleep(wait_ms / 1000.0)


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "./file/status.txt":
            with open("./file/status.txt", "r") as f:
                try:
                    colors = f.read().strip().split(',')
                    color_wipe(strip, Color(int(colors[0]), int(colors[1]), int(colors[2])))
                except:
                    print("could not read file, trying again")
                    MyHandler()
            # colorWipe(strip, Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='./file', recursive=False)
observer.start()

observer.join()


