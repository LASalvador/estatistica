import statistics
from flask import Flask, request, json, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    content = request.json
    listax = content['x']
    listay = content['y']

    modax = moda(x)
    moday = moda(y)
    mediax = media(x)
    mediay = media(y)
    mediaGx = mediaGeometrica(x)
    mediaGy = mediaGeometrica(y)
    mediaHx = mediaHarmonica(x)
    mediaHy = mediaHarmonica(y)
    medX = mediana(x)
    medY = mediana(y)
    dpX = desvioPadrao(x)
    dpY = desvioPadrao(y)
    vX = variancia(x)
    vY = variancia(y)


    response = jsonify({
        "modax":modax,
        "moday":moday,
        "mediax":mediax,
        "mediay":mediay,
        "mediaGx":mediaGx,
        "mediaGy":mediaGy,
        "mediaHx":mediaHx,
        "mediaHy":mediaHy,
        "medX":medX,
        "medY":medY,
        "dpX":dpX,
        "dpY":dpY,
        "vX":vX,
        "vY":vY
    })

    return 'Server Works!'

# Medidas tendencia central
def moda(lista):
    return statistics.mode(lista)

def media(lista):
    return statistics.mean(lista)

def mediaGeometrica(lista):
    return statistics.geometric_mean(lista)

def mediaHarmonica(lista):
    return statistics.harmonic_mean(lista)

def mediana(lista):
    return statistics.median(lista)
# Medidas de dispersao
def desvioPadrao(lista):
    return statistics.pstdev(lista)

def variancia(lista):
    return statistics.pvariance(lista)