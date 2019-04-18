from flask import request
from flask_restful import Resource
from models import db, Book, BookSchema

from models import book_schema

class BookResource(Resource):
    def get(self, id):
        book_data = []
        book = db.session.query(Book).filter(Book.id == id).first()
        if not book:
            return {'status_code' : 404 ,'status': 'success','message': "Book {} doesn't exist".format(id), 'data': []}, 404
        else:
            book_data = book_schema.dump(book).data
            book_data['authors'] = book_data['authors'].split(',')
        return {'status_code' : 200 ,'status': 'success', 'data': book_data}, 200

    def patch(self, id):
        json_data = request.get_json(force=True)
        result = []
        if not json_data:
               return {'message': 'No input data provided'}, 400

        book = Book.query.filter_by(id=id).first()
        if not book:
            return { 'status_code' : 200, 'status': 'success', 'message':'book does not exist' }, 400
        else:
            name = json_data['name'] if 'name' in json_data else book.name
            isbn = json_data['isbn'] if 'isbn' in json_data else book.isbn
            if 'authors' in json_data:
                json_data = self._deserialise_author(self, json_data['authors'])  
            else:
                authors = book.authors        
            number_of_pages = json_data['number_of_pages'] if 'number_of_pages' in json_data else book.number_of_pages
            publisher = json_data['publisher'] if 'publisher' in json_data else book.publisher
            country = json_data['country'] if 'country' in json_data else book.country
            release_date = json_data['release_date'] if 'release_date' in json_data else book.release_date

            book.name = name
            book.isbn = isbn
            book.authors = authors
            book.publisher = publisher
            book.country = country
            book.release_date = release_date

            db.session.commit()

            result = book_schema.dump(book).data
            message = "The book {} was updated successfully".format(book.name)
        
        return { 'status_code' : 200, 'status': 'success', 'message': message,'data': [ result ] }, 200

    def delete(self, id):
        book = Book.query.filter_by(id=id).first()        
        if not book:
            return { 'status_code' : 200, 'status': 'success', 'message':'book does not exist' }, 400
        else:            
            message = "The book {} was deleted successfully".format(book.name)            
            db.session.delete(book)
            db.session.commit()
            return { 'status_code' : 204, 'status': 'success', 'message': message,'data': [] }, 200

    def _serialise_author(self, book):
        book['authors'] = book.authors.split(",")
        return book

    def _deserialise_author(self, data):
        data['authors'] = ",".join(data['authors'])
        return data