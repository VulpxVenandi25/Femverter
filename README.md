# README - Conversor de Imágenes (Femverter)

## Descripción

Programa en Python con interfaz gráfica (pywebview) que convierte múltiples imágenes entre formatos. Soporta arrastrar y soltar, selección manual y conversión a varios formatos populares.

## Características

- Interfaz basada en HTML+CSS+JS con pywebview
- Arrastrar y soltar imágenes (compatible con WebView2 y CEF)
- Conversión a PNG, JPEG, WEBP, BMP, GIF, TIFF
- Lista de imágenes seleccionadas
- Selección de carpeta de destino
- Mensajes de retroalimentación

## Dependencias

- pywebview (interfaz nativa con WebView2/CEF)
- Pillow (procesamiento de imágenes)

```bash
pip install -r requirements.txt
```

## Estructura del proyecto

```
Femverter/
├── app.py                  # Punto de entrada
├── api/
│   └── converter_api.py    # API bridge expuesta a JavaScript
├── gui/
│   ├── index.html          # Cuerpo de la interfaz
│   ├── style.css           # Estilos
│   └── script.js           # Lógica del cliente (drag & drop, UI)
├── src/
│   ├── image_utils.py      # Validación de extensiones
│   └── converter.py        # Conversión con Pillow
└── requirements.txt
```

## Formatos soportados

| Entrada                              | Salida                          |
| ------------------------------------ | ------------------------------- |
| PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP | PNG, JPEG, WEBP, BMP, GIF, TIFF |

## Cómo ejecutar

```bash
python app.py
```

## Licencia

MIT. Siéntete libre de modificarlo y distribuirlo.

---

Desarrollado con Python, pywebview y Pillow.
