from flask import Flask
import json
from processor import Processor
from Extract_cities_coordinates import Extractor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
processor =  Processor()
@app.route('/')
data_dict = {}
def index():
	extractor = Extractor(request.args.get('sport'))
	return extractor.get_most_popular_city()

if(__name__ == '__main__'):
	app.run()
