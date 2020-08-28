from flask import Flask, request, jsonify
import led_service as ls

app = Flask(__name__)


# {{url}}/led?red=255&green=255&blue=255&position=1
@app.route('/', methods=['GET'])
def led():
    red = request.args.get('red')
    green = request.args.get('green')
    blue = request.args.get('blue')

    resp = ls.update_led(red, green, blue)
    return jsonify({"message": resp})

