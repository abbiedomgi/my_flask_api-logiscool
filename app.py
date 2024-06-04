from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/api/v1/resources/books', methods=['GET'])
def get_books():
    books = [
        {'id': 1, 'title': '1984', 'author': 'George Orwell'},
        {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
        {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
    ]
    return jsonify(books)

@app.route('/api/v1/resources/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    books = [
        {'id': 1, 'title': '1984', 'author': 'George Orwell'},
        {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
        {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
    ]
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
