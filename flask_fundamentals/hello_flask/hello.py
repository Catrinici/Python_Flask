from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/success')
def succes():
    return "succes"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "hello "+name

@app.route('/users/<username>/<id>')
def show_user_profile(username,id):
    print(username)
    print(id)
    return "username: "+username + ", id: " + id

if __name__ == "__main__":
    app.run(debug = True)