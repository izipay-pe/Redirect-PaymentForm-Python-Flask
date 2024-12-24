from flask import Flask, request, render_template, redirect, url_for, json
from datetime import datetime
import base64
import requests
import json
import hmac
import hashlib
from controller import dataForm
from controller import calcularSignature

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
    # Obtener el valor de la moneda y la cantidad
    currency = checkoutParameters["currency"]
    amount = checkoutParameters["amount"]
    
    # Asignar el tipo de moneda correspondiente
    if (currency == "604"):
        currencyType = "Soles"
    else:
        currencyType = "Dólares"
    
    # Calcular el Signature y los valores dinámicos para el formulario
    formParams = dataForm(checkoutParameters)
    
    # Renderiza el template enviando los valores para el formulario de pago
    return render_template("checkout.html", parameters=formParams, currency=currencyType, amount=amount)


# Manejo de solicitudes POST para la ruta result
@app.post('/result')
def paidResult():
    
    # Asignando los valores de la respuesta de Izipay en un diccionario
    resultParameters = request.form.to_dict()
    # Obtener el signature de la respuesta
    resultPostSignature = resultParameters["signature"]
    # Calcular el signature con los valores de la transacción
    resultSignature = calcularSignature(resultParameters)
    # Obtener el valor de la moneda
    currency = resultParameters["vads_currency"]
    # Formatear los datos a Pretty Json
    pjson = json.dumps(resultParameters, indent=2, ensure_ascii=False)
    
    # Asignar el tipo de moneda correspondiente
    if (currency == "604"):
        currencyType = "PEN"
    else:
        currencyType = "USD"
    
    # Verifica la integridad de el signature recibido y el generado
    if resultPostSignature == resultSignature:
        return render_template('result.html', data = resultParameters, pjson=pjson, currency=currencyType)
    else:
        return 'ERROR', 500

# Manejo de solicitudes POST para la ruta ipn
@app.post('/ipn')
def ipn():
    
    # Asignando los valores de la respuesta de Izipay en un diccionario
    ipnParameters = request.form.to_dict()
    # Obtener el signature de la respuesta
    ipnPostSignature = ipnParameters["signature"]
    # Calcular el signature con los valores de la transacción
    ipnSignature = calcularSignature(ipnParameters)
    # Obtener el estado de la trasnacción
    orderStatus = ipnParameters["vads_trans_status"]
    
    # Verifica la integridad del signature recibido y el generado
    if ipnPostSignature == ipnSignature:
        print("OK! Order Status is " + orderStatus )
        return 'Correcto', 200
    else:
        print("Notification Error")
        return 'Acceso denegado', 500

if __name__ == '__main__':
    app.run(debug=True)
