import os
from flask import Flask
from flask_migrate import Migrate
from app.config import Config, db
from app.routes import main_routes 
from app.models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True) #Migraciones en caso de cambios en el modelo de datos


app.register_blueprint(main_routes) #Registrar rutas

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001, debug=True)
