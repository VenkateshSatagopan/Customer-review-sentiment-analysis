# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 13:45:50 2020

@author: venkatesh
"""

import tensorflow_datasets as tfds
import tensorflow as tf
from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
from healthcheck import HealthCheck

import logging


app= Flask(__name__)
Bootstrap(app)
padding_size=1000
model=tf.keras.models.load_model('sentiment_analysis.hdf5')
text_encoder=tfds.features.text.TokenTextEncoder.load_from_file('sa_encoder.vocab')


logging.basicConfig(filename='flask.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logging.info('Model and Vocabulary loaded.....')
health=HealthCheck(app,"/hcheck")


def howami():
    return True, "I am Good"

health.add_check(howami)

def pad_to_size(vec,size):
  zeros=[0]*(size-len(vec))
  vec.extend(zeros)
  return vec

def predict_fn(pred_text,padding_size):
  encoded_pred_text=text_encoder.encode(pred_text)
  print(encoded_pred_text)
  encoded_pred_text=pad_to_size(encoded_pred_text,32)
  print(encoded_pred_text)
  encoded_pred_text=tf.cast(encoded_pred_text,tf.float64)
  predictions=model.predict(tf.expand_dims(encoded_pred_text,0))
  return predictions


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/seclassifier',methods=['post'])
def predict_sentiment():
    text=request.form['text']
    print(text)
    predictions=predict_fn(text,padding_size)
    sentiment='positive' if float(''.join(map(str,predictions[0]))) > 0 else 'Negative'
    app.logger.info("Prediction :"+ str(predictions[0])+ "sentiment:" + sentiment)
    return render_template('results.html',predictions=sentiment,name = text)
    #return "PASS"

if __name__=="__main__":
    app.run(host='0.0.0.0',port='5000')