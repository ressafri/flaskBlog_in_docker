# Create tables for all models
from app import db
from counter.models import *
db.create_all()

user_1 = User(username='redwan', email='redwan@demo.com', password='password')
db.session.add(user_1)

user_2 = User(username='marian', email='mariam@demo.com', password='password')
db.session.add(user_2)

db.session.commit()
