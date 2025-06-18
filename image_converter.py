import os
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, 
                             QWidget, QComboBox, QPushButton, QFileDialog, 
                             QMessageBox, QListWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PIL import Image


class ImageConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Imágenes")
        self.setGeometry(100, 100, 600, 400)
        
        # Variables
        self.image_paths = []
        self.output_format = "PNG"
        
        # Crear widgets
        self.init_ui()
        
    def init_ui(self):
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QVBoxLayout()
        
        # Etiqueta de instrucciones
        self.label = QLabel("Arrastra y suelta imágenes aquí o haz clic en 'Seleccionar imágenes'")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaa;
                padding: 20px;
                margin: 10px;
            }
        """)
        self.label.setAcceptDrops(True)
        layout.addWidget(self.label)
        
        # Lista de imágenes seleccionadas
        self.image_list = QListWidget()
        self.image_list.setMaximumHeight(100)
        layout.addWidget(self.image_list)
        
        # Selector de formato de salida
        self.format_combo = QComboBox()
        self.format_combo.addItems(["PNG", "JPEG", "WEBP", "BMP", "GIF", "TIFF"])
        self.format_combo.currentTextChanged.connect(self.set_output_format)
        layout.addWidget(QLabel("Formato de salida:"))
        layout.addWidget(self.format_combo)
        
        # Botón para seleccionar imágenes
        self.select_button = QPushButton("Seleccionar imágenes")
        self.select_button.clicked.connect(self.select_images)
        layout.addWidget(self.select_button)
        
        # Botón para convertir
        self.convert_button = QPushButton("Convertir imágenes")
        self.convert_button.clicked.connect(self.convert_images)
        layout.addWidget(self.convert_button)
        
        # Botón para limpiar lista
        self.clear_button = QPushButton("Limpiar lista")
        self.clear_button.clicked.connect(self.clear_list)
        layout.addWidget(self.clear_button)
        
        # Configurar layout
        central_widget.setLayout(layout)
        
        # Permitir arrastrar y soltar
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            
    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if self.is_image_file(file_path):
                if file_path not in self.image_paths:
                    self.image_paths.append(file_path)
                    self.image_list.addItem(os.path.basename(file_path))
            else:
                QMessageBox.warning(self, "Advertencia", f"El archivo {os.path.basename(file_path)} no es una imagen válida.")
        
    def is_image_file(self, file_path):
        valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
        return file_path.lower().endswith(valid_extensions)
        
    def set_output_format(self, format):
        self.output_format = format
        
    def select_images(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Seleccionar imágenes", "", 
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp)"
        )
        
        if files:
            for file_path in files:
                if file_path not in self.image_paths:
                    self.image_paths.append(file_path)
                    self.image_list.addItem(os.path.basename(file_path))
        
    def convert_images(self):
        if not self.image_paths:
            QMessageBox.warning(self, "Advertencia", "No hay imágenes para convertir.")
            return
            
        # Pedir directorio de salida
        output_dir = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta de destino")
        if not output_dir:
            return
            
        # Convertir cada imagen
        success_count = 0
        for image_path in self.image_paths:
            try:
                # Abrir la imagen
                img = Image.open(image_path)
                
                # Crear nombre de archivo de salida
                base_name = os.path.splitext(os.path.basename(image_path))[0]
                output_path = os.path.join(output_dir, f"{base_name}.{self.output_format.lower()}")
                
                # Guardar en el nuevo formato
                if self.output_format == "JPEG":
                    img.save(output_path, "JPEG", quality=95)
                else:
                    img.save(output_path, self.output_format)
                
                success_count += 1
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo convertir {os.path.basename(image_path)}: {str(e)}")
        
        # Mostrar resultado
        QMessageBox.information(
            self, "Conversión completada", 
            f"Se convirtieron {success_count} de {len(self.image_paths)} imágenes a {self.output_format}."
        )
        
    def clear_list(self):
        self.image_paths.clear()
        self.image_list.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageConverterApp()
    window.show()
    sys.exit(app.exec_())