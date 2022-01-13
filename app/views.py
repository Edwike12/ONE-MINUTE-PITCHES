from flask import render_template
from app import app

# Views
@app.route('/pitch/<int:pitch_id>')
def index(pitch_id):

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('one_minute_pitch.html',id = pitch_id)