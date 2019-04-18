from flask import Flask
from flask import Blueprint
from flask_restful import Api

from resources.book_resource import BookResource
from resources.booklist_resource import BookListResource
from resources.external_book_resource import ExternalBookResource

book_app = Flask(__name__)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ExternalBookResource, '/external-books', endpoint = 'externam-books')
api.add_resource(BookListResource, '/v1/books', endpoint = 'books')
api.add_resource(BookResource, '/v1/books/<int:id>', endpoint = 'book', methods = ['GET', 'POST', 'PATCH', 'DELETE'])
