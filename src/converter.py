import os
from PIL import Image

from src.image_utils import is_image_file


def convert_images(image_paths, output_format, output_dir):
    converted = 0
    errors = []

    for file_path in image_paths:
        try:
            img = Image.open(file_path)
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            ext = output_format.lower()
            output_path = os.path.join(output_dir, f"{base_name}.{ext}")

            save_kwargs = {"format": output_format}
            if output_format.upper() == "JPEG":
                save_kwargs["quality"] = 95

            img.save(output_path, **save_kwargs)
            converted += 1
        except Exception as e:
            errors.append(f"{os.path.basename(file_path)}: {e}")

    return converted, errors
