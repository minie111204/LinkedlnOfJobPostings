from flask import Flask
from flask_cors import CORS
from sqlalchemy import text
from app.routes.posting import posting_bp
from app.routes.dashboard import dashboard_bp

from app.routes.apiNguyen import GN_bp
from app.routes.company_routes import company_routes

from config import Config
from app.models import db

def create_app():
    
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(posting_bp, url_prefix='/api/v1')
    app.register_blueprint(dashboard_bp, url_prefix='/api/v1')
    app.register_blueprint(GN_bp, url_prefix='')
    app.register_blueprint(company_routes, url_prefix='/api/company')
   
    @app.route('/test-db-connection')
    def test_db_connection():
        try:
            # Wrap the SQL query in the text() function
            result = db.session.execute(text('SELECT 1'))
            return "Database connection is successful!"
        except Exception as e:
            return f"Error: {str(e)}", 500


    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)