from main import app
from application.sec import datastore
from application.models import db,Role
from flask_security import hash_password
from werkzeug.security import generate_password_hash 
with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name = 'admin' , description = 'User ia an admin')
    datastore.find_or_create_role(name = 'sponsor' , description = 'User ia an sponsor')
    datastore.find_or_create_role(name = 'influencer' , description = 'User ia an influencer')
    db.session.commit()
    if not datastore.find_user(email = 'admin@email.com'):
        datastore.create_user(username = 'admin', email = 'admin@email.com', password =generate_password_hash('admin1') ,roles = ['admin'])
    if not datastore.find_user(email = 'sponsor1@email.com'):
        datastore.create_user(username = 'sponsor1', email = 'sponsor1@email.com', password =generate_password_hash('sponser1') ,roles = ['sponsor'], active = False)
    if not datastore.find_user(email = 'influencer1@email.com'):
        datastore.create_user(username = 'influencer1', email = 'influencer1@email.com', password =generate_password_hash('influencer1') ,roles = ['influencer'], active =False)
    db.session.commit()    
