from flask import *
from api_interface import get_currently_playing

app = Flask(__name__) # instantiates a flask object in app keyword

@app.route('/')
def index():
	return render_template('/index.html', data = get_currently_playing())

if __name__ == '__main__':
    app.run(debug=True)