from flask import Flask, request, jsonify, current_app
import led_service as ls

app = Flask(__name__)


@app.route('/led', methods=['GET'])
def ui():
    return current_app.send_static_file('index.html')


# {{url}}/led?red=255&green=255&blue=255&position=1
@app.route('/led', methods=['GET'])
def led():
    red = request.args.get('red')
    green = request.args.get('green')
    blue = request.args.get('blue')

    resp = ls.update_led(red, green, blue)
    return jsonify({"message": resp})


@app.route('/check_vis_status', methods=['GET'])
def check_vis_status():
    return jsonify({"message": ls.check_visualization_status()})

