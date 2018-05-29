from flask import Flask
import json
from processor import Processor

app = Flask(__name__)

processor =  Processor()
@app.route('/')
data_dict = {}
def index():
	jsonFile = json.dump(processor.getData(data_dict))
	return jsonFile

if(__name__ == '__main__'):
	app.run()
