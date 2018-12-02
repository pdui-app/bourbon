import cv2
import urllib
import numpy as np
from flask import Flask, request, jsonify
from skimage import io, transform

from bourbon_ import calibrate, rate_drunkenness

app = Flask(__name__)


@app.route('/calibrate', methods=['POST'])
def calibrate_req():
    data = request.json
    min_img_url = data['min-img-url']
    max_img_url = data['max-img-url']

    min_img = io.imread(min_img_url)
    max_img = io.imread(max_img_url)

    min_img = cv2.cvtColor(min_img, cv2.COLOR_RGB2BGR)
    max_img = cv2.cvtColor(max_img, cv2.COLOR_RGB2BGR)

    min_img = np.rot90(min_img, 2)
    max_img = np.rot90(max_img, 2)

    funcs = calibrate(min_img, max_img, 1)
    return jsonify({'success': funcs != None})


@app.route('/tipsy', methods=['POST'])
def tipsy():
    data = request.json
    min_img_url = data['min-img-url']
    max_img_url = data['max-img-url']
    vid_url = data['vid-url']

    min_img = io.imread(min_img_url)
    max_img = io.imread(max_img_url)
    urllib.urlretrieve(vid_url, 'eyes.mp4')

    vidcap = cv2.VideoCapture('eyes.mp4')

    funcs = calibrate(min_img, max_img, 1)
    if not funcs:
        return jsonify({'success': False})
    x_f, y_f = funcs[0], funcs[1]

    err = rate_drunkenness(vidcap, x_f, y_f, 30)

    return jsonify({
        'success': True,
        'error': err
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
