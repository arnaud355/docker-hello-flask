# server.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)

# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('x', type=int, default=False, required=False)
parser.add_argument('y', type=int, default=False, required=False)

class HelloWorld(Resource):
    def get(self):
        return {'bonjour': 'world'}

class Meteo(Resource):
    def get(self,x):
        return {x}

class Info_ville_Meteo(Resource):
    def get(self,x):
        return {x}

class Multiply(Resource):
    def get(self, x):
        result = x * x
        return {'result':result}

class Even(Resource):
    def get(self, x):
        result_even = x % 2
        if result_even == 0:
            return {'Le nombre est pair':result_even}
        else:
            return {'Le nombre est impair': result_even}

class Add(Resource):
    def get(self):
        args = parser.parse_args()
        x = args['x']
        y = args['y']
        #api.add_resource(Add, '/add/?x=<int:x>&y=<int:y>')
        result = int(x) + int(y)
        return {"result":result}

    #def post(self):
    #    args = parser.parse_args()
    #    todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
    #    todo_id = 'todo%i' % todo_id
    #    TODOS[todo_id] = {'task': args['task']}
     #   return TODOS[todo_id], 201

# url: http://127.0.0.1:5000/example-requetes?language=Python&framework=Flask&website=arn
@app.route('/example-requetes')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    website = request.args.get('website')

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)

#url: http://127.0.0.1:5000/form-example?language=Python&framework=Flask&website=arn
@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

api.add_resource(HelloWorld, '/hello')
api.add_resource(Multiply, '/multiply/<int:x>')
#api.add_resource(Add, '/add/?x=<int:x>&y=<int:y>')
api.add_resource(Add, '/add/')
api.add_resource(Even, '/even/<int:x>')
api.add_resource(Meteo, 'https://www.metaweather.com/api/location/search/?query=<string:x>')
api.add_resource(Info-ville-Meteo, 'https://www.metaweather.com/api/location/<int:x>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')