from flask import Flask, request, render_template
from datetime import datetime
import base64
import time
import hmac
import hashlib
from configKey import SHOP_ID, MODE, KEY, URL_IZIPAY

app = Flask(__name__)


def get_signature(params, keys):
    content_signature = ""
    sorted_params = sorted(params.items(), key=lambda x: x[0])
    for name, value in sorted_params:
        if name.startswith('vads_'):
            content_signature += value + "+"
    content_signature += keys
    hash_object = hmac.new(keys.encode('utf-8'), content_signature.encode('utf-8'), hashlib.sha256)
    signature = base64.b64encode(hash_object.digest()).decode('utf-8')
    return signature

@app.get('/')
def index():
    order = datetime.now().strftime("Order-%Y%m%d%H%M%S")
    args = request.args
    return render_template('home.html', data={"order": order})


@app.post('/redirect')
def redirect():

    data = {
        "vads_action_mode": "INTERACTIVE",
        "vads_amount": str(int(request.form["amount"]) * 100),
        "vads_ctx_mode": MODE,
        "vads_currency": "604",  # Moneda PEN
        "vads_cust_email": request.form["email"],
        "vads_page_action": "PAYMENT",
        "vads_payment_config": "SINGLE",
        "vads_site_id": SHOP_ID,
        "vads_url_success": "http://127.0.0.1:5000/resultado",
        "vads_return_mode": "POST",
        "vads_trans_date": datetime.utcnow().strftime('%Y%m%d%H%M%S'),
        "vads_trans_id": str(int(time.time()) % 1000000),
        "vads_version": "V2",
        "vads_order_id": request.form["order"],
        "vads_redirect_success_timeout": str(5)
    }

    return render_template("redirect.html", data={"redirect": data, "url_izipay": URL_IZIPAY, "signature": get_signature(data, KEY)})


@app.post('/resultado')
def paidResult():

    vadsResult = request.form.get("vads_result")
    vadsTransStatus = request.form.get("vads_trans_status")
    vadsAmount = request.form.get("vads_amount")
    vadsOrder = request.form.get("vads_order_id")

    return render_template("result.html", data={'result' : vadsResult, 'status': vadsTransStatus, 'monto': vadsAmount, 'order': vadsOrder})


@app.post('/ipn')
def ipn():
    signature = request.form.get("signature")

    print("IPN")
    print(request.form)
    print("Signature: " + signature)

    if signature == get_signature(request.form, KEY):
        return 'Correcto', 200
    else:
        return 'Acceso denegado', 500


if __name__ == '__main__':
    app.run(debug=True)
