from flask import Flask, request, jsonify
import led_service as ls

app = Flask(__name__)


# {{url}}/led?red=255&green=255&blue=255&position=1
@app.route('/', methods=['GET'])
def led():
    red = request.args.get('red')
    green = request.args.get('green')
    blue = request.args.get('blue')
    if ls.check_visualization_status() is True:
        ls.start_visualization()
    if red == '0' and green == '0' and blue == '0':
        ls.stop_visualization()
    resp = ls.update_led(red, green, blue)
    return jsonify({"message": resp})


@app.route('/check_vis_status', methods=['GET'])
def check_vis_status():
    return jsonify({"message": ls.check_visualization_status()})

