from flask import Blueprint, render_template, request

blueprint = Blueprint("vista_encripcion", __name__, "templates" )

import sys
sys.path.append("src")
from controller.EncryptionController import EncryptionController
from model.CipherEngine import CipherEngine

def Encrypt_Validate(text, key):
    if text == "":
        return "El campo del texto a encriptar no puede estar vacío"
    if key == "":
        return "El campo de la clave de encriptación no puede estar vacío"
    for character in key:
        if not character.isalnum():
            return "La clave de encriptación contiene caracteres no válidos o especiales"
    if len(text) < len(key):
            return "La clave es más larga que el texto a encriptar"
    encrypted_text = CipherEngine.EncryptText(text, key)

    cursor = EncryptionController.GetCursor()
    cursor.execute(f"SELECT COUNT(*) FROM cipher WHERE key = '{key}';")
    count = cursor.fetchone()[0]
    if count > 0:
        return "La clave ya está en uso"
    else:
        return None
def Decrypt_Delete_Validate(text, key):
    if text == "":
        return "El campo del texto a desencriptar no puede estar vacío"
    if key == "":
        return "El campo de la clave de desencriptación no puede estar vacío"
    for character in key:
        if not character.isalnum():
            return "La clave de desencriptación contiene caracteres no válidos o especiales"
    if len(text) < len(key):
            return "La clave es más larga que el texto a desencriptar"
    cursor = EncryptionController.GetCursor()
    cursor.execute(f"""select encrypt_text from cipher where key = '{key}' and encrypt_text = '{text}'""")
    decrypted_data = cursor.fetchone()
    if not decrypted_data:
        return "No se encontraron datos en la base de datos para la clave y el texto encriptado proporcionados"
    else:
        return None
    
def Update_Validate(encrypted_text, key, new_text):
    if new_text == "":
        return "El campo del nuevo texto a encriptar no puede estar vacío"
    if encrypted_text == "":
        return "El campo del texto encriptado no puede estar vacío"
    if key == "":
        return "El campo de la clave de desencriptación no puede estar vacío"
    for character in key:
        if not character.isalnum():
            return "La clave de desencriptación contiene caracteres no válidos o especiales"
    if len(encrypted_text) < len(key):
            return "La clave es más larga que el texto encriptado"
    if len(new_text) < len(key):
            return "La clave es más larga que el nuevo texto a encriptar"
    cursor = EncryptionController.GetCursor()
    cursor.execute(f"""select encrypt_text from cipher where key = '{key}' and encrypt_text = '{encrypted_text}'""")
    decrypted_data = cursor.fetchone()
    if not decrypted_data:
        return "No se encontraron datos en la base de datos para la clave y el texto encriptado proporcionados"
    else:
        return None
    

@blueprint.route("/")
def Home():
    return render_template("index.html")

@blueprint.route("/encriptar")
def encriptar():
    return render_template("encriptar.html")

@blueprint.route("/encriptación")
def encriptación():
    text_to_encrypt = request.args["texto_a_encriptar"]
    key = request.args["clave_de_encriptacion"]
    validate = Encrypt_Validate(text_to_encrypt, key)
    if validate:
        return render_template("/errors/error_message.html", mensaje = validate)
    else:
        encrypted_text = EncryptionController.InsertIntoTableEncrypt(text_to_encrypt, key)
        return render_template("/messages/mensaje_encriptado.html", texto_encriptado = encrypted_text, mensaje = "El mensaje encriptado es:")

@blueprint.route("/desencriptar")
def desencriptar():
    return render_template("desencriptar.html")

@blueprint.route("/desencriptación")
def desencriptación():
    key = request.args["clave_de_desencriptacion"]
    encrypted_text  = request.args["texto_a_desencriptar"]
    validate = Decrypt_Delete_Validate(encrypted_text, key)
    if validate:
        return render_template("/errors/error_message.html", mensaje = validate)
    else:
        decrypted_text = EncryptionController.DecryptText(key, encrypted_text)
        return render_template("/messages/mensaje_desencriptado.html", texto_desencriptado = decrypted_text, mensaje = "El mensaje desencriptado es:")

@blueprint.route("/eliminar_registro")
def eliminar_registro():
    return render_template("eliminar_registro.html")

@blueprint.route("/registro_eliminado")
def registro_eliminado():
    key = request.args["clave_a_eliminar"]
    encrypted_text = request.args["texto_a_eliminar"]
    validate = Decrypt_Delete_Validate(encrypted_text, key)
    if validate:
        return render_template("/errors/error_message.html", mensaje = validate)
    else:
        EncryptionController.DeleteFromTable(key, encrypted_text)
        return render_template("/messages/mensaje_registro_eliminado.html", clave = key, texto_encriptado = encrypted_text)

@blueprint.route("/actualizar_registro")
def actualizar_registro():
    return render_template("/actualizar_registro.html")

@blueprint.route("/registro_actualizado")
def registro_actualizado():
    key = request.args["clave"]
    encrypted_text = request.args["texto_encriptado"]
    new_text = request.args["nuevo_texto"]
    validate = Update_Validate(encrypted_text, key, new_text)
    if validate:
        return render_template("/errors/error_message.html", mensaje = validate)
    else:
        new_encrypted_text = EncryptionController.UpdateFromTable(key, encrypted_text, new_text)
        return render_template("/messages/mensaje_registro_actualizado.html", clave = key, texto_encriptado = encrypted_text, nuevo_texto_encriptado = new_encrypted_text)