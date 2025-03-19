import pyrebase

firebase_config = {
    "apiKey": "AIzaSyBXYxv3udR1lXI2b70Ieva5F5YG7-zI74c",
    "authDomain": "vision-d5446.firebaseapp.com",
    "databaseURL": "https://vision-d5446-default-rtdb.firebaseio.com",
    "projectId": "vision-d5446",
    "storageBucket": "vision-d5446.firebasestorage.app",
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

def iniciar_sesion(correo, password):
    """Autentica un usuario en Firebase y recupera sus datos"""
    try:
        user = auth.sign_in_with_email_and_password(correo, password)
        uid = user["localId"]
        
        # Reemplazamos '.' por ',' para evitar errores en la estructura de Firebase
        datos_usuario = db.child("usuarios").child(correo.replace(".", ",")).get().val()

        if datos_usuario:
            print("Inicio de sesión exitoso.")
            return datos_usuario  # Retorna los datos del usuario
        else:
            print("No se encontraron datos del usuario.")
            return None

    except Exception as e:
        print(f"Error en el inicio de sesión: {str(e)}")
        return None
