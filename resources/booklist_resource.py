from flask import request
from flask_restful import Resource
from models import db, Book, BookSchema
from models import book_schema
from models import books_schema

class BookListResource(Resource):
    def get(self):
        books_data = []
        if 'name' in request.args:
            book_name = request.args.get('name')
            books = Book.query.filter(Book.name.contains(book_name))            
        elif 'country' in request.args:
            book_country = request.args.get('country')
            #books = Book.query.filter_by(country=book_country)
            books = Book.query.filter(Book.country.contains(book_country))
        elif 'publisher' in request.args:
            book_publisher = request.args.get('publisher')
            #books = Book.query.filter_by(publisher=book_publisher)
            books = Book.query.filter(Book.publisher.contains(book_publisher))
        elif 'release_date' in request.args:
            book_release_year = request.args.get('release_date')
            books = Book.query.filter(Book.release_date.contains(book_release_year))
        else:
            books = Book.query.all()
    
        if books:
            books_data = books_schema.dump(books).data

        pbooks_data = [ self._serialise_author(ibook) for ibook in books_data ]
        return {'status_code' : 200 ,'status': 'success', 'data': pbooks_data}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        try:
            book = Book.query.filter_by(name=json_data['name']).first()
            if book:
                return {'message': 'book already exists'}, 400

            book_data = self._deserialise_author(json_data)

            book = Book(
                    isbn = book_data['isbn'], 
                    name = book_data['name'],            
                    authors = book_data['authors'], 
                    number_of_pages = book_data['number_of_pages'],
                    publisher = book_data['publisher'],
                    country = book_data['country'],
                    release_date = book_data['release_date']
                    )
            db.session.add(book)
            db.session.commit()
            result = self._serialise_author(book_schema.dump(book).data)
            return {'status_code' : 201, 'status': 'success', 'data': [ result ] }, 201
        except KeyError:
            return {'status_code' : 400, 'status': 'One or more required field missing', 'data': [] }, 400


    def _serialise_author(self, book):
        book['authors'] = book['authors'].split(",")
        return book

    def _deserialise_author(self, data):
        data['authors'] = ",".join(data['authors'])
        return data