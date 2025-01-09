# Redirect-PaymentForm-Python-Flask

<p align="center">
  <img src="https://github.com/izipay-pe/Imagenes/blob/main/logos_izipay/logo-izipay-banner-1140x100.png?raw=true" alt="Formulario" width=100%/>
</p>

## Índice

➡️ [1. Introducción](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#%EF%B8%8F-1-introducci%C3%B3n)  
🔑 [2. Requisitos previos](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-2-requisitos-previos)  
🚀 [3. Ejecutar ejemplo](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-3-ejecutar-ejemplo)  
🔗 [4. Pasos de integración](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#4-pasos-de-integraci%C3%B3n)  
💻 [4.1. Desplegar pasarela](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#41-desplegar-pasarela)  
💳 [4.2. Analizar resultado de pago](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#42-analizar-resultado-del-pago)  
📡 [4.3. Pase a producción](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#43pase-a-producci%C3%B3n)  
🎨 [5. Personalización](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-5-personalizaci%C3%B3n)  
📚 [6. Consideraciones](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-6-consideraciones)

## ➡️ 1. Introducción

En este manual podrás encontrar una guía paso a paso para configurar un proyecto de **[PYTHON]** con la pasarela de pagos de IZIPAY. Te proporcionaremos instrucciones detalladas y credenciales de prueba para la instalación y configuración del proyecto, permitiéndote trabajar y experimentar de manera segura en tu propio entorno local.
Este manual está diseñado para ayudarte a comprender el flujo de la integración de la pasarela para ayudarte a aprovechar al máximo tu proyecto y facilitar tu experiencia de desarrollo.


<p align="center">
  <img src="https://github.com/izipay-pe/Imagenes/blob/main/formulario_redireccion/Imagen-Formulario-Redireccion.png?raw=true" alt="Formulario" width="750"/>
</p>

## 🔑 2. Requisitos Previos

- Comprender el flujo de comunicación de la pasarela. [Información Aquí](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/guide/start.html)
- Extraer credenciales del Back Office Vendedor. [Guía Aquí](https://github.com/izipay-pe/obtener-credenciales-de-conexion)
- Para este proyecto utilizamos Python 3.12
- Para este proyecto utilizamos la herramienta Visual Studio Code.

> [!NOTE]
> Tener en cuenta que, para que el desarrollo de tu proyecto, eres libre de emplear tus herramientas preferidas.

## 🚀 3. Ejecutar ejemplo

### Instalar Plugin "Python"
Python, extensión para Visual Studio Code que ofrece soporte completo para el lenguaje Python (para todas las versiones del lenguaje >= 3.7). Para instalarlo:
1. Ingresar a la sección "Extensiones" de Visual Studio Code
2. Buscar "Python"
3. Instalar extensión

<p align="center">
  <img src="https://i.postimg.cc/XYZKRcNJ/Plugin.png" alt="Plugin" width="850"/>
</p>

### Clonar el proyecto
```sh
git clone https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask
```

### Datos de conexión 

Reemplace **[CHANGE_ME]** con sus credenciales de `API` extraídas desde el Back Office Vendedor, revisar [Requisitos previos](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-2-requisitos-previos).

- Editar el archivo `key.py` en la ruta raíz:
```python
credentials = {
    # Identificador de su tienda
    "SHOP_ID": "~ CHANGE_ME_USER_ID ~",
    # Clave de Test o Producción
    "KEY": "~ CHANGE_ME_KEY ~",
    }
```

### Preparar el entorno:
Antes de ejecutar el proyecto, se creará el virtual environment (venv):
1. Presionar `ctrl` + `shift` + `p` para abrir la paleta de comandos y buscar `Python: Select Interpreter`
<p align="center">
  <img src="https://i.postimg.cc/yYpXprHt/Select-Interpreter.png" alt="PanelComandos" width="600"/>
</p>
2. Seleccionar `Create Virtual Environment`
<p align="center">
  <img src="https://i.postimg.cc/43fcJ6sV/Create-Env.png" alt="CreateVenv" width="600"/>
</p>
3. Seleccionar el tipo de venv
<p align="center">
  <img src="https://i.postimg.cc/PJ2zjS8L/Venv.png" alt="SelectVenv" width="600"/>
</p>
4. Seleccionar la versión de Python
<p align="center">
  <img src="https://i.postimg.cc/1RHKw3Y9/Select-Python.png" alt="SelectPython" width="600"/>
</p>
5. Seleccionar archivo de dependencias `requirements.txt`
<p align="center">
  <img src="https://i.postimg.cc/pr2Y4wyb/Requirements.png" alt="SelectRequirements" width="600"/>
</p>

### Ejecutar proyecto
1. Para ejecutar el proyecto a través de Visual Studio, ingresar a la sección "Ejecutar" y seleccionar `Run and Debug`
<p align="center">
  <img src="https://i.postimg.cc/8sQdxm4D/Ejecutar.png" alt="SelectInterpreter" width="400"/>
</p>
2. Seleccionar el debugger: `Python Debugger`
<p align="center">
  <img src="https://i.postimg.cc/yxSXfbFv/Debugger.png" alt="SelectRequirements" width="600"/>
</p>
3. Seleccionar la configuración del debugger `Flask`
<p align="center">
  <img src="https://i.postimg.cc/wvrQQps1/Debug-conf.png" alt="SelectRequirements" width="600"/>
</p>
4. El proyecto se ha ejecutado y es accesible a través de:

 ```sh
  http://127.0.0.1:5000
 ```


## 🔗4. Pasos de integración

<p align="center">
  <img src="https://i.postimg.cc/pT6SRjxZ/3-pasos.png" alt="Formulario" />
</p>

## 💻4.1. Desplegar pasarela
### Autentificación
Extraer las claves de `identificador de tienda` y `clave de test o producción` del Backoffice Vendedor y agregarlo en los parámetros `vads_site_id` y en la función `calculateSignature(parameters)`. Este último permite calcular la firma transmitida de los datos de pago. Podrás encontrarlo en el archivo `controller.py`.
```python
def dataForm(parameters):
    # Obteniendo usuario
    username = credentials["SHOP_ID"]

    new_params = OrderedDict()

    # Definir los parámetros vads_ y sus valores
    new_params = {
            "vads_site_id": username,  # ID de tienda
            ...
            ...
        }

    # Calcular el signature
    signature = calculateSignature(new_params)

    # Agregar el signature
    new_params["signature"] = signature

    # Retornar los parámetros
    return new_params

def calculateSignature(parameters):
    # Obtener la clave API
    key = credentials["KEY"]
    ...
    ...
    # Retornar Firma
    return signature
```

ℹ️ Para más información: [Autentificación](https://secure.micuentaweb.pe/doc/es-PE/form-payment/quick-start-guide/identificarse-durante-los-intercambios.html)
### Visualizar formulario
Para desplegar la pasarela, crea un formulario **HTML** de tipo **POST** con el valor del **ACTION** con la url de servidor de la pasarela de pago y agregale los parámetros de pago como etiquetas `<input type="hidden" name="..." value="{{ ... }}" />`. Como se muestra el ejemplo en la ruta del archivo `templates/checkout.html` 

```html
<!-- Formulario con los datos de pago -->
<form class="from-checkout" action="https://secure.micuentaweb.pe/vads-payment/" method="post">
		<!-- Inputs generados dinámicamente -->
		<input type="hidden" name="vads_action_mode" value="{{ parameters.vads_action_mode }}" />
		...
    ...
		<input type="hidden" name="signature" value="{{ parameters.signature }}" />
		<button class="btn btn-checkout" type="submit" name="pagar">Pagar</button>
</form>	
```
ℹ️ Para más información: [Formulario de pago en POST](https://secure.micuentaweb.pe/doc/es-PE/form-payment/quick-start-guide/enviar-un-formulario-de-pago-en-post.html)

## 💳4.2. Analizar resultado del pago

### Validación de firma
Se configura el método `calculateSignature(parameters)` que generará la firma de los datos de la respuesta de pago. Podrás encontrarlo en el archivo `controller.py`.

```python
def calculateSignature(parameters):
    # Obtener la clave API
    key = credentials["KEY"]
    ...
    ...
    # Calcular Firma
    hash_object = hmac.new(key.encode('utf-8'), content_signature.encode('utf-8'), hashlib.sha256)
    hash_bytes = hash_object.digest()
    signature = base64.b64encode(hash_bytes).decode('utf-8')
    
    # Retornar Firma
    return signature
```

Se valida que la firma recibida es correcta en `checkSignature(parameters)`. Podrás encontrarlo en el archivo `controller.py`.

```python
def checkSignature(parameters):
    # Obtener el signature de la respuesta
    signature = parameters["signature"]

    # Verifica la integridad de el signature recibido y el generado
    return signature == calculateSignature(parameters) 
```
En caso que la validación sea exitosa, se renderiza el template con los valores. Como se muestra en el archivo `templates/result.html`.

```html
<p><strong>Estado:</strong> <span>{{ data.vads_trans_status }}</span></p>
<p><strong>Monto:</strong> <span>{% if data.vads_currency == '604' %}PEN{% else %}USD{% endif %}</span><span>{{ (data.vads_amount | float) / 100 }}</span></p>
<p><strong>Order-id:</strong> <span>{{ data.vads_order_id }}</span></p>
```
ℹ️ Para más información: [Analizar resultado del pago](https://secure.micuentaweb.pe/doc/es-PE/form-payment/quick-start-guide/recuperar-los-datos-devueltos-en-la-respuesta.html)

### IPN
La IPN es una notificación de servidor a servidor (servidor de Izipay hacia el servidor del comercio) que facilita información en tiempo real y de manera automática cuando se produce un evento, por ejemplo, al registrar una transacción.

Se realiza la verificación de la firma y se retorna una respuesta del estado del pago. Podrás encontrarlo en el archivo `app.py`.

```python
@app.post('/ipn')
def ipn():
    if not request.form: raise Exception("no post data received!")

    ipnParameters = request.form.to_dict()
    
    if not checkSignature(ipnParameters) : raise Exception("Invalid signature")

    # Obtener el estado de la transacción
    orderStatus = ipnParameters["vads_trans_status"]
    
    # Retorna la respuesta del Order Status
    return 'OK! OrderStatus is ' + orderStatus, 200
```

La IPN debe ir configurada en el Backoffice Vendedor, en `Configuración -> Reglas de notificación -> URL de notificación al final del pago`

<p align="center">
  <img src="https://github.com/izipay-pe/Imagenes/blob/main/formulario_redireccion/Url-Notificacion-Redireccion.png?raw=true" alt="Url de notificacion en redireccion" width="650" />
</p>

ℹ️ Para más información: [Analizar IPN](https://secure.micuentaweb.pe/doc/es-PE/form-payment/quick-start-guide/implementar-la-ipn.html)

## 5. Transacción de prueba

Antes de poner en marcha su pasarela de pago en un entorno de producción, es esencial realizar pruebas para garantizar su correcto funcionamiento. 

Puede intentar realizar una transacción utilizando una tarjeta de prueba (en la parte inferior del formulario).

<p align="center">
  <img src="https://github.com/izipay-pe/Imagenes/blob/main/formulario_redireccion/Imagen-Formulario-Redireccion-testcard.png?raw=true" alt="Tarjetas de prueba" width="450"/>
</p>

- También puede encontrar tarjetas de prueba en el siguiente enlace. [Tarjetas de prueba](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/api/kb/test_cards.html)

## 📡4.3.Pase a producción

Reemplace **[CHANGE_ME]** con sus credenciales de PRODUCCIÓN extraídas desde el Back Office Vendedor, revisar [Requisitos Previos](https://github.com/izipay-pe/Redirect-PaymentForm-Python-Flask/tree/main?tab=readme-ov-file#-2-requisitos-previos).

- Editar el archivo `key.py` en la ruta raíz:
```python
credentials = {
    # Identificador de su tienda
    "SHOP_ID": "~ CHANGE_ME_USER_ID ~",
    # Clave de Test o Producción
    "KEY": "~ CHANGE_ME_KEY ~",
    }
```

## 🎨 5. Personalización

Si deseas aplicar cambios específicos en la apariencia de la página de pago, puedes lograrlo mediante las opciones de personalización en el Backoffice. En este enlace [Personalización - Página de pago](https://youtu.be/hy877zTjpS0?si=TgSeoqw7qiaQDV25) podrá encontrar un video para guiarlo en la personalización.

<p align="center">
  <img src="https://github.com/izipay-pe/Imagenes/blob/main/formulario_redireccion/Personalizacion-formulario-redireccion.png?raw=true" alt="Personalizacion de formulario en redireccion"  width="750" />
</p>

## 📚 6. Consideraciones

Para obtener más información, echa un vistazo a:

- [Formulario incrustado: prueba rápida](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/quick_start_js.html)
- [Primeros pasos: pago simple](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/javascript/guide/start.html)
- [Servicios web - referencia de la API REST](https://secure.micuentaweb.pe/doc/es-PE/rest/V4.0/api/reference.html)
