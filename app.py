'''
#importer le package Image de la bibliothèque Pillow
from PIL import Image

#importer la librairie pour la boite de dialogue
from tkinter.filedialog import askopenfilename

#récupérer le chemin de l'image via la boite de dialogue
chemin=askopenfilename(file='hih.jpg', filetypes=[('JPEG files','.jpg'),('all files','.*')])

#lire l'image
imageLue = Image.open(chemin)

#Afficher l'image
imageLue.show()
'''

'''

#importer le package Image de la bibliothèque Pillow
from PIL import Image

# lire l'image '4.jpg' *
# Copier le dossier 'train' dans votre espace de travail
imageLue = Image.open('train\4.jpg')

#Afficher l'image
imageLue.show()
'''
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import pyqrcode
import requests
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def index(X='index.html', link = "www.google.com", TEXT = "Hi, choose", TEXTdeux = "your text!"):
    response = requests.get(
        "https://storeuk.taylorswift.com/cdn/shop/products/SWIFT_SNLLHOODIE_BACK.png?v=1692041046&width=1000")
    if response.status_code == 200:
        print("-"+link+"-", "Link", type(link))
        if (link!="" and link!="None"):
            print("encore moi")
            img = Image.open(BytesIO(response.content))
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype("Agbalumo-Regular.ttf", size=50)  # Use a default font
            d1.text((370, 450), TEXT, font=myFont, fill=(0, 0, 0))
            d1.text((370, 500), TEXTdeux, font=myFont, fill=(0, 0, 0))
            qr_code = pyqrcode.create(link)
            qr_code.png("static/QRCode.png", scale=7)
            img222 = Image.open("static/QRCode.png").convert("RGBA")
            img2=img222.resize([230,230])
            enhancer = ImageEnhance.Brightness(img2)
            img2 = enhancer.enhance(1)  # Adjust the brightness to 70% of the original
            enhancer = ImageEnhance.Contrast(img2)
            img2 = enhancer.enhance(0.82)  # Increase the contrast by 20%
            img.paste(img2, (380, 570))
            img.save("static/image.png")

            return render_template(X)
        else:
            print("Wesh elle est ou louou")
            responseLoulou = requests.get(
                "https://ih1.redbubble.net/image.5169692417.2177/aps,504x498,medium,transparent-pad,600x600,f8f8f8.jpg")
            responseLoulouO = requests.get(
                "https://ih1.redbubble.net/image.5169692417.2177/aps,504x498,medium,transparent-pad,600x600,f8f8f8.jpg")
            img = Image.open(BytesIO(response.content))
            FINOLoulou = Image.open(BytesIO(responseLoulouO.content))
            FINOLoulou.save("static/ImageLoulouFin.png")
            img222 = Image.open(BytesIO(responseLoulou.content))
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype("Agbalumo-Regular.ttf", size=50)  # Use a default font
            d1.text((370, 450), TEXT, font=myFont, fill=(0, 0, 0))
            d1.text((370, 500), TEXTdeux, font=myFont, fill=(0, 0, 0))
            img2 = img222.resize([230, 230])
            enhancer = ImageEnhance.Brightness(img2)
            img2 = enhancer.enhance(1)  # Adjust the brightness to 70% of the original
            enhancer = ImageEnhance.Contrast(img2)
            img2 = enhancer.enhance(0.82)  # Increase the contrast by 20% QRCOULOULOUOU
            img.paste(img2, (380, 570))
            img.save("static/ImageLoulou.png")

            return render_template("indexLoulou.html")
    else:
        print("Failed to retrieve the image. Status code:", response.status_code)


