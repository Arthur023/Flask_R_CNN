from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

# import flask
import pickle

from flask import Flask, request, render_template, flash, url_for, redirect, send_file
from werkzeug.utils import secure_filename
# import sre_compile

import os
import random
import pprint
import shutil
import sys
import time
import numpy as np
# from optparse import OptionParser
import pickle
import math
import cv2
import copy

# from app import Config as C

# from PIL import Image

from flask import send_file
from matplotlib import pyplot as plt
import tensorflow as tf
# tf.disable_v2_behavior()

# import pandas as pd

# from sklearn.metrics import average_precision_score

# from sklearn.metrics import average_precision_score, precision_recall_curve

from keras import backend as K
# from keras.optimizers import Adam, SGD, RMSprop
from keras.layers import Flatten, Dense, Input, MaxPooling2D, Dropout, Activation, ZeroPadding2D, \
    BatchNormalization, \
    Conv2D, Add
from keras.layers import GlobalAveragePooling2D, GlobalMaxPooling2D, TimeDistributed, AveragePooling2D
# from keras.engine.topology import get_source_inputs
# from keras.utils import layer_utils
# from keras.utils.data_utils import get_file
# from keras.objectives import categorical_crossentropy
from keras.initializers import glorot_uniform

from keras.models import Model
# from keras.utils import generic_utils
from keras.layers import Layer

# from keras import initializers, regularizers

from zipfile import ZipFile

# from sklearn.metrics import average_precision_score
from test_model import *

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'zip'}

app = Flask(__name__)
app.secret_key = os.urandom(128)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# base_path = 'model'
#
# # test_base_path = '../../data/augmentatie/deel_2_minder_augment'  # Directory to save the test images
#
# config_output_filename = os.path.join(base_path, 'model_resnet_config.pickle')
#
# with open(config_output_filename, 'rb') as f_in:
#     C = pickle.load(f_in)
# C = Config

# base_path = 'model_2'
# config_output_filename = os.path.join(base_path, 'model_resnet_config.pickle')
# with open(config_output_filename, 'rb') as f_in:
#     C = pickle.load(f_in)
# # print('config',Config)
# # print('config',Config.class_mapping)
# # print('config',Config.use_horizontal_flips)
# # print('config model path',Config.model_path)
# Config = C
# print('config',Config)
# print('config',Config.class_mapping)
# print('config',Config.use_horizontal_flips)
# print('config model path',Config.model_path)
# print('HHHHHHHHHHHH')

# @app.route('/')
# def index():
#     return render_template('index.html')
#
# if __name__ == "__main__":
#     app.run(debug=True)
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_image(filename):
    if not "." in filename:
        print('fout met die punt')
        return False
    ext = filename.rsplit(".", 1)[1].lower()
    if ext in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        print('een andere fout')
        return False


@app.route('/')
def upload_form():
    return render_template('upload_image.html')


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        # render_template('download.html')
        if request.files:
            zip = request.files["zip"]

            if zip.filename == "":
                print("No filename")
                return redirect(request.url)
            if allowed_image(zip.filename):
                filename = secure_filename(zip.filename)

                print('zip', zip)
                # filename = secure_filename(zip.filename)
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                zip.save(file_path)
                # print("Image saved")
                # print('zip filename', zip.filename)
                # print('zip', zip)
                # print('file_path', file_path)
                # print('filename', filename)
                zip_file = maint(file_path,filename,C)
                return zip_file # redirect(request.url)#
            else:
                print("That file extension is not allowed")
                return redirect(request.url)
    return render_template('upload_image.html')


#
# @app.route('/')
# def upload_form():
#     return render_template('upload.html')
#
#
# @app.route('/', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         print('upload_image filename: ' + filename)
#         flash('Image successfully uploaded and displayed, in upload_image()')
#         print(filename)
#         all_data = maint(filename)
#         print('all_data', all_data)
#         print('SUper test')
#         return render_template('upload.html')  # ,filename=filename) # om de afbeelding te tonen
#     else:
#         flash('Allowed image types are -> png, jpg, jpeg, gif')
#         return redirect(request.url)
#

# @app.route('/display/<filename>')
# def display_image(filename):
#     print('display_image filename: ' + filename)
#     return send_file('static/uploads/' + filename)
#     # return redirect(url_for('static', filename='uploads/' + filename), code=301)
#

@app.route('/return_files/')
def return_files():
    try:
        # return redirect(url_for('static', filename='uploads/' + 'dd.txt'), code=301)
        print('image_name')
        # as_attachment zorgt ervoor dat je het tekst document download
        # time.sleep(1000)
        return send_file('static/text_files/tekst.txt', attachment_filename='tekst.txt', as_attachment=True)
    except Exception as e:
        return str(e)


@app.route('/file_downloads/')
def file_downloads():
    return render_template('download.html')




if __name__ == "__main__":

    # flask run --host=0.0.0.0
    # base_path = 'model_2'
    # config_output_filename = os.path.join(base_path, 'model_resnet_config.pickle')
    # with open(config_output_filename, 'rb') as f_in:
    #     C = pickle.load(f_in)
    # # print('config',Config)
    # # print('config',Config.class_mapping)
    # # print('config',Config.use_horizontal_flips)
    # # print('config model path',Config.model_path)
    # Config = C
    # print('config',Config)
    # print('config',Config.class_mapping)
    # print('config',Config.use_horizontal_flips)
    # print('config model path',Config.model_path)
    # print('HHHHHHHHHHHH')
    # app.run(host="172.17.0.2")

    app.run(debug=True,threaded=False)


