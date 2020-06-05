from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=""):
    fahrenheit = str(float(celsius) * 9.0 / 5 + 32)
    return fahrenheit


if __name__ == '__main__':
    app.run()
