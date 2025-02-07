from flask import Flask
from application.models import db,User,Role
from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password
from config import DevelopmentConfig
from application.resorces import api
from application.sec import datastore
def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    app.security = Security(app , datastore)
    with app.app_context():
        import application.views
    return app
    
app = create_app()    

if __name__ == '__main__':
    app.run(debug = True) 