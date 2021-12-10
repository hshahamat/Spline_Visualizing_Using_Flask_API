# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:20:48 2021

@author: Shahamat
"""

import numpy as np
from flask import Flask, request, jsonify
from lib import show_spline_on_img
from PIL import Image
import cv2

app = Flask(__name__)

@app.route("/", methods=["POST"])
def process_image():
    file = request.files['image']
    frm = request.form.to_dict(flat=False)
    img = Image.open(file.stream)
    

    
    ann = {}
    ann['t'] = np.array(frm['t'])
    ann['k'] = int(frm['k'][0])
    
    tmp_c = frm['c']
    tmp_c = [c[1:-1] for c in tmp_c]
    tmp_c = [[float(c.split(',')[0]),float(c.split(',')[1])] for c in tmp_c]
    ann['c'] = tmp_c

    timg = np.asarray(img)
    timg = cv2.cvtColor(timg,cv2.COLOR_BGR2RGB)
    img = show_spline_on_img(timg,ann)
    res = {}
    res['packetID'] = frm['packetID']
    _, img_encoded = cv2.imencode('.jpg', img)
    res['resultImage'] = list(img_encoded.tobytes())
    return jsonify(res)


if __name__ == "__main__":
    app.run()