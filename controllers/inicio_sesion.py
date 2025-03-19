import web
from models.admin import iniciar_sesion

render = web.template.render('views/')

class InicioSesion:
    def GET(self):
        # Este es el mensaje que se quere imprimir
        mensaje=None
        return render.inicio_sesion(mensaje)

    def POST(self):
        try:
            datos = web.input()
            email = datos.email
            password = datos.password
            print(f"email: {email}, password: {password}")
            usuario = iniciar_sesion(email, password)
            print(f"datos del usuario: {usuario}")
                

            if usuario:
                return web.seeother('/bienvenida_admin')
            else:
                mensaje ="Correo o contraseña incorrectos."
                return render.inicio_sesion(mensaje) 

        # Se llama al mensaje 
        except Exception as e:
            mensaje = f" Error en inicio de sesión: {str(e)}"
            print(mensaje)  
            return render.inicio_sesion(mensaje)
