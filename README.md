# Deteccion-de-plagas-en-plantas-con-tensorflow
This code allows you to detect pests in several species of edible plants: potatoes, tomatoes, cherries, orange trees ... among others. Use tensorflow and I can do it with images, videos, or in real time with a pc and a camera or a raspberry pi with a camera.
To use my code, you must have installed tensorflow and opencv.
You will be able to detect the following pests:

Spider tomato

healthy raspberry

leaf spot isariopisis grape

stain leaf gray corn

Healthy mnanzana

Cedar apple scab

dusty mildew green leaves

tomato mosaic virus

healthy cherry

northern tizon or maiz leaf

healthy peach

cherry mushroom podosphaera clandestine

greening orange

tomato late blight

tomato bacterial spot

healthy grape

common mold corn

tomato leaf mold

bacterial blotch peppers

grape black rot

early tomato

healthy strawberry

leaf spot tomato

grape measles

curl virus yellow leaf tomato

scorched leaf strawberry

healthy potato

pudridumbrenegraen-apples

healthy blueberries

late tizon potato

healthy pepper

healthy tomato

early tizon potato

costra apple

tomato focus point

healthy soy

healthy corn

peach bacterial blotch

#If you are in a raspberry pi you can follow this tutorial to install tensorflow:
https://www.tensorflow.org/install/install_raspbian
#Or follow these steps if you are in Ubuntu:
https://www.tensorflow.org/install/install_linux
#You can follow this guide to compile opencv in raspberry:
https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
#Once you have installed tensorflow and opencv, download my already trained model:
https://drive.google.com/drive/folders/1sowAcyeYXFCnhekE-WSOxUt5PASTijLq
#Now you must open and edit the file: 
"recognition.py"
#Search the following code lines:


"# Loads label file, strips off carriage return

 label_lines = [line.rstrip () for line

 in tf.gfile.GFile ("retrained_labels11.txt")]"



"with tf.gfile.FastGFile ("retrained_graph11.pb", 'rb')"

Modify there the route where you have saved the model that you have downloaded.
Now look for the following code lines at the beginning of the file:
#if you use a video place your video here:
video = 'march.mp4'
#if you use a video uncomment this line:
 "cam = cv2.VideoCapture (video)"
#This line is to make the detection in real time through your camera, comment on it if you do it with video:
 "cam = cv2.VideoCapture (0)"

There, comment or uncomment the code according to your need if you want to do it in real time with a camera or if you want to do the detection from a video.

#To execute your code:
python recognition.py
You should first see the prediction that corresponds to the type of pest you are detecting.


#You can use the file: 
labelimage.py 
#if you want to do the detection with photos, you can do it in the following way:
"python labelimage.py "path of the image you want to try""

#If you want to train a new moidelo, use the retrain.py file and follow the steps below:

https://github.com/VikramTiwari/tensorflow-retrain-sample


#If you speak English you will want to understand your model in English, so you can download the original dataset from here and train with those images so that your human text is in English:

https://github.com/salathegroup/plantvillage_deeplearning_paper_dataset/tree/master/raw/color


#If you want to understand the model for use on mobile devices, you can see this guide, you will use mobilenet for this purpose :

https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html#3


#I use mobilenet mobilenet_v1_1.0_224, you can download it from here:

https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md


#Then you must convert your model to a Lite type model to work in android studio, and the build.gradle can recognize it. Use this command, it works fine on Ubuntu 16.04, you will use it for this purpose, it is installed when you install tensorflow:

"toco --input_file=tf_files/retrained_graph.pb --output_file=tf_files/optimized_graph.lite --input_format=TENSORFLOW_GRAPHDEF 
--output_format=TFLITE --input_shape="1,224,224,3" --input_array=input --output_array=final_result --inference_type=FLOAT --input_data_type=FLOAT"

#Now you will have an optimized model for android studio: 
"optimized_graph.lite"


#Now you must copy your model to android studio, you can follow this guide to configure your android studio in ubuntu 16.04:

https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2-tflite/#3


#You can download from here the android studio:

https://developer.android.com/studio/









happy hacking!




