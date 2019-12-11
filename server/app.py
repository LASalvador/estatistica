import statistics
from flask import Flask, request, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculo', methods = ['POST'])
def index():
    content = request.json
    listax = content['x']
    listay = content['y']

    mediax = media(listax)
    mediay = media(listay)
    mediaHx = mediaHarmonica(listax)
    mediaHy = mediaHarmonica(listay)
    medX = mediana(listax)
    medY = mediana(listay)
    dpX = desvioPadrao(listax)
    dpY = desvioPadrao(listay)
    vX = variancia(listax)
    vY = variancia(listay)
    
    response = jsonify({
        "mediax" : mediax,
        "mediay" : mediay,
        "mediaHx" : mediaHx,
        "mediaHy" : mediaHy,
        "medX" : medX,
        "medY" : medY,
        "dpX" : dpX,
        "dpY" : dpY,
        "vX" : vX,
        "vY" : vY
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Medidas tendencia central
def media(lista):
    return statistics.mean(lista)

def mediaHarmonica(lista):
    return statistics.harmonic_mean(lista)

def mediana(lista):
    return statistics.median(lista)
# Medidas de dispersao
def desvioPadrao(lista):
    return statistics.pstdev(lista)

def variancia(lista):
    return statistics.pvariance(lista)