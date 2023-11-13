import os
from flask import Flask
from config import Config
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


from flask_migrate import Migrate

# Importing all extensions
from core.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # ! Extensions 
    # All extensions are registered here
    db.init_app(app)

    migrate = Migrate(app, db)
  
    # ! Blueprints
    # All blueprints are registered here
    from core.main import bp as main_bp
    app.register_blueprint(main_bp)





    @app.route('/test/')
    def test_page():
        return '<h1>Testing flask factory</h1>'
    
    

    return app
