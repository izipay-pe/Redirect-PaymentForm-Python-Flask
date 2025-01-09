from flask import Flask, request, render_template, redirect, url_for, json
from datetime import datetime
import base64
import requests
import json
import hmac
import hashlib
from controller import dataForm
from controller import checkSignature

app = Flask(__name__)

# Manejo de solicitudes GET para la ruta raíz
@app.get('/')
def index():
    # Generar un número de orden
    order = datetime.now().strftime("Order-%Y%m%d%H%M%S")
    args = request.args
    # Renderizar el template y enviar el orderID
    return render_template('index.html', data={"order": order})

# Manejo de solicitudes POST para la ruta checkout
@app.post('/checkout')
def formulario():
    
    # Obtener todos los datos enviados por POST
    checkoutParameters = request.form.to_dict()
    # Obtener la cantidad
    amount = checkoutParameters["amount"]
    
    # Calcular el Signature y los valores dinámicos para el formulario
    formParams = dataForm(checkoutParameters)
    
    # Renderiza el template enviando los valores para el formulario de pago
    return render_template("checkout.html", parameters=formParams, amount=amount)


# Manejo de solicitudes POST para la ruta result
@app.post('/result')
def paidResult():
    if not request.form: raise Exception("no post data received!")

    resultParameters = request.form.to_dict()
    
    if not checkSignature(resultParameters) : raise Exception("Invalid signature")

    # Formatear los datos a Pretty Json
    pjson = json.dumps(resultParameters, indent=2, ensure_ascii=False)
    
    return render_template('result.html', data = resultParameters, pjson=pjson)

# Manejo de solicitudes POST para la ruta ipn
@app.post('/ipn')
def ipn():
    if not request.form: raise Exception("no post data received!")

    ipnParameters = request.form.to_dict()
    
    if not checkSignature(ipnParameters) : raise Exception("Invalid signature")

    # Obtener el estado de la transacción
    orderStatus = ipnParameters["vads_trans_status"]
    
    # Retorna la respuesta del Order Status
    return 'OK! OrderStatus is ' + orderStatus, 200

if __name__ == '__main__':
    app.run(debug=True)
