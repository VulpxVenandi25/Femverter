# README - Conversor de Imágenes

## 📌 Descripción

Este es un programa en Python con interfaz gráfica que permite convertir múltiples imágenes a un formato específico. La aplicación soporta arrastrar y soltar archivos, selección manual de imágenes y conversión a varios formatos populares.

## 🛠️ Características principales

- Interfaz gráfica intuitiva basada en PyQt5
- Soporte para arrastrar y soltar imágenes
- Conversión a múltiples formatos (PNG, JPEG, WEBP, BMP, GIF, TIFF)
- Visualización de la lista de imágenes seleccionadas
- Selección de carpeta de destino para las imágenes convertidas
- Mensajes de retroalimentación durante el proceso

## 📦 Dependencias

El programa requiere las siguientes bibliotecas de Python:

- PyQt5 (para la interfaz gráfica)
- Pillow (para el procesamiento de imágenes)

Puedes instalarlas con:

```bash
pip install PyQt5 pillow
```

## 🏗️ Estructura del código

### Componentes principales

1. **Clase `ImageConverterApp` (QMainWindow)**

   - Clase principal que hereda de QMainWindow
   - Contiene toda la lógica de la interfaz y conversión

2. **Métodos principales**

   - `init_ui()`: Configura los elementos de la interfaz
   - `dragEnterEvent()` y `dropEvent()`: Manejan el arrastrar y soltar
   - `is_image_file()`: Verifica si un archivo es una imagen válida
   - `set_output_format()`: Establece el formato de salida
   - `select_images()`: Abre el diálogo para seleccionar imágenes
   - `convert_images()`: Realiza la conversión de formatos
   - `clear_list()`: Limpia la lista de imágenes seleccionadas

3. **Widgets de la interfaz**
   - `QLabel`: Área para arrastrar y soltar imágenes
   - `QListWidget`: Muestra la lista de imágenes seleccionadas
   - `QComboBox`: Selector de formato de salida
   - `QPushButton`: Botones para seleccionar, convertir y limpiar

## 🖼️ Formatos soportados

### Formatos de entrada:

- PNG (.png)
- JPEG (.jpg, .jpeg)
- WEBP (.webp)
- BMP (.bmp)
- GIF (.gif)
- TIFF (.tiff)

### Formatos de salida:

- PNG
- JPEG
- WEBP
- BMP
- GIF
- TIFF

## 🚀 Cómo ejecutar el programa

1. Clona o descarga el repositorio
2. Instala las dependencias con `pip install -r requirements.txt`
3. Ejecuta el archivo principal:

```bash
python image_converter.py
```

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Siéntete libre de modificarlo y distribuirlo según tus necesidades.

## 💡 Mejoras posibles

Algunas características que podrían añadirse:

- Opción para redimensionar imágenes durante la conversión
- Ajuste de calidad para formatos como JPEG
- Procesamiento por lotes con diferentes configuraciones
- Previsualización de imágenes antes de la conversión

---

Desarrollado con ❤️ usando Python, PyQt5 y Pillow. ¡Espero que te sea útil!
