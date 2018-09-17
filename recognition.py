#This code was written by @NiperiaLab, Daniel Dieser
#coding: utf-8

import socket
from threading import *
import commands
import os, sys
import tensorflow as tf
import cv2
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#if you use a video place your video here:
video = 'marcha.mp4'
#if you use a video uncomment this line:
#cam = cv2.VideoCapture(video)
# This line is to make the detection in real time through your camera, comment on it if you do it with video:
cam = cv2.VideoCapture(0) 

 
 
while True:
# Loads label file, strips off carriage return

 label_lines = [line.rstrip() for line

                   in tf.gfile.GFile("retrained_labels.txt")]




 with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:

    graph_def = tf.GraphDef()

    graph_def.ParseFromString(f.read())

    tf.import_graph_def(graph_def, name='')



 while True:

    have_frame, frame = cam.read()

    with tf.Session() as sess:

        # Feed the image_data as input to the graph and get first prediction

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')



        predictions = sess.run(softmax_tensor, \

                 {'DecodeJpeg/contents:0': cv2.imencode('.jpg', frame)[1].tostring()})



        # Sort to show labels of first prediction in order of confidence

        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        #recibido = sc.recv(400000)

        for node_id in top_k:

            human_string = label_lines[node_id]

            score = predictions[0][node_id]

            print('%s (score = %.5f)' % (human_string, score))
            
            if  human_string==("daniel") and score > 0.99:

                print ("hola, daniel como estas?")
                os.system("google_speech -l es 'hola daniel, como estas?' -e speed 1 pitch -600")
                os.system("python ./cancionfav.py") 
            if  human_string==("orcas") and score > 0.70:

                os.system("python ./bot.py Orcas-en-Zona-Doradillo")                



if cv2.waitKey(34) == 27:

		exit(0) 


    
