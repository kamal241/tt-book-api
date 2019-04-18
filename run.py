from flask import Flask
from app import book_app, api_bp
from models import db

def create_app(config_filename):
	book_app = Flask(__name__)
	book_app.config.from_object(config_filename)

	book_app.register_blueprint(api_bp, url_prefix='/api')

	db.init_app(book_app)

	return book_app

if __name__ == "__main__":
    book_api = create_app("config")
    book_api.run(host="0.0.0.0", port=8080)