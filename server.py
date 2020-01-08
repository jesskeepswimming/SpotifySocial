from flask import *
from api_interface import refresh

app = Flask(__name__) # instantiates a flask object in app keyword

@app.route('/', methods = ['POST'])
def index():
	return render_template('/index.html')

@app.route('/refresh', methods = ['POST'])
def refresh():
	return render_template('/index.html', data = refresh())

if __name__ == '__main__':
    app.run(debug=True)