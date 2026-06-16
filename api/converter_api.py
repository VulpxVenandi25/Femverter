import os
import base64
import tempfile
import atexit
import shutil
import webview

from src.converter import convert_images
from src.image_utils import is_image_file


class ConverterApi:
    def __init__(self):
        self.image_paths = []
        self._temp_dir = tempfile.mkdtemp(prefix="femverter_")
        atexit.register(self._cleanup_temp)

    def _cleanup_temp(self):
        if os.path.isdir(self._temp_dir):
            shutil.rmtree(self._temp_dir, ignore_errors=True)

    def _normalize_path(self, raw):
        if isinstance(raw, (list, tuple)):
            return raw[0] if raw else ""
        return raw

    def select_images(self):
        window = webview.windows[0]
        result = window.create_file_dialog(
            webview.OPEN_DIALOG,
            allow_multiple=True,
            file_types=("Imágenes (*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff;*.webp)",),
        )
        if not result:
            return []

        paths = result if isinstance(result, (list, tuple)) else [result]
        valid = [f for f in paths if is_image_file(f) and f not in self.image_paths]
        self.image_paths.extend(valid)
        return [os.path.basename(f) for f in valid]

    def add_paths(self, paths):
        valid = [f for f in paths if is_image_file(f) and f not in self.image_paths]
        self.image_paths.extend(valid)
        return [os.path.basename(f) for f in valid]

    def add_files_data(self, files_data):
        added = []
        for f in files_data:
            try:
                header, encoded = f["data"].split(",", 1)
                data = base64.b64decode(encoded)
                name = os.path.basename(f["name"])
                tmp_path = os.path.join(self._temp_dir, name)
                # avoid name collision
                if os.path.exists(tmp_path):
                    root, ext = os.path.splitext(name)
                    tmp_path = os.path.join(
                        self._temp_dir, f"{root}_{len(self.image_paths)}{ext}"
                    )
                with open(tmp_path, "wb") as out:
                    out.write(data)
                if is_image_file(tmp_path):
                    self.image_paths.append(tmp_path)
                    added.append(name)
            except Exception:
                pass
        return added

    def convert(self, output_format):
        if not self.image_paths:
            return {"ok": False, "msg": "No hay imágenes para convertir."}

        window = webview.windows[0]
        output_dir = self._normalize_path(
            window.create_file_dialog(webview.FOLDER_DIALOG)
        )
        if not output_dir:
            return {"ok": False, "msg": "No se seleccionó carpeta de destino."}

        converted, errors = convert_images(self.image_paths, output_format, output_dir)

        total = len(self.image_paths)
        self.image_paths = []

        msg = f"Se convirtieron {converted} de {total} imágenes a {output_format}."
        if errors:
            msg += "\n\nErrores:\n" + "\n".join(errors)

        return {"ok": True, "msg": msg}

    def clear_list(self):
        self.image_paths = []
