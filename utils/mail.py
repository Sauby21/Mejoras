from flask_mail import Mail, Message

class mail:
    SECRET_KEY = '123456'
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'CondosaCondominios@gmail.com'
    MAIL_PASSWORD = 'htghjytuhbugcefs'
   
    

mail_instance = Mail()  # Crear una instancia de Flask-Mail

# Configurar la instancia de Flask-Mail con la configuración
def configure_mail(app):
    mail_instance.init_app(app)