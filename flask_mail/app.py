from flask import Flask
from flask_mail import Mail


def create_app():
    app = Flask(__name__)
    
    app.config['MAIL_SERVER'] = 'smtp.fastmail.com'
    app.config['MAIL_PORT'] = 456
    app.config['MAIL_USERNAME'] = 'seriffiratkara@gmail.com'
    app.config['MAIL_PASSWORD'] = ''
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_DEFAULT_SENDER'] = 'seriffiratkara@gmail.com'
    app.config['MAIL_MAX_EMAIL'] = 26
    
    
    mail = Mail()
    mail.init_app(app)
    
    @app.route('/')
    def index():
        msg = Message('hello',recipients=['sfkara@gmail.com'])
        msg.add_recipients(recipients=['fk@gmail.com'])
        msg.html = 'sent'
        mail.send(msg)
        
        return '<h1>Sent!!!!</h1>'
    @app.route('/bulk')
    def bulk():
        users = [{'name':'Fırat','email':'kara@gmail.com'}]
        
        with mail.connect() as connect:
            for user in users:
                msg = Message('Bulk',recipients=[user['email']])
                msg.body = 'hello {}'.format(user['name'])
                connect.send(msg)
    
    return app