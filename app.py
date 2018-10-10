from flask import Flask, jsonify, request, Response

app = Flask(__name__)

fruits = [
	{
		'name': 'apple',
		'color': 'red',
		'description': 'A crunchy yet refreshing treat'
	},
	{
		'name': 'grape',
		'color': 'green',
		'description': 'they are small and squishy'
	},
	{
		'name': 'orange',
		'color': 'orange',
		'description': 'tangy slices of goodness'
	},
	{
		'name': 'starfruit',
		'color': 'yellowish green',
		'description': 'an odd shaped fruit that actually looks like a star!'
	},
	{
		'name': 'watermelon',
		'color': 'green/red/black/white',
		'description': 'so juicy! perfect for the summer'
	}
]

# GET /fruits
@app.route('/fruits')
def get_fruits():
	return jsonify({'fruits': fruits})

# POST sanitization
def validFruitObject(fruitObject):
	if ("name" in fruitObject and "color" in fruitObject and "description" in fruitObject):
		return True
	else:
		return False

# /fruits/name
@app.route('/fruits', methods=['POST'])
def add_fruit():
	request_data = request.get_json()
	if(validFruitobject(request_data)):
				new_fruit = {
			"name": request_data['name'],
			"color": request_data['color'],
			"description": request_data['description']
		}
		fruits.insert(0, request_data)
		response = Response("", 201, mimetype="application/json")
		response.headers['Location'] = "/fruits/" + str(new_fruit['name'])
		return response
	else:
		invalidFruitObjectErrorMsg = {
			"error": "Invalid fruit object passed into request",
			"helpString": "Data passing in must be similar to this {'name': 'fruit name', 'color': 'fruit color', 'description': 'fruit description'}"
		}
		response = Response(json.dumps(invalidFruitObjectErrorMsg), status=400, mimetype='application/json'):
		return response


@app.route ('/fruits/<string:name>')
def get_fruit_by_name(name):
	return_value = {}
	print(type(name))
	for fruit in fruits:
		if fruit["name"] == name:
			return_value = {
				'color': fruit["color"],
				'description': fruit["description"]
			}
	return jsonify(return_value)

# PUT /fruits/newFruitName
@app.route('/fruits/<string:name>', method=['PUT'])
def replace_fruit(name):
	return jsonify(request.get_json())

app.run(port=5000)