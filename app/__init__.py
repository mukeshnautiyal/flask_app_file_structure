from flask import Flask

from config import Config
from app.extensions import db
from flask_migrate import Migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    
    db.init_app(app)
    migrate = Migrate(app, db)
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')
    
    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/auth/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app