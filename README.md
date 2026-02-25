<div align="center">

# 🌱 Detección de Plagas en Plantas con TensorFlow

### Sistema de detección de plagas usando Deep Learning e Inteligencia Artificial

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Detección automática de plagas en plantas comestibles usando visión por computadora**

[🚀 Inicio Rápido](#-inicio-rápido) • [📋 Características](#-características) • [⚙️ Instalación](#️-instalación) • [🎯 Uso](#-uso)

</div>

---

## 📋 Características

- 🔍 **Detección en Tiempo Real** - Análisis en vivo con cámara
- 📸 **Análisis de Imágenes** - Procesamiento de fotos estáticas
- 🎥 **Procesamiento de Video** - Detección en archivos de video
- 🤖 **IA Avanzada** - Modelo entrenado con TensorFlow y MobileNet
- 📱 **Compatible con Android** - Modelo optimizado para dispositivos móviles
- 🍓 **Múltiples Especies** - Soporta más de 30 tipos de plantas y plagas

---

## 🌿 Plantas y Plagas Soportadas

El sistema puede detectar plagas en las siguientes especies:

### Plantas Soportadas

- 🥔 **Papa** - Early/Late blight, pudrición negra
- 🍅 **Tomate** - Mosaico, tizón tardío, mancha bacteriana, moho
- 🍒 **Cereza** - Hongo podosphaera, manchas
- 🍊 **Naranjo** - Enverdecimiento (greening)
- 🌽 **Maíz** - Mancha gris, moho común, tizón del norte
- 🍇 **Uva** - Mancha isariopisis, podredumbre negra, sarampión
- 🍎 **Manzana** - Sarna de cedro, costra, pudrición negra
- 🍑 **Durazno** - Mancha bacteriana
- 🫐 **Arándano** - Varias enfermedades
- 🌶️ **Pimiento** - Mancha bacteriana
- 🍓 **Fresa** - Hoja chamuscada
- 🌾 **Soja** - Varias enfermedades

**Y muchas más...** (Más de 30 tipos diferentes)

### Lista Completa de Plagas Detectables

\`\`\`
Spider tomato
healthy raspberry
leaf spot isariopisis grape
stain leaf gray corn
Healthy manzana
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
\`\`\`

---

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.7+
- TensorFlow instalado
- OpenCV instalado
- Cámara (opcional, para detección en tiempo real)

### Instalación Rápida

\`\`\`bash
# Clonar el repositorio
git clone https://github.com/daletoniris/deteccion-de-plagas-en-plantas-con-tensorflow.git
cd deteccion-de-plagas-en-plantas-con-tensorflow

# Instalar dependencias
pip install tensorflow opencv-python
\`\`\`

---

## ⚙️ Instalación Detallada

### Instalar TensorFlow

#### En Raspberry Pi:
Sigue la guía oficial: [TensorFlow Installation for Raspberry Pi](https://www.tensorflow.org/install/install_raspbian)

#### En Ubuntu:
Sigue la guía oficial: [TensorFlow Installation for Linux](https://www.tensorflow.org/install/install_linux)

### Instalar OpenCV

#### En Raspberry Pi:
Sigue esta guía: [OpenCV Installation Guide for Raspberry Pi](https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/)

---

## 📥 Descargar Modelo Pre-entrenado

1. Descarga el modelo ya entrenado desde:
   \`\`\`
   https://drive.google.com/drive/folders/1sowAcyeYXFCnhekE-WSOxUt5PASTijLq
   \`\`\`

2. Extrae los archivos en el directorio del proyecto

---

## 🎯 Uso

### Configuración del Modelo

Edita el archivo \`recognition.py\` y modifica las rutas del modelo:

\`\`\`python
# Carga el archivo de etiquetas
label_lines = [line.rstrip() for line 
               in tf.gfile.GFile("retrained_labels11.txt")]

# Carga el modelo
with tf.gfile.FastGFile("retrained_graph11.pb", 'rb') as f:
    # Tu código aquí
\`\`\`

**Importante**: Actualiza las rutas según donde guardaste el modelo descargado.

### Configurar Fuente de Video

En \`recognition.py\`, configura según tu necesidad:

\`\`\`python
# Para usar un video:
video = 'march.mp4'
cam = cv2.VideoCapture(video)  # Descomenta esta línea

# Para detección en tiempo real con cámara:
# cam = cv2.VideoCapture(0)  # Descomenta esta línea
\`\`\`

### Ejecutar Detección

#### Detección en Tiempo Real o Video:
\`\`\`bash
python recognition.py
\`\`\`

#### Detección con Imágenes:
\`\`\`bash
python labelimage.py "ruta/de/la/imagen.jpg"
\`\`\`

---

## 🎓 Entrenar tu Propio Modelo

### Usar el Script de Reentrenamiento

1. Sigue esta guía para reentrenar el modelo:
   \`\`\`
   https://github.com/VikramTiwari/tensorflow-retrain-sample
   \`\`\`

2. Usa el archivo \`retrain.py\` incluido en el repositorio

### Dataset en Inglés

Si prefieres etiquetas en inglés, descarga el dataset original:
\`\`\`
https://github.com/salathegroup/plantvillage_deeplearning_paper_dataset/tree/master/raw/color
\`\`\`

---

## 📱 Uso en Dispositivos Móviles (Android)

### Optimizar Modelo para Mobile

El proyecto usa **MobileNet v1.0_224** para dispositivos móviles.

#### 1. Descargar MobileNet:
\`\`\`
https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md
\`\`\`

#### 2. Convertir a TensorFlow Lite:

\`\`\`bash
toco --input_file=tf_files/retrained_graph.pb \\
     --output_file=tf_files/optimized_graph.lite \\
     --input_format=TENSORFLOW_GRAPHDEF \\
     --output_format=TFLITE \\
     --input_shape="1,224,224,3" \\
     --input_array=input \\
     --output_array=final_result \\
     --inference_type=FLOAT \\
     --input_data_type=FLOAT
\`\`\`

#### 3. Integrar en Android Studio:

1. Descarga Android Studio:
   \`\`\`
   https://developer.android.com/studio/
   \`\`\`

2. Sigue esta guía para configurar:
   \`\`\`
   https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2-tflite/#3
   \`\`\`

3. Copia \`optimized_graph.lite\` a tu proyecto Android

---

## 📁 Estructura del Proyecto

\`\`\`
deteccion-de-plagas-en-plantas-con-tensorflow/
├── recognition.py          # Detección en tiempo real/video
├── labelimage.py          # Detección en imágenes
├── retrain.py             # Script de reentrenamiento
├── retrained_graph11.pb   # Modelo pre-entrenado (descargar)
├── retrained_labels11.txt # Etiquetas del modelo
└── README.md              # Este archivo
\`\`\`

---

## 🔧 Configuración Avanzada

### Ajustar Parámetros de Detección

En \`recognition.py\` puedes modificar:

- **Confianza mínima**: Umbral de confianza para mostrar detecciones
- **Resolución**: Tamaño de frame para procesamiento
- **FPS**: Velocidad de procesamiento

---

## 📊 Resultados Esperados

Al ejecutar el código, verás:

1. **Ventana de video** con la detección en tiempo real
2. **Etiqueta de la plaga** detectada
3. **Nivel de confianza** del modelo
4. **FPS** de procesamiento

---

## 🐛 Solución de Problemas

### Error: "No se encuentra el modelo"
- Verifica que descargaste el modelo desde Google Drive
- Confirma que las rutas en \`recognition.py\` son correctas

### Error: "OpenCV no detecta la cámara"
- Verifica que la cámara esté conectada
- Prueba cambiar el índice: \`cv2.VideoCapture(1)\` en lugar de \`0\`

### Error: "TensorFlow no se encuentra"
- Reinstala TensorFlow siguiendo la guía oficial
- Verifica la versión de Python (debe ser 3.7+)

---

## 🤝 Contribuir

Las contribuciones son bienvenidas! Puedes:

- 🐛 Reportar bugs
- 💡 Sugerir nuevas características
- 📝 Mejorar la documentación
- 🔧 Enviar pull requests

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo \`LICENSE\` para más detalles.

---

## 👤 Autor

**Daniel Dieser** - Investigador de Robótica e IA

- GitHub: [@daletoniris](https://github.com/daletoniris)
- Organizaciones: @initiasur, @NiperiaLab

---

## 🔗 Enlaces Útiles

- [TensorFlow Official](https://www.tensorflow.org/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [MobileNet Guide](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/index.html)
- [Plant Village Dataset](https://github.com/salathegroup/plantvillage_deeplearning_paper_dataset)

---

<div align="center">

**🌱 Protegiendo cultivos con Inteligencia Artificial**

[⭐ Dános una estrella si te gustó el proyecto](https://github.com/daletoniris/deteccion-de-plagas-en-plantas-con-tensorflow)

**¡Feliz hacking! 🚀**

</div>
