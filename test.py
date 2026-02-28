import qrcode

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


for elemento in data:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(elemento["name"])
    qr.make(fit=True)

    img = qr.make_image(fill_color=elemento["fillcolor"], back_color=elemento["backcolor"])
    img.save(f'{elemento["name"]}.png')