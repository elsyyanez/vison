import web  # Carga la librería web.py

# Importar controladores
from controllers.index import Index
from controllers.usuario import Usuario
from controllers.inicio_sesion import InicioSesion
from controllers.bienvenida_admin import BienvenidaAdmin

# Definir rutas
urls = (
    '/', 'Index',
    '/usuario', 'Usuario',
    '/inicio_sesion', 'InicioSesion',
    '/static/(.*)', 'Static',
    '/bienvenida_admin', 'BienvenidaAdmin',
)


# Iniciar aplicación
app = web.application(urls, globals())

if __name__ == "__main__":
    try:
        app.run()
    except Exception as error:
        print(f"ERROR: {str(error)}")