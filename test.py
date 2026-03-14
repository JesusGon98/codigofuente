# Importamos la librería qrcode que permite generar códigos QR en Python
import qrcode


# Lista de datos que se utilizarán para generar los códigos QR
# Cada elemento contiene:
# - name: el texto que se codificará en el QR
# - fillcolor: color del QR
# - backcolor: color del fondo del QR
data = [
    {"name": "Jesus",
     "fillcolor": "black",
     "backcolor": "white"}, 

    {"name": "Maria",
     "fillcolor": "purple",
     "backcolor": "white"}, 

    {"name": "Jose",
     "fillcolor": "blue",
     "backcolor": "white"}, 

    {"name": "Pedro",
     "fillcolor": "pink",
     "backcolor": "white"}, 

    {"name": "Pablo",
     "fillcolor": "red",
     "backcolor": "white"}, 

    {"name": "Santiago",
     "fillcolor": "orange",
     "backcolor": "white"}
]


# Recorremos cada elemento de la lista para generar un QR por cada nombre
for elemento in data:

    # Se crea el objeto QRCode con diferentes configuraciones
    qr = qrcode.QRCode(
        version=1,  # Define el tamaño del QR (1 es el más pequeño)
        
        # Nivel de corrección de errores del QR
        # Permite que el QR pueda leerse incluso si está parcialmente dañado
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        
        box_size=10,  # Tamaño de cada "cuadro" del QR
        
        border=4,  # Grosor del borde blanco alrededor del QR
    )

    # Se agrega la información que se convertirá en código QR
    # En este caso se usa el nombre de la persona
    qr.add_data(elemento["name"])

    # Genera la estructura final del QR
    # fit=True permite que el QR se ajuste automáticamente al contenido
    qr.make(fit=True)


    # Se genera la imagen del QR usando los colores definidos en el diccionario
    img = qr.make_image(
        fill_color=elemento["fillcolor"],  # Color del código QR
        back_color=elemento["backcolor"]   # Color de fondo
    )


    # Se guarda la imagen del QR en formato PNG
    # El nombre del archivo será el nombre de la persona
    # Ejemplo: Jesus.png, Maria.png, etc.
    img.save(f'{elemento["name"]}.png')