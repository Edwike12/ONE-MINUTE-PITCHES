from flask import render_template
from app import app

# Views
@app.route('/movie/<int:movie_id>')
def index(movie_id):

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello World'
    return render_template('index.html',message = message)