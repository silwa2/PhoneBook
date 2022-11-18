
from flask import Flask


app = Flask (__name__)

@app.route('/')
def main():
    return "<h1>Hello World<h1><br><a href='/index'>перейти на следующую страницу<a>"

@app.route('/index/<x>/<y>')
def index(x,y):
    return f'<h1>Результат {int(x)+int(y)}<h1>'

if __name__ == '__main__':
    app.run()
