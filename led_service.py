import os
import subprocess
#
# import board
# import neopixel
# import config

# Change to the number of LEDs you are using
# Uses GPIO Pin 18. if you want to use another pin, change the D18 to some other pin
# pixels = neopixel.NeoPixel(board.D18, config.LED_COUNT)


def update_led(mode, red, green, blue):
    # os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py  ' + red + ' ' + green + ' ' + blue)
    with open("/var/www/html/fcw/file/status.txt", "w") as f:
        f.write(mode + "," + red + "," + green + "," + blue)
    # os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py  ' + red + ' ' + green + ' ' + blue)
    # for x in range(0, config.LED_COUNT):
    #     pixels[x] = (red, green, blue)


def start_visualization():
    # os.popen('sudo nohup python3 /var/www/html/fcw/led_watchdog.py >> /dev/null 2>&1 &')
    # os.popen('sh /var/www/html/fcw/script.sh')
    subprocess.Popen(["sudo", "python3", "/var/www/html/fcw/led_watchdog.py"])


def stop_visualization():
    os.popen('sudo pkill -f led_watchdog.py')


def check_visualization_status():
    resp = os.popen('ps aux | grep led_watchdog.py')
    if "sudo python3 /var/www/html/fcw/led_watchdog.py" in resp.read():
        return True
    else:
        return False
