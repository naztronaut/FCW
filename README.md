# FCW
Flask Controlled WS2812b LED Strip

## Demo

(Coming soon)

<a href="https://www.youtube.com/watch?v=1a16lYx2mZE" target="_blank"><img src="img/FCW_thumbnail.jpg" alt="FCW Demo" width="700px" /></a>

Once everything works, the current version's web UI will look like this:

<img src="img/ui_demo.png" alt="FCW UI" width="700px">

## Table of Contents

1. [Getting Started](#getting-started)
    1. [Hardware](#hardware)
    2. [Install Git & Clone repo](#install-git--clone-repo)
    3. [Install dependencies with `install.py`](#install-dependencies-with-installpy)
    4. [Config.py](#configpy-has-been-edited-as-follows)
2. [Install and Run Flask](#install-and-run-flask)
3. [Run led_watchdog.py](#run-led_watchdogpy-in-the-background)
4. [Authors](#authors)
5. [License](#license)
6. [Questions](#questions-)
7. [Contribute](#contribute)

## Getting Started

### Hardware

Here's a small Fritz diagram of how to wire the Pi with your WS2812b LED strip:

<img src="img/AIIM_circuit.jpg" width="700px" alt="Circuit Diagram for WS2812b lights">

### Install Git & Clone repo

I normally start the lite version of Raspberry Pi OS without desktop and recommended software so it usually doesn't come with Git installed. So let's install it:

```shell
sudo apt install git -y
```

After we install git, clone this repo:

```shell
git clone https://github.com/naztronaut/FCW.git
sudo mv FCW fcw
```
The last command is to just rename the folder to lower case. 

Then let's head into our install directory and continue to the next step:

```shell
cd fcw/install
```

### Install dependencies with `install.py`

Once you are in the install directory, run this command:

```shell
sudo python3 install.py
```

The installation should take a few minutes (depends on your internet speed and how many of the packages need a full install). The script is very simple. It runs a bunch of `sudo apt install`
and `pip3 install` commands to make sure all dependencies are installed. 

The script also installs the `rpi_ws281x` library which is used to actually turn the lights on and off. 

### `config.py` has been edited as follows:

```python
LED_COUNT = 142        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
```

The only thing you need to change is the `LED_COUNT` if it's different from 142. My LED strip has 142 lights. Feel free to play with the other settings as well. 


### Install and Run Flask

I recommend running everything in a virtual environment. Makes it really easy to undo as well as run multiple projects at the same time without collision. For more information on
how to run Flask behind Apache, check out https://www.easyprogramming.net/raspberrypi/pi_flask_app_server.php

Here are some quick steps to take once you are inside your `fcw` folder:

```shell
sudo python3 -m venv venv
sudo chown -R pi:www-data venv
pip3 install flask
cd venv/bin/
wget https://raw.githubusercontent.com/naztronaut/RaspberryPi-RGBW-Control/master/utils/activate_this.py
``` 

Then in your Apache config, place the contents from `utils/apache-led.conf` file into a separate .conf file like below:

```shell
cd /etc/apache2/sites-available
sudo nano fcw.conf
```

Paste in the contents:

```apache
<VirtualHost *:80>
        ServerName fcw
        WSGIDaemonProcess fcw user=pi group=www-data threads=5
        WSGIScriptAlias /fcw /var/www/html/fcw/fcw.wsgi
        <Directory /var/www/html/fcw>
                WSGIProcessGroup fcw
                WSGIApplicationGroup &{GLOBAL}
                Require all granted
        </Directory>
</VirtualHost>
```

Then disable the default config and add the new one and restart Apache:

```shell
sudo a2ensite piapp.conf
sudo a2dissite 000-default.conf
sudo service apache2 restart
```

If things go well, you should be able to access the app by going to http://ip_addr/fcw

### Run led_watchdog.py in the background

The way the lights work is a background watchdog process is run looking for updates to `file/status.txt` and then it parses that data to turn on the lights. 

We need to do this so that the lights are continuously updating when new commands are sent instead of restarting. I'm still working on trying to figure out a way to run that script
from the Flask app, still a bit behind, hopefully  I'll figure it out soon. If you have ideas, let me know! 

In the meantime, run the script in the background with this command (activate your virtual environment if you are using it):

```shell
sudo nohup python3 /var/www/html/fcw/led_watchdog.py >> /dev/null 2>&1 &
```

Now any updates sent from the UI will make the lights trigger. 

To kill the script, run:

```shell
sudo pkill -f led_watchdog.py
```


## Authors
* **Nazmus Nasir** - [Nazmus](https://nazm.us) - Owner of EasyProgramming.net

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Questions ?
Have questions? You can reach me through several different channels. You can ask a question in the  [issues forum](/../../issues), 
on [EasyProgramming.net](https://www.easyprogramming.net), or on the video comments on YouTube. 


## Contribute 
I will accept Pull requests fixing bugs or adding new features after I've vetted them. Feel free to create pull requests!  