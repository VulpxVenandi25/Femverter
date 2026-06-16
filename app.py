import os
import sys
import webview

from api.converter_api import ConverterApi


def main():
    api = ConverterApi()
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gui")
    url = os.path.join(gui_dir, "index.html")

    webview.create_window(
        "Femverter - Conversor de Imágenes",
        url,
        js_api=api,
        width=600,
        height=440,
        resizable=False,
    )
    webview.start()


if __name__ == "__main__":
    main()
