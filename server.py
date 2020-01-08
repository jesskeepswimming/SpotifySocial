from flask import *
from api_interface import refresh 

app = Flask(__name__) # instantiates a flask object in app keyword

@app.route('/')
def index():
	return render_template('/index.html')

@app.route('/sync', methods = ['POST'])
def sync():
    oauth1 = request.form['Player']
    oauth2 = request.form['Listener']
    return render_template('/index.html', data = refresh(oauth1, oauth2))

if __name__ == '__main__':
    app.run(debug=True)