import hmac
import hashlib
import base64
import json
from key import credentials
from datetime import datetime
from collections import OrderedDict
from decimal import Decimal

def dataForm(parameters):
    # Obteniendo usuario
    username = credentials["SHOP_ID"]

    # Crear un diccionario ordenado para los parámetros
    new_params = OrderedDict()

    # Definir los parámetros vads_ y sus valores
    new_params = {
            "vads_action_mode": "INTERACTIVE",
            "vads_ctx_mode": "TEST",  # TEST O PRODUCTION
            "vads_page_action": "PAYMENT",
            "vads_payment_config": "SINGLE",
            "vads_url_success": "http://127.0.0.1:5000/result",
            "vads_return_mode": "POST",
            "vads_site_id": username,  # ID de tienda
            "vads_cust_first_name": parameters["firstName"],
            "vads_cust_last_name": parameters["lastName"],
            "vads_cust_email": parameters["email"],
            "vads_cust_cell_phone": parameters["phoneNumber"],
            "vads_cust_address": parameters["address"],
            "vads_cust_country": parameters["country"],
            "vads_cust_state": parameters["state"],
            "vads_cust_city": parameters["city"],
            "vads_cust_zip": parameters["zipCode"],
            "vads_order_id": parameters["orderId"],
            "vads_amount": int(Decimal(parameters["amount"]) * 100),
            "vads_currency": parameters["currency"],
            "vads_cust_national_id": parameters["identityCode"],
        }


    # Generar vads_trans_date con la fecha actual (en formato YmdHis)
    trans_date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    new_params["vads_trans_date"] = trans_date

    # Generar vads_trans_id como un hash de tiempo
    trans_id = hex(int(datetime.utcnow().timestamp() * 1000))[-6:]
    new_params["vads_trans_id"] = trans_id

    new_params["vads_version"] = "V2"
    new_params["vads_redirect_success_timeout"] = "5"  # Tiempo de redirección

    # Calcular el signature
    signature = calculateSignature(new_params)

    # Agregar el signature
    new_params["signature"] = signature

    # Retornar los parámetros
    return new_params
    
def calculateSignature(parameters):
    # Obtener la clave API
    key = credentials["KEY"]

    # Ordenar los parámetros alfabéticamente
    sort_parameters = {k: parameters[k] for k in sorted(parameters)}

    # Crear el contenido para la firma
    content_signature = "".join(
        f"{value}+" for key, value in sort_parameters.items() if key.startswith("vads_")
    )
    content_signature += key
    
    # Calcular Firma
    hash_object = hmac.new(key.encode('utf-8'), content_signature.encode('utf-8'), hashlib.sha256)
    hash_bytes = hash_object.digest()
    signature = base64.b64encode(hash_bytes).decode('utf-8')
    
    # Retornar Firma
    return signature

def checkSignature(parameters):
    # Obtener el signature de la respuesta
    signature = parameters["signature"]

    # Verifica la integridad de el signature recibido y el generado
    return signature == calculateSignature(parameters) 
