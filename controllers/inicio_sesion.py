import web
from models.admin import iniciar_sesion

render = web.template.render('views/')

class InicioSesion:
    def GET(self):
        return render.inicio_sesion()

        def POST(self):
            try:
                datos = web.input()
                email = datos.email
                password = datos.password

                usuarios = iniciar_sesion(email, password)

                if usuarios:
                    return web.seeother('/bienvenida_admin')
                else:
                    return render.iniciosesion(error="Correo o contraseña incorrectos.") 
            
            except Exception as e:
                error_msg = f" Error en inicio de sesión: {str(e)}"
                print(error_msg)  
                return render.iniciosesion(error=error_msg)