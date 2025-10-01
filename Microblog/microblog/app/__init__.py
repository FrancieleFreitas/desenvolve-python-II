import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = "PD12345678" 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///microblog.db"

db.init_app(app)

login = LoginManager(app)
login.login_view = 'login' 

# 1. IMPORTAÇÃO DOS MODELOS (AQUI PARA QUEBRAR O CICLO E PARA O user_loader)
from app.models.models import User, Post 

# 2. Define o user_loader
@login.user_loader 
def load_user(id):
    return db.session.get(User, int(id))

# 3. Importa as rotas e alquimias NO FINAL
from app import routes, alquimias

with app.app_context():
    db.create_all()

