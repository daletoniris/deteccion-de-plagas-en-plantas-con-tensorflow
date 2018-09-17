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

If you are in a raspberry pi you can follow this tutorial to install tensorflow:
https://www.tensorflow.org/install/install_raspbian
Or follow these steps if you are in Ubuntu:
https://www.tensorflow.org/install/install_linux
You can follow this guide to compile opencv in raspberry:
https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
Once you have installed tensorflow and opencv, download my already trained model:
https://drive.google.com/drive/folders/1sowAcyeYXFCnhekE-WSOxUt5PASTijLq
Now you must open and edit the file: "recognition.py"
Search the following code lines:


# Loads label file, strips off carriage return

 label_lines = [line.rstrip () for line

                   in tf.gfile.GFile ("retrained_labels11.txt")]




 with tf.gfile.FastGFile ("retrained_graph11.pb", 'rb')

Modify there the route where you have saved the model that you have downloaded.
Now look for the following code lines at the beginning of the file:
#if you use a video place your video here:
video = 'march.mp4'
#if you use a video uncomment this line:
#cam = cv2.VideoCapture (video)
# This line is to make the detection in real time through your camera, comment on it if you do it with video:
cam = cv2.VideoCapture (0)

There, comment or uncomment the code according to your need if you want to do it in real time with a camera or if you want to do the detection from a video.

To execute your code:
python recognition.py
You should first see the prediction that corresponds to the type of pest you are detecting.


You can use the file: labelimage.py if you want to do the detection with photos, you can do it in the following way:
python labelimage.py "path of the image you want to try"

If you want to train a new moidelo, use the retrain.py file and follow the steps below:

https://github.com/VikramTiwari/tensorflow-retrain-sample

happy hacking!


Para usar mi codigo, debes tener instalado tensorflow y opencv.
Podras detectar las siguientes plagas o te dira si tu planta está sana:

araña  del tomate

frambuesa sana

mancha foliar isariopisis uva

mancha hoja gris maiz

mnanzana saludable

roña de manzana de cedro

moho polvoriento hojas verdes

tomate virus mosaico

cereza saludable

tizon norte o hoja maiz

melocoton sano

cereza hongo podosphaera clandestina

enverdecimiento naranja

tizon tardio tomate

punto bacteriano tomate

uva sana

moho comun maiz

molde de hoja tomate

mancha bacteriana pimientos

pudredumbre negra uva

tizon temprano tomate

fresa sana

mancha hoja tomate

sarampion de uva

virus de curl hoja amarilla tomate

fresa hoja chamuscada

papa sana

pudredumbrenegraenmanzanas

arandanos saludables

tizon tardio papa

pimiento saludable

tomate sano

tizon temprano papa

costramanzana

punto de enfoque tomate

soja sana

maiz saludable

mancha bacteriana melocoton

Si estás en una raspberry pi puedes seguir este tutorial para instalar tensorflow:
https://www.tensorflow.org/install/install_raspbian
O sigue estos pasos si estás en Ubuntu:
https://www.tensorflow.org/install/install_linux
Puedes seguir esta guia para compilar opencv en raspberry:
https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
Una vez que tengas instalado tensorflow y opencv, descarga mi modelo ya entrenado:
https://drive.google.com/drive/folders/1sowAcyeYXFCnhekE-WSOxUt5PASTijLq
ahora deberas abrir y editar el archivo: "recognition.py"
Busca en el las siguientes lineas de codigo:


# Loads label file, strips off carriage return

 label_lines = [line.rstrip() for line

                   in tf.gfile.GFile("retrained_labels11.txt")]




 with tf.gfile.FastGFile("retrained_graph11.pb", 'rb')

Modifica alli la ruta donde has guardo el modelo que te has descargado.
Ahora busca al incio del mismo archivo las siguientes lineas de codigo:
#if you use a video place your video here:
video = 'marcha.mp4'
#if you use a video uncomment this line:
#cam = cv2.VideoCapture(video)
# This line is to make the detection in real time through your camera, comment on it if you do it with video:
cam = cv2.VideoCapture(0) 

Allí comenta o descomenta el codigo segun tu necesidad si quieres hacerlo en tiempo real con una camara o si quieres hacer la detección desde un video.

Para ejecutar tu codigo:
python recognition.py
Deberas ver en primer lugar la predicción que corresponde al tipo de plaga que esta detectando.


Puedes usar el archivo: labelimage.py si quieres hacer la deteccón con fotos, puedes hacerlo de la siguiente manera:
python labelimage.py "ruta de la imagen que quieres probar"

Si quieres entrenar un moidelo nuevo usa el archivo retrain.py y sigue los siguientes pasos:

https://github.com/VikramTiwari/tensorflow-retrain-sample

Feliz hacking!