@app.route('/', methods=['POST', 'GET'])  # Allow both GET and POST methods
def submit():
    global Number
    global data
    data=request.form
    print(request.form)
    if request.method == 'POST':
        if 'first_line' in request.form:
            print("a1")# Si le formulaire avec l'ID postForm a été soumis
            # Traiter les données de ce formulaire ici
            return redirect(url_for('successtwo'))  # Rediriger vers la fonction successTwo
        elif 'parameterXYZ' in request.form:
            print("JE suis la")
            didi=request.form
            Number = didi.get('parameterXYZ')
            print(Number, "Number ini")
            if Number == "":
                Number = int(0)
                print("Changed to 0")
            if int(Number) > 0 :
                print(Number, ">0")
                print("2a")# Si le formulaire avec l'ID getForm a été soumis
                # Traiter les données de ce formulaire ici
                return redirect(url_for('success'))  # Rediriger vers la fonction success
            else:
                print("back")
                return index(X='HTMLError.html', link = "www.google.com", TEXT = "Hi, choose", TEXTdeux = "your text!")
        elif 'parameterXYZLOULOU' in request.form:
            didi = request.form
            Number = didi.get('parameterXYZLOULOU')
            print(Number, "Number ini")
            if Number == "":
                Number = int(0)
                print("Changed to 0")
            if int(Number) > 0:
                print(Number, ">0")
                print("2a")  # Si le formulaire avec l'ID getForm a été soumis
                # Traiter les données de ce formulaire ici
                return redirect(url_for('successLOULOU'))  # Rediriger vers la fonction success
            else:
                print("back")
                return index(X='HTMLError.html', link = "www.google.com", TEXT = "Hi, choose", TEXTdeux = "your text!")
        elif "fsurnamePipipi" in request.form.keys():
            print("3a")# Si le formulaire avec l'ID getForm a été soumis
            # Traiter les données de ce formulaire ici
            return redirect(url_for('successtrois'))  # Rediriger vers la fonction success
        elif  "fsurnameLoulou" in request.form.keys():
            print("3a")# Si le formulaire avec l'ID getForm a été soumis
            # Traiter les données de ce formulaire ici
            return redirect(url_for('successtroisLOULOU'))
        else:
            return "Méthode non autorisée"  # Gérer d'autres cas si nécessaire
    else:
        return "Méthode non autorisée"  # Gérer d'autres cas si nécessaire


@app.route('/templates/index1', methods=['GET', 'POST'])
def successtwo():
    print("2")
    print(data)
    flin = data.get("first_line")
    slin = data.get("second_line")
    QR = str(data.get("qrcode"))
    print("-"+QR+"-", "COup dur pour lui")
    global QRR
    QRR = ""
    if QR =="None":
        QR=""
    if QR !="":
        if QR !="":
            QRR=QR
        global fline
        fline = ""
        if flin != "":
            fline = flin
        global sline
        sline=""
        if slin != "":
            sline = slin
        print("-"+QRR+"-", "Valeur11111", type(QRR))
        return index(X='index.html', link = QRR, TEXT = fline, TEXTdeux = sline)
    else:
        print("passage secret")
        QRdeux = str(data.get("qrcodedeux"))
        QRR = ""
        if QRdeux !="":
            QRR=QRdeux
        fline = ""
        if flin != "":
            fline = flin
        sline=""
        if slin != "":
            sline = slin
        print("-"+QRR+"-", "Valeur222", type(QRR))
        return index(X='index.html', link = QRR, TEXT = fline, TEXTdeux = sline)

@app.route('/templates/Paiement_file.html', methods=['POST', 'GET'])
def success():
    print("1")
    return render_template("Paiement_file.html")
@app.route('/templates/PaiementLoulou.html', methods=['POST', 'GET'])
def successLOULOU():
    print("1")
    return render_template("PaiementLoulou.html")

@app.route('/templates/index1.html', methods=['POST', 'GET'])
def successtrois():
    print("Bravo NIco")
    return render_template("index1.html", Number=Number)

@app.route('/templates/index1Loulou.html', methods=['POST', 'GET'])
def successtroisLOULOU():
    print("Bravo NIco Loulou")
    return render_template("index1Loulou.html", Number=Number)






if __name__ == '__main__':
    app.run(debug=True)
'''
import pyqrcode
from PIL import Image
link = input("Enter your link to generate a QR code: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
img = Image.open("QRCode.png")
img.show()

'''
