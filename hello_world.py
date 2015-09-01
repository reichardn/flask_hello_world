from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())
    
@app.route("/jedi/<first>/<last>")
def jedi(first, last):
    jedi_name = last[:3] + first[:2]
    return "Your jedi name is {}".format(jedi_name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            
