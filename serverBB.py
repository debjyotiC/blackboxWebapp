from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/<arg>')
def index(arg):
    names_addr = {'a': 'farakka', 'b': 'Canada', 'c': 'kolkata'}
    return names_addr[arg]


if __name__ == '__main__':
    app.run(host='192.168.1.6')



