from flask import Flask
from utils.config import Config
from flask import Flask
from utils.config import Config

def crear_app():
    app = Flask(__name__)
    #CARGAR CONFIGURACION
    app.config.from_object(Config)
    #BLUEPRINTS
    from routes import login
    app.register_blueprint(login.bp)
    
    from routes import principal
    app.register_blueprint(principal.bp)
    
    from routes import contratos
    app.register_blueprint(contratos.routes)
    return app