import os

VALID_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp'}


def is_image_file(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() in VALID_EXTENSIONS


def get_valid_extension_filter():
    return "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp)"
