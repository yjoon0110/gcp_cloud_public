from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Welcome to Python Flask World 1.0 for automation'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
